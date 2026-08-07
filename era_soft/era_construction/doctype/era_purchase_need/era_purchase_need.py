from __future__ import annotations

import frappe
from frappe import _
from frappe.model.document import Document
from frappe.utils import flt, getdate

DECISION_REASON_STATES = {"Returned", "Rejected"}
CLOSED_PROJECT_STATES = {"Completed", "Cancelled"}


class ERAPurchaseNeed(Document):
	def before_validate(self) -> None:
		if not self.requested_by:
			self.requested_by = frappe.session.user
		self._set_item_defaults()

	def validate(self) -> None:
		self._validate_dates()
		self._validate_project()
		self._validate_decision_reason()
		self._validate_items()

	def on_submit(self) -> None:
		if self.purchase_request:
			frappe.throw(_("A Purchase Request has already been created for this need."))

		purchase_request = frappe.get_doc(
			{
				"doctype": "Material Request",
				"material_request_type": "Purchase",
				"company": self.company,
				"transaction_date": self.request_date,
				"schedule_date": self.required_by,
				"title": self.title,
				"custom_era_purchase_need": self.name,
				"items": [
					{
						"item_code": item.item_code,
						"description": item.description,
						"qty": item.qty,
						"uom": item.uom,
						"schedule_date": self.required_by,
						"warehouse": item.target_warehouse,
						"project": self.project,
					}
					for item in self.items
				],
			}
		)
		purchase_request.flags.ignore_permissions = True
		purchase_request.insert()
		purchase_request.submit()
		self.db_set("purchase_request", purchase_request.name, update_modified=False)
		purchase_request.add_comment(
			"Info",
			_("Created from approved Purchase Need {0}").format(self.name),
		)

	def _validate_dates(self) -> None:
		if self.request_date and self.required_by:
			if getdate(self.required_by) < getdate(self.request_date):
				frappe.throw(_("Required By cannot be earlier than Request Date."))

	def _validate_project(self) -> None:
		project = frappe.db.get_value("Project", self.project, ["company", "status"], as_dict=True)
		if not project:
			frappe.throw(_("Project {0} does not exist.").format(self.project))
		if project.company and project.company != self.company:
			frappe.throw(_("Project must belong to the selected Company."))
		if project.status in CLOSED_PROJECT_STATES:
			frappe.throw(_("Purchase Needs cannot be created for a closed Project."))

	def _validate_decision_reason(self) -> None:
		if self.workflow_state in DECISION_REASON_STATES and not (self.decision_reason or "").strip():
			frappe.throw(_("Decision Reason is required when a need is returned or rejected."))

	def _validate_items(self) -> None:
		if not self.items:
			frappe.throw(_("Add at least one required item."))

		for item in self.items:
			if flt(item.qty) <= 0:
				frappe.throw(_("Row {0}: Quantity must be greater than zero.").format(item.idx))

			item_values = frappe.db.get_value(
				"Item",
				item.item_code,
				["disabled", "is_stock_item", "stock_uom", "description"],
				as_dict=True,
			)
			if not item_values or item_values.disabled:
				frappe.throw(_("Row {0}: Item is unavailable.").format(item.idx))
			if not item_values.is_stock_item:
				frappe.throw(_("Row {0}: Select a stock item.").format(item.idx))

			warehouse = frappe.db.get_value(
				"Warehouse", item.target_warehouse, ["company", "is_group"], as_dict=True
			)
			if not warehouse or warehouse.is_group:
				frappe.throw(_("Row {0}: Select an active warehouse.").format(item.idx))
			if warehouse.company and warehouse.company != self.company:
				frappe.throw(_("Row {0}: Warehouse must belong to the selected Company.").format(item.idx))

	def _set_item_defaults(self) -> None:
		for item in self.items:
			if not item.item_code:
				continue
			item_values = frappe.db.get_value(
				"Item", item.item_code, ["stock_uom", "description"], as_dict=True
			)
			if not item_values:
				continue
			item.uom = item.uom or item_values.stock_uom
			item.description = item.description or item_values.description
