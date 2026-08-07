from __future__ import annotations

import frappe
from frappe.translate import get_all_translations
from frappe.tests import IntegrationTestCase

from era_soft.setup.localization import apply_russian_localization


class TestInstallation(IntegrationTestCase):
	def test_required_apps_are_installed(self) -> None:
		installed_apps = frappe.get_installed_apps()
		self.assertIn("erpnext", installed_apps)
		self.assertIn("era_soft", installed_apps)

	def test_domain_modules_are_registered(self) -> None:
		modules = set(frappe.get_all("Module Def", filters={"app_name": "era_soft"}, pluck="name"))
		self.assertEqual(
			modules,
			{
				"ERA Soft",
				"ERA Concrete",
				"ERA Construction",
				"ERA Finance",
				"Executive Dashboard",
			},
		)

	def test_visual_baseline_is_installed(self) -> None:
		self.assertEqual(frappe.db.get_single_value("Website Settings", "app_name"), "ERA SOFT")
		self.assertEqual(frappe.db.get_single_value("System Settings", "default_app"), "era_soft")
		self.assertEqual(frappe.db.get_value("Desktop Icon", "ERPNext", "hidden"), 0)
		for icon_name in ("Organization", "Accounting", "Subcontracting", "ERPNext Settings"):
			with self.subTest(icon_name=icon_name):
				self.assertEqual(
					frappe.db.get_value("Desktop Icon", icon_name, "parent_icon"),
					"ERPNext",
				)
		self.assertEqual(
			set(
				frappe.get_all(
					"Workspace",
					filters={"app": "era_soft"},
					pluck="name",
				)
			),
			{"Dashboard", "Construction", "Procurement", "Finance", "Reports", "Settings"},
		)

	def test_russian_localization_baseline_is_installed(self) -> None:
		# Frappe's test runner temporarily selects English while preparing a run.
		# Reapply the idempotent installation hook before asserting the site baseline.
		apply_russian_localization()
		self.assertEqual(frappe.db.get_single_value("System Settings", "language"), "ru")
		self.assertEqual(frappe.db.get_value("User", "Administrator", "language"), "ru")

		translations = get_all_translations("ru")
		self.assertEqual(translations["Dashboard"], "Главная")
		self.assertEqual(translations["Material Request"], "Заявка на закупку")
		self.assertEqual(translations["Purchase Order"], "Заказ на закупку")
		self.assertEqual(translations["Purchase Invoice"], "Счет поставщика")
		self.assertEqual(translations["Payment Entry"], "Оплата")
		self.assertEqual(translations["Project"], "Объект")
