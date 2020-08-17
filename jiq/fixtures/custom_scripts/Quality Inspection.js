frappe.ui.form.on("Quality Inspection", {
    refresh: function(frm, cdt, cdn) {
        var d = locals[cdt][cdn];
        console.log("items.....", +JSON.stringify(d));
        var reference_type = d.reference_type;
        console.log("reference_type.....", reference_type);
	
        if(reference_type=="Work Order"){
	
	var parent = d.reference_name;
        console.log("parent.....", parent);
	var item_codes = fetch_item_of_work_order(parent);
        console.log("item_codes", item_codes);

	}   
}
});

function fetch_item_of_work_order(parent) {
    console.log("entered into function");
    var item_code = [];
    frappe.call({
        method: "jiq.api.item_query_quality_inspection",
        args: {
            "parent": parent
        },
        async: false,
        callback: function(r) {
            if (r.message) {

                for (var i = 0; i < r.message.length; i++) {
                    item_code.push(r.message[i].item_code);
                 console.log("readings-----------" + JSON.stringify(r.message));
                }

            }
        }
    });
    return item_code
}


