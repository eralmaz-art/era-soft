frappe.ui.form.on("Project", {
	refresh(frm) {
		if (frm.is_new() || frm.doc.status !== "Open") {
			return;
		}

		frm.add_custom_button(
			__("Create Purchase Need"),
			() => {
				frappe.new_doc("ERA Purchase Need", {
					company: frm.doc.company,
					project: frm.doc.name,
					title: __("Purchase need for {0}", [frm.doc.project_name || frm.doc.name]),
				});
			},
			__("Create")
		);
	},
});
