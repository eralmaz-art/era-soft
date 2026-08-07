from __future__ import annotations

import pathlib
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


if __name__ == "__main__":
	unittest.main()
