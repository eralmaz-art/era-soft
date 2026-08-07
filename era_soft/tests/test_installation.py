from __future__ import annotations

import frappe
from frappe.tests import IntegrationTestCase


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
