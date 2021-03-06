// Copyright (c) 2019, Frappé and contributors
// For license information, please see license.txt

frappe.ui.form.on('Pressure Test Requirements', {
	refresh: function(frm) {

	}
});

frappe.ui.form.on("Pressure Test Requirements", "reports_based_on", function(frm, cdt, cdn) {
    console.log("Pressure Test Print Format...");
    var d = locals[cdt][cdn];
    var reports_based_on = d.reports_based_on;
    if (reports_based_on == "Different Readings") {
        cur_frm.set_df_property("number_of_readings_to_be_considered", "hidden", false);
        refresh_field("number_of_readings_to_be_considered");
    } else if (reports_based_on == "Separate Reports") {
        cur_frm.set_df_property("number_of_readings_to_be_considered", "hidden", true);
        refresh_field("number_of_readings_to_be_considered");
    }
});

frappe.ui.form.on("Quality Inspection Reading Configuration", {
    reading_type: function(frm, cdt, cdn) {
        var row = locals[cdt][cdn];
        console.log("reading_type::" + row.reading_type);
        if (row.reading_type == "Text") {
            var dialog = new frappe.ui.Dialog({
                title: __("Select Reporting Value"),
                fields: [{
                    "fieldtype": "Select",
                    "label": __("Reporting Value"),
                    "fieldname": "reporting_value",
		    "reqd": 1,
                    "options": ['Report Acceptance Criteria', 'Reading1']
                }],
                primary_action: function() {
                    dialog.hide();
		   var readings = dialog.get_values();
		   var reporting_value = readings.reporting_value;
            	   row.report_value = reporting_value;
		   refresh_field("report_value");
        	   refresh_field("readings");
                }
            }); //end of dialog box...
            dialog.show();

        }else if (row.reading_type == "Float"){
		var dialog = new frappe.ui.Dialog({
                title: __("Select Reporting Value"),
                fields: [{
                    "fieldtype": "Select",
                    "label": __("Reporting Value"),
                    "fieldname": "reporting_value",
		    "reqd": 1,
                    "options": ['Max', 'Min', 'Avg']
                }],
                primary_action: function() {
                    dialog.hide();
		   var readings = dialog.get_values();
		   var reporting_value = readings.reporting_value;
            	   row.report_value = reporting_value;
		   refresh_field("report_value");
        	   refresh_field("readings");
                }
            }); //end of dialog box...
            dialog.show();
	}

    }//end of reading type
});

frappe.ui.form.on("Pressure Test Requirements", "quality_inspection_template", function(frm, cdt, cdn) {
    var cocpf_id = cur_frm.doc.quality_inspection_template;
    //var readings = fetch_cocpf_readings(cocpf_id);
    frappe.call({
        method: "jiq.jiq.doctype.pressure_test_requirements.pressure_test_requirements.fetch_quality_inspection_readings",
        args: {
            "name": cocpf_id
        },
        async: false,
        callback: function(r) {
            if (r.message) {
                console.log("readings------------::" + JSON.stringify(r.message));
		cur_frm.clear_table("readings");
		var readings = r.message;
		for (var i=0;i<readings.length;i++){
			console.log("specification------------::" + readings[i]['specification']);
			var child = cur_frm.add_child("readings");
			frappe.model.set_value(child.doctype, child.name, "specification", readings[i]['specification']);
		}//end of for loop...
		 refresh_field("readings");
            }
        } //end of callback fun..
    }) //end of frappe call..
});
