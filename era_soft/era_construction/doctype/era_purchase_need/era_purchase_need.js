frappe.ui.form.on("ERA Purchase Need", {
	setup(frm) {
		frm.set_query("project", () => ({
			filters: {
				company: frm.doc.company,
				status: "Open",
			},
		}));

		frm.set_query("target_warehouse", "items", () => ({
			filters: {
				company: frm.doc.company,
				is_group: 0,
			},
		}));

		frm.set_query("item_code", "items", () => ({
			filters: {
				disabled: 0,
				is_stock_item: 1,
			},
		}));
	},

	refresh(frm) {
		if (frm.doc.purchase_request) {
			frm.add_custom_button(__("Open Purchase Request"), () => {
				frappe.set_route("Form", "Material Request", frm.doc.purchase_request);
			});
		}

		const guidance = {
			"Draft Need": __("Describe the business reason and required materials, then submit for approval."),
			"Pending Approval": __("Review the project, reason, date, and quantities before deciding."),
			Returned: __("Review the decision reason, correct the need, and resubmit."),
			Rejected: __("This need was rejected. Revise it only when the business requirement changes."),
			"Approved Purchase Request": __("The approved ERPNext Purchase Request is available from this need."),
		};

		if (guidance[frm.doc.workflow_state]) {
			frm.set_intro(guidance[frm.doc.workflow_state], "blue");
		}
	},

	company(frm) {
		if (frm.doc.project) {
			frm.set_value("project", "");
		}
	},
});
