from __future__ import annotations

import json

import frappe
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields

CONFIG_PATH = frappe.get_app_path("era_soft", "era_construction", "purchase_need_config.json")


def apply_construction_mvp() -> None:
	"""Install the first Construction capability using supported Frappe records."""
	config = _load_config()
	_ensure_roles(config["roles"])
	_ensure_standard_reference_permissions(config)
	_ensure_material_request_source_link()
	_ensure_workflow(config["workflow"])
	frappe.clear_cache()


def ensure_construction_roles() -> None:
	"""Create roles before DocType permissions are synchronized during migrate."""
	_ensure_roles(_load_config()["roles"])


def _load_config() -> dict:
	with open(CONFIG_PATH, encoding="utf-8") as config_file:
		return json.load(config_file)


def _ensure_roles(roles: list[str]) -> None:
	for role_name in roles:
		if frappe.db.exists("Role", role_name):
			continue
		frappe.get_doc(
			{
				"doctype": "Role",
				"role_name": role_name,
				"desk_access": 1,
				"is_custom": 1,
			}
		).insert(ignore_permissions=True)


def _ensure_standard_reference_permissions(config: dict) -> None:
	for doctype in config["standard_read_permissions"]:
		for role_name in config["roles"]:
			filters = {"parent": doctype, "role": role_name, "permlevel": 0}
			name = frappe.db.exists("Custom DocPerm", filters)
			values = {
				"read": 1,
				"select": 1,
				"report": int(doctype in {"Project", "Material Request"}),
				"export": 0,
			}
			if name:
				permission = frappe.get_doc("Custom DocPerm", name)
				permission.update(values)
				permission.save(ignore_permissions=True)
			else:
				frappe.get_doc(
					{
						"doctype": "Custom DocPerm",
						**filters,
						**values,
					}
				).insert(ignore_permissions=True)


def _ensure_material_request_source_link() -> None:
	create_custom_fields(
		{
			"Material Request": [
				{
					"fieldname": "custom_era_purchase_need",
					"label": "Purchase Need",
					"fieldtype": "Link",
					"options": "ERA Purchase Need",
					"insert_after": "amended_from",
					"read_only": 1,
					"no_copy": 1,
					"in_standard_filter": 1,
					"search_index": 1,
					"unique": 1,
				}
			]
		},
		update=True,
	)


def _ensure_workflow(workflow_config: dict) -> None:
	for state in workflow_config["states"]:
		_upsert_named_document(
			"Workflow State",
			state["state"],
			{"workflow_state_name": state["state"], "style": state["style"]},
		)

	for transition in workflow_config["transitions"]:
		_upsert_named_document(
			"Workflow Action Master",
			transition["action"],
			{"workflow_action_name": transition["action"]},
		)

	workflow_values = {
		"workflow_name": workflow_config["name"],
		"document_type": workflow_config["document_type"],
		"is_active": 1,
		"override_status": 0,
		"send_email_alert": 0,
		"enable_action_confirmation": 1,
		"workflow_state_field": workflow_config["workflow_state_field"],
		"states": [
			{
				"state": state["state"],
				"doc_status": state["doc_status"],
				"allow_edit": state["allow_edit"],
				"send_email": 0,
			}
			for state in workflow_config["states"]
		],
		"transitions": workflow_config["transitions"],
	}

	if frappe.db.exists("Workflow", workflow_config["name"]):
		workflow = frappe.get_doc("Workflow", workflow_config["name"])
		workflow.update(workflow_values)
		workflow.save(ignore_permissions=True)
	else:
		frappe.get_doc({"doctype": "Workflow", **workflow_values}).insert(ignore_permissions=True)


def _upsert_named_document(doctype: str, name: str, values: dict) -> None:
	if frappe.db.exists(doctype, name):
		document = frappe.get_doc(doctype, name)
		document.update(values)
		document.save(ignore_permissions=True)
	else:
		frappe.get_doc({"doctype": doctype, **values}).insert(ignore_permissions=True)
