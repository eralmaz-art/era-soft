from __future__ import annotations

import csv
import json
import pathlib
import plistlib
import re
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]


class RepositoryContractTest(unittest.TestCase):
	def test_frappe_packages_exist_for_every_module(self) -> None:
		modules = (ROOT / "era_soft" / "modules.txt").read_text(encoding="utf-8").splitlines()
		for module in filter(None, modules):
			package = module.lower().replace(" ", "_")
			with self.subTest(module=module):
				self.assertTrue((ROOT / "era_soft" / package / "__init__.py").is_file())

	def test_supported_major_versions_are_bounded(self) -> None:
		config = (ROOT / "pyproject.toml").read_text(encoding="utf-8")
		self.assertIn('frappe = ">=16.0.0,<17.0.0"', config)
		self.assertIn('erpnext = ">=16.0.0,<17.0.0"', config)

	def test_no_erpnext_source_is_vendored(self) -> None:
		self.assertFalse((ROOT / "erpnext").exists())

	def test_only_approved_construction_doctypes_exist(self) -> None:
		doctype_names = {path.parent.name for path in (ROOT / "era_soft").glob("**/doctype/*/*.json")}
		self.assertEqual(
			doctype_names,
			{"era_purchase_need", "era_purchase_need_item"},
		)

	def test_purchase_need_workflow_is_scoped_and_segregated(self) -> None:
		config_path = ROOT / "era_soft" / "era_construction" / "purchase_need_config.json"
		config = json.loads(config_path.read_text(encoding="utf-8"))
		workflow = config["workflow"]

		self.assertEqual(workflow["document_type"], "ERA Purchase Need")
		self.assertNotEqual(workflow["document_type"], "Material Request")
		self.assertEqual(
			{state["state"] for state in workflow["states"]},
			{
				"Draft Need",
				"Pending Approval",
				"Approved Purchase Request",
				"Returned",
				"Rejected",
			},
		)
		approve_transition = next(
			transition for transition in workflow["transitions"] if transition["action"] == "Approve Need"
		)
		self.assertEqual(approve_transition["allowed"], "ERA Construction Approver")
		self.assertEqual(approve_transition["allow_self_approval"], 0)

	def test_release_version_is_consistent(self) -> None:
		package_version = re.search(
			r'__version__ = "([^"]+)"',
			(ROOT / "era_soft" / "__init__.py").read_text(encoding="utf-8"),
		).group(1)
		hooks_version = re.search(
			r'app_version = "([^"]+)"',
			(ROOT / "era_soft" / "hooks.py").read_text(encoding="utf-8"),
		).group(1)
		self.assertEqual(package_version, "0.5.4")
		self.assertEqual(hooks_version, package_version)

	def test_platform_and_construction_navigation_are_separate(self) -> None:
		platform_sidebar_path = ROOT / "era_soft" / "workspace_sidebar" / "era_soft.json"
		platform_sidebar = json.loads(platform_sidebar_path.read_text(encoding="utf-8"))
		self.assertEqual(
			[item["label"] for item in platform_sidebar["items"]],
			[
				"ERA SOFT",
				"Applications",
				"ERA Construction",
				"ERA Concrete",
				"SRIS Bishkek",
				"Platform Services",
				"ERA Finance",
				"ERA HR",
				"ERA Documents",
				"ERA AI",
				"Management",
				"Executive Dashboard",
				"Administration",
			],
		)

		sidebar_path = ROOT / "era_soft" / "workspace_sidebar" / "construction.json"
		sidebar = json.loads(sidebar_path.read_text(encoding="utf-8"))
		self.assertEqual(
			[item["label"] for item in sidebar["items"]],
			[
				"ERA SOFT",
				"Construction Application",
				"Overview",
				"Projects",
				"Budgets",
				"Procurement",
				"Materials",
				"Contractors",
				"Payments",
				"Reports",
			],
		)

	def test_visual_configuration_files_are_valid_json(self) -> None:
		configuration_paths = [
			ROOT / "era_soft" / "desktop_icon" / "era_soft.json",
			ROOT / "era_soft" / "workspace_sidebar" / "construction.json",
			ROOT / "era_soft" / "workspace_sidebar" / "era_soft.json",
			*sorted((ROOT / "era_soft").glob("**/workspace/**/*.json")),
		]
		for path in configuration_paths:
			with self.subTest(path=path):
				json.loads(path.read_text(encoding="utf-8"))

	def test_visual_assets_and_launcher_exist(self) -> None:
		for relative_path in (
			"era_soft/public/images/era-soft-mark.svg",
			"era_soft/public/images/era-soft-logo.svg",
			"era_soft/public/branding/construction.png",
			"era_soft/public/branding/concrete.png",
			"era_soft/public/branding/education.png",
			"era_soft/public/css/era_soft.css",
			"docs/branding/application-branding.md",
			"macos/ERA SOFT.command",
			"macos/ERA SOFT.app/Contents/MacOS/era-soft-launcher",
			"macos/ERA SOFT.app/Contents/Resources/era-soft-launcher.sh",
			"macos/ERA SOFT.app/Contents/Resources/era-soft.icns",
			"scripts/build_macos_app.sh",
			"scripts/install_macos_app.sh",
		):
			with self.subTest(relative_path=relative_path):
				self.assertTrue((ROOT / relative_path).is_file())

		info_path = ROOT / "macos" / "ERA SOFT.app" / "Contents" / "Info.plist"
		with info_path.open("rb") as info_file:
			info = plistlib.load(info_file)
		self.assertEqual(info["CFBundleDisplayName"], "ERA SOFT")
		self.assertEqual(info["CFBundleExecutable"], "era-soft-launcher")

	def test_russian_translation_layer_has_unique_sources(self) -> None:
		translation_path = ROOT / "era_soft" / "translations" / "ru.csv"
		with translation_path.open(encoding="utf-8", newline="") as translation_file:
			rows = list(csv.reader(translation_file))
		sources = [row[0] for row in rows]
		self.assertEqual(len(sources), len(set(sources)))
		self.assertTrue(all(len(row) in {2, 3} for row in rows))

	def test_russian_terminology_matches_approved_terms(self) -> None:
		translation_path = ROOT / "era_soft" / "translations" / "ru.csv"
		with translation_path.open(encoding="utf-8", newline="") as translation_file:
			translations = {row[0]: row[1] for row in csv.reader(translation_file)}

		self.assertEqual(
			{source: translations[source] for source in self.APPROVED_RUSSIAN_TERMS},
			self.APPROVED_RUSSIAN_TERMS,
		)

	def test_every_custom_workspace_label_has_a_russian_translation(self) -> None:
		translation_path = ROOT / "era_soft" / "translations" / "ru.csv"
		with translation_path.open(encoding="utf-8", newline="") as translation_file:
			translated_sources = {row[0] for row in csv.reader(translation_file)}

		visible_sources: set[str] = set()
		for workspace_path in sorted((ROOT / "era_soft").glob("**/workspace/**/*.json")):
			workspace = json.loads(workspace_path.read_text(encoding="utf-8"))
			visible_sources.add(workspace["title"])
			visible_sources.update(link["label"] for link in workspace.get("links", []))
			for block in json.loads(workspace["content"]):
				if card_name := block.get("data", {}).get("card_name"):
					visible_sources.add(card_name)
				if text := block.get("data", {}).get("text"):
					visible_sources.update(
						part.strip() for part in re.split(r"<[^>]+>", text) if part.strip()
					)

		for sidebar_path in sorted((ROOT / "era_soft" / "workspace_sidebar").glob("*.json")):
			sidebar = json.loads(sidebar_path.read_text(encoding="utf-8"))
			visible_sources.update(item["label"] for item in sidebar["items"])
		visible_sources = {
			source
			for source in visible_sources
			if re.search(r"[A-Za-z]", source) and not re.search(r"[А-Яа-яЁё]", source)
		}
		visible_sources.discard("ERA SOFT")

		self.assertEqual(visible_sources - translated_sources, set())

	APPROVED_RUSSIAN_TERMS = {
		"Dashboard": "Главная",
		"Construction": "Строительство",
		"Procurement": "Закупки",
		"Finance": "Финансы",
		"Projects": "Проекты",
		"Suppliers": "Поставщики",
		"Employees": "Сотрудники",
		"Reports": "Отчеты",
		"Settings": "Настройки",
		"Customer": "Клиент",
		"Supplier": "Поставщик",
		"Purchase Order": "Заказ на закупку",
		"Payment Entry": "Оплата",
		"Cost": "Себестоимость",
		"Project": "Объект",
		"Account": "Статья затрат",
	}


if __name__ == "__main__":
	unittest.main()
