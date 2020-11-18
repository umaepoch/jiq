frappe.ui.form.on("Internal Concession", "reference_name", function(frm, cdt, cdn) {

    var d = locals[cdt][cdn];
    var reference_type = d.reference_type;
    console.log("reference_type", reference_type);
    var work_order = d.reference_name;
    console.log("work_order", work_order);
    if (reference_type == "Work Order") {
        var item_serial_no = d.item_serial_no;
        console.log("item_serial_no", item_serial_no);
        var get_serial_no = [];
        get_serial_no = get_item_serial_list(work_order);
        console.log("get_serial_no------------", get_serial_no);

        //cur_frm.set_value("serial_no", get_serial_no.toString());
        cur_frm.set_query('item_serial_no', function() {
            var get_serial_no = [];
            get_serial_no = get_item_serial_list(work_order);
            console.log("get_serial_no------------", get_serial_no);
            return {
                "filters": [
                    ['Serial No', 'name', 'in', get_serial_no]
                ]
            }
        });

        cur_frm.set_query('item_code', function() {
            var item_name = fetch_item_name(work_order);
            console.log("item_name------------", item_name);
            return {
                "filters": [
                    ['Item', 'name', '=', item_name]
                ]
            }
        });
    }
})

frappe.ui.form.on("Internal Concession", "refresh", function(frm, cdt, cdn) {

    var d = locals[cdt][cdn];
    var reference_type = d.reference_type;
    console.log("reference_type", reference_type);
    var work_order = d.reference_name;
    console.log("work_order", work_order);
    if (reference_type == "Work Order") {
        var item_serial_no = d.item_serial_no;
        console.log("item_serial_no", item_serial_no);
        var get_serial_no = [];
        get_serial_no = get_item_serial_list(work_order);
        console.log("get_serial_no------------", get_serial_no);

        //cur_frm.set_value("serial_no", get_serial_no.toString());
        cur_frm.set_query('item_serial_no', function() {
            var get_serial_no = [];
            get_serial_no = get_item_serial_list(work_order);
            console.log("get_serial_no------------", get_serial_no);
            return {
                "filters": [
                    ['Serial No', 'name', 'in', get_serial_no]
                ]
            }
        });

        cur_frm.set_query('item_code', function() {
            var item_name = fetch_item_name(work_order);
            console.log("item_name------------", item_name);
            return {
                "filters": [
                    ['Item', 'name', '=', item_name]
                ]
            }
        });
    }
})

function get_item_serial_list(work_order) {
    var item_serial_list = [];
    frappe.call({
        method: 'jiq.api.serial_no',
        args: {
            "work_order": work_order
        },
        async: false,
        callback: function(r) {

            for (var i = 0; i < r.message.length; i++) {

                item_serial_list.push(r.message[i].serial_no);

                console.log("item_serial_list", item_serial_list);

            }

        }

    });

    return item_serial_list
}

function get_serial_list(work_order) {
    var serial_list = [];
    frappe.call({
        method: 'jiq.api.serial_no_list',
        args: {
            "work_order": work_order
        },
        async: false,
        callback: function(r) {

            if (r.message) {
                serial_list = JSON.stringify(r.message);

                console.log("readings-----------" + JSON.stringify(r.message));


            }
            /*for (var i = 0; i < r.message.length; i++) {
				    
				    serial_list.push(r.message[i]);
				   
				    console.log("serial_list",serial_list);
				    
				}*/

        }

    });

    return serial_list
}



function fetch_item_name(work_order) {
    console.log("entered into has_batch_no function");
    var item_name = "";
    frappe.call({
        method: 'frappe.client.get_value',
        args: {
            'doctype': "Work Order",
            'fieldname': "item_name",

            'filters': {
                name: work_order,
            }
        },
        async: false,
        callback: function(r) {
            if (r.message) {
                item_name = r.message.item_name;
                console.log(item_name);
                console.log("readings-----------" + JSON.stringify(r.message));

            }
        }
    });
    return item_name
}
var array = [];
var text = [];

function onlyUnique(value, index, self) {
    return self.indexOf(value) === index;
}
frappe.ui.form.on("Internal Concession", "item_serial_no", function(frm, cdt, cdn) {

    var d = locals[cdt][cdn];
    var reference_type = d.reference_type;
    console.log("reference_type", reference_type);
    var work_order = d.reference_name;
    console.log("work_order", work_order);

    if (reference_type == "Work Order") {
        var item_serial_no = d.item_serial_no;
        console.log("item_serial_no", item_serial_no);


        array.push(item_serial_no);
        console.log("array", array);
        var unique = array.filter(onlyUnique);
        console.log("unique", unique);
        var filtered = unique.filter(x => x !== undefined);
        console.log("filtered", filtered);

        /*var text=[];
        var projects =[ "BUNDLE-000001", "BUNDLE-000002" ];
        for (var i = 1; i < projects.length; i++) {
            text +=  projects[i];
        } */
        //cur_frm.set_value('serial_no', some_array);
        cur_frm.set_value("serial_no", filtered.toString());
        frm.refresh_field("item_serial_no");
        var serial_no = d.serial_no;
        console.log("serial_no", serial_no);
        //cur_frm.refresh_field("item_serial_no");
    }
});
