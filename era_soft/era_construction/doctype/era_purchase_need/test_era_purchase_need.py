from __future__ import annotations

import unittest

import frappe
from frappe.model.workflow import apply_workflow
from frappe.tests import IntegrationTestCase
from frappe.utils import add_days, nowdate

PROJECT_MANAGER = "era.project.manager@example.com"
APPROVER = "era.construction.approver@example.com"
BOTH_ROLES = "era.need.owner.approver@example.com"

# This capability test intentionally uses the site's installed ERPNext master data.
# Loading ERPNext's generic Company test records would replace the site's currency
# assumptions (for example, KGS) with the upstream INR test defaults.
IGNORE_TEST_RECORD_DEPENDENCIES = [
	"Company",
	"Project",
	"User",
	"Workflow State",
	"Material Request",
	"Item",
	"UOM",
	"Warehouse",
]


class TestERAPurchaseNeed(IntegrationTestCase):
	@classmethod
	def setUpClass(cls) -> None:
		super().setUpClass()
		frappe.set_user("Administrator")
		cls.company, cls.warehouse, cls.item = cls._get_installed_master_data()

	def setUp(self) -> None:
		super().setUp()
		frappe.set_user("Administrator")
		self.project = self._ensure_project()
		self._ensure_user(PROJECT_MANAGER, "ERA Project Manager")
		self._ensure_user(APPROVER, "ERA Construction Approver")
		self._ensure_user(
			BOTH_ROLES,
			"ERA Project Manager",
			"ERA Construction Approver",
		)

	def tearDown(self) -> None:
		frappe.set_user("Administrator")
		super().tearDown()

	def test_approved_need_creates_submitted_erpnext_purchase_request(self) -> None:
		need = self._make_need(PROJECT_MANAGER)
		self.assertEqual(need.workflow_state, "Draft Need")

		apply_workflow(need, "Submit for Approval")
		need.reload()
		self.assertEqual(need.workflow_state, "Pending Approval")

		frappe.set_user(APPROVER)
		apply_workflow(need, "Approve Need")
		need.reload()

		self.assertEqual(need.workflow_state, "Approved Purchase Request")
		self.assertEqual(need.docstatus, 1)
		self.assertTrue(need.purchase_request)

		purchase_request = frappe.get_doc("Material Request", need.purchase_request)
		self.assertEqual(purchase_request.docstatus, 1)
		self.assertEqual(purchase_request.material_request_type, "Purchase")
		self.assertEqual(purchase_request.custom_era_purchase_need, need.name)
		self.assertEqual(purchase_request.items[0].project, self.project)
		self.assertEqual(purchase_request.items[0].warehouse, self.warehouse)

	def test_owner_cannot_approve_their_own_need(self) -> None:
		need = self._make_need(BOTH_ROLES)
		apply_workflow(need, "Submit for Approval")
		need.reload()

		with self.assertRaises(frappe.ValidationError):
			apply_workflow(need, "Approve Need")

	def test_return_requires_a_decision_reason(self) -> None:
		need = self._make_need(PROJECT_MANAGER)
		apply_workflow(need, "Submit for Approval")
		need.reload()
		frappe.set_user(APPROVER)

		with self.assertRaises(frappe.ValidationError):
			apply_workflow(need, "Return for Revision")

		need.reload()
		need.decision_reason = "Clarify the required quantity."
		need.save()
		apply_workflow(need, "Return for Revision")
		need.reload()
		self.assertEqual(need.workflow_state, "Returned")

	def test_non_stock_item_is_rejected(self) -> None:
		service_item = frappe.db.get_value("Item", {"disabled": 0, "is_stock_item": 0}, "name")
		if not service_item:
			self.skipTest("No active service item is installed on this site.")

		with self.assertRaises(frappe.ValidationError):
			self._make_need(PROJECT_MANAGER, item_code=service_item)

	def _make_need(self, user: str, item_code: str | None = None):
		frappe.set_user(user)
		return frappe.get_doc(
			{
				"doctype": "ERA Purchase Need",
				"title": "Foundation material need",
				"company": self.company,
				"project": self.project,
				"request_date": nowdate(),
				"required_by": add_days(nowdate(), 7),
				"business_reason": "Required to continue foundation work.",
				"items": [
					{
						"item_code": item_code or self.item,
						"qty": 2,
						"target_warehouse": self.warehouse,
					}
				],
			}
		).insert()

	@classmethod
	def _get_installed_master_data(cls) -> tuple[str, str, str]:
		warehouse = frappe.db.get_value(
			"Warehouse",
			{"is_group": 0, "disabled": 0},
			["name", "company"],
			as_dict=True,
		)
		item = frappe.db.get_value("Item", {"disabled": 0, "is_stock_item": 1}, "name")
		if not warehouse or not warehouse.company or not item:
			raise unittest.SkipTest(
				"ERA Purchase Need integration tests require one company warehouse and one active item."
			)
		return warehouse.company, warehouse.name, item

	@classmethod
	def _ensure_project(cls) -> str:
		project_name = f"_Test ERA Construction Need Project {frappe.scrub(cls.company)}"
		project = frappe.db.get_value("Project", {"project_name": project_name}, "name")
		if not project:
			project = (
				frappe.get_doc(
					{
						"doctype": "Project",
						"project_name": project_name,
						"company": cls.company,
						"status": "Open",
					}
				)
				.insert(ignore_permissions=True)
				.name
			)
		return project

	@staticmethod
	def _ensure_user(email: str, *roles: str) -> None:
		if not frappe.db.exists("User", email):
			frappe.get_doc(
				{
					"doctype": "User",
					"email": email,
					"first_name": email.split("@", 1)[0],
					"send_welcome_email": 0,
					"user_type": "System User",
				}
			).insert(ignore_permissions=True)
		frappe.get_doc("User", email).add_roles(*roles)
