//onload this frappe call will execute.It will get all data from database
var details;
var item_code = [];
var serial_no = [];
var sales_order = [];

console.log("before call", details);
frappe.call({

    method: "jiq.www.CertificationDocuments.api_user",

    async: false,
    callback: function(r) {

        details = r.message;
        console.log("inside", details);

        var all_data = details;

        var tableBody = '<table width="100%" cellpadding="3" align="center" style="border-collapse:collapse;border-color: lightgray;" border="1"><tr style="font-weight:bold;text-align:center;background-color: #8c8a8a;"><td style="color:white;">Item Name</td><td style="color:white;">Item Serial No</td><td style="color:white;">COC</td><td style="color:white;">Pressure Test</td><td style="color:white;">Build Sheet</td><td style="color:white;">DNV-GL Product Certificate</td><td style="color:white;">EU Declaration of Conformity</td><td style="color:white;">Docpack</td><td style="color:white;">Customer PO</td><td style="color:white;">Delivery Note</td><td style="color:white;">Delivery Note Date</td></tr>';

        all_data.forEach(function(d) {
            tableBody += '<tr><td style="text-align:left;border-color: lightgray;">' + d.item_name + '</td><td style="text-align:left;border-color: lightgray;">' + d.serial_no + '</td>if (d.pch1_coc !== "null") {<td style="text-align:center;border-color: lightgray;">' + d.pch1_coc + '</td> } else {<td style="text-align:center;border-color: lightgray;">' + "tbu" + '</td>}if (d.pch1_pressure_test !== "null") {<td style="text-align:center;border-color: lightgray;">' + d.pch1_pressure_test + '</td>} else { <td style="text-align:center;border-color: lightgray;">' + "tbu" + '</td>}if (d.pch1_build_sheet !== "null") { <td style="text-align:center;border-color: lightgray;">' + d.pch1_build_sheet + '</td> } else {   <td style="text-align:center;border-color: lightgray;">' + "tbu" + '</td>}<td style="text-align:center;border-color: lightgray;">' + d.pch1_dnv_gl_product_certificate + '</td><td style="text-align:center;border-color: lightgray;">' + d.pch1_eu_declaration_of_conformity + '</td><td style="text-align:center;border-color: lightgray;">' + d.pch1_combined_pdf + '</td><td style="text-align:center;border-color: lightgray;">' + d.po_no + '</td><td style="text-align:left;border-color: lightgray;">' + d.delivery_document_no + '</td><td style="text-align:center;border-color: lightgray;">' + d.delivery_date + '</td></tr>';
});
        tableBody += '<table>';

        // FINALLY ADD THE NEWLY CREATED TABLE WITH JSON DATA TO A CONTAINER.

        var divContainer = document.getElementById("showData");
        divContainer.innerHTML = tableBody;
    }


});




function ShowValue(btn) {
    var filter_value = [];

    var po_no = document.getElementById('customer_po').value;

    console.log("po_no", po_no);

    var delivery_document_no = document.getElementById('delivery_note').value;
    console.log("delivery_document_no", delivery_document_no);

    var serial_no = document.getElementById('item_serial_no').value;
    console.log("serial_no", serial_no);

    if (po_no !== "" && delivery_document_no === "" && serial_no === "") {

        get_po_no(po_no);
    } else if (serial_no !== "" && po_no === "" && delivery_document_no === "") {

        get_serial_no(serial_no);
    } else if (delivery_document_no !== "" && po_no === "" && serial_no === "") {

        get_delivery_document_no(delivery_document_no);
    } else if (serial_no !== "" && delivery_document_no !== "" && po_no === "") {
        console.log("entered  po_no not entered  block");

        get_value_of_data(delivery_document_no, serial_no);
    } else if (serial_no !== "" && delivery_document_no === "" && po_no !== "") {
        console.log("entered  delivery_document_no not entered  block");

        get_value_of_po_serial(po_no, serial_no);
    } else if (serial_no === "" && delivery_document_no !== "" && po_no !== "") {
        console.log("entered  in serial no not applied  block");

        get_value_of_po_delivery(po_no, delivery_document_no);
    } else if (serial_no !== "" && delivery_document_no !== "" && po_no !== "") {
        console.log("entered  all filters applied block");

        get_value_of_all_filters(po_no, delivery_document_no, serial_no);
    }

}



function ResetAll(btn) {



    document.getElementById('customer_po').value = '';
    document.getElementById('delivery_note').value = '';
    document.getElementById('item_serial_no').value = '';
    get_all();
}


function get_value_of_data(delivery_document_no, serial_no) {
    console.log("enetered in function block");
    var details;
    frappe.call({

        method: "jiq.www.CertificationDocuments.delivery_serial",
        args: {
            "delivery_document_no": delivery_document_no,
            "serial_no": serial_no
        },
        async: false,
        callback: function(r) {

            details = r.message;
            console.log("details", details);

            var all_data = details;

            console.log("get_value_of_data", details);
            if (all_data == "") {

                frappe.msgprint("Nothing to Display - Please change filters and try again");
            } else {

                var tableBody = '<table width="100%" cellpadding="3" align="center" style="border-collapse:collapse;border-color: lightgray;" border="1"><tr style="font-weight:bold;text-align:center;background-color: #8c8a8a;"><td style="color:white;">Item Name</td><td style="color:white;">Item Serial No</td><td style="color:white;">COC</td><td style="color:white;">Pressure Test</td><td style="color:white;">Build Sheet</td><td style="color:white;">DNV-GL Product Certificate</td><td style="color:white;">EU Declaration of Conformity</td><td style="color:white;">Docpack</td><td style="color:white;">Customer PO</td><td style="color:white;">Delivery Note</td><td style="color:white;">Delivery Note Date</td></tr>';

                all_data.forEach(function(d) {
                    tableBody += '<tr><td style="text-align:left;border-color: lightgray;">' + d.item_name + '</td><td style="text-align:left;border-color: lightgray;">' + d.serial_no + '</td><td style="text-align:center;border-color: lightgray;">' + d.pch1_coc + '</td><td style="text-align:center;border-color: lightgray;">' + d.pch1_pressure_test + '</td><td style="text-align:center;border-color: lightgray;">' + d.pch1_build_sheet + '</td><td style="text-align:center;border-color: lightgray;">' + d.pch1_dnv_gl_product_certificate + '</td><td style="text-align:center;border-color: lightgray;">' + d.pch1_eu_declaration_of_conformity + '</td><td style="text-align:center;border-color: lightgray;">' + d.pch1_combined_pdf + '</td><td style="text-align:center;border-color: lightgray;">' + d.po_no + '</td><td style="text-align:left;border-color: lightgray;">' + d.delivery_document_no + '</td><td style="text-align:center;border-color: lightgray;">' + d.delivery_date + '</td></tr>';
                });
                tableBody += '<table>';

                // FINALLY ADD THE NEWLY CREATED TABLE WITH JSON DATA TO A CONTAINER.

                var divContainer = document.getElementById("showData");
                divContainer.innerHTML = tableBody;
            }
        }

    });
}

//po_no and delivery note

function get_value_of_po_delivery(po_no, delivery_document_no) {
    console.log("enetered in function block");
    var details;
    frappe.call({

        method: "jiq.www.CertificationDocuments.po_delivery",
        args: {
            "delivery_document_no": delivery_document_no,
            "po_no": po_no
        },
        async: false,
        callback: function(r) {

            details = r.message;
            console.log("details", details);

            var all_data = details;

            console.log("get_value_of_data", details);
            if (all_data == "") {

                frappe.msgprint("Nothing to Display - Please change filters and try again");
            } else {

                var tableBody = '<table width="100%" cellpadding="3" align="center" style="border-collapse:collapse;border-color: lightgray;" border="1"><tr style="font-weight:bold;text-align:center;background-color: #8c8a8a;"><td style="color:white;">Item Name</td><td style="color:white;">Item Serial No</td><td style="color:white;">COC</td><td style="color:white;">Pressure Test</td><td style="color:white;">Build Sheet</td><td style="color:white;">DNV-GL Product Certificate</td><td style="color:white;">EU Declaration of Conformity</td><td style="color:white;">Docpack</td><td style="color:white;">Customer PO</td><td style="color:white;">Delivery Note</td><td style="color:white;">Delivery Note Date</td></tr>';

                all_data.forEach(function(d) {
                    tableBody += '<tr><td style="text-align:left;border-color: lightgray;">' + d.item_name + '</td><td style="text-align:left;border-color: lightgray;">' + d.serial_no + '</td><td style="text-align:center;border-color: lightgray;">' + d.pch1_coc + '</td><td style="text-align:center;border-color: lightgray;">' + d.pch1_pressure_test + '</td><td style="text-align:center;border-color: lightgray;">' + d.pch1_build_sheet + '</td><td style="text-align:center;border-color: lightgray;">' + d.pch1_dnv_gl_product_certificate + '</td><td style="text-align:center;border-color: lightgray;">' + d.pch1_eu_declaration_of_conformity + '</td><td style="text-align:center;border-color: lightgray;">' + d.pch1_combined_pdf + '</td><td style="text-align:center;border-color: lightgray;">' + d.po_no + '</td><td style="text-align:left;border-color: lightgray;">' + d.delivery_document_no + '</td><td style="text-align:center;border-color: lightgray;">' + d.delivery_date + '</td></tr>';
                });
                tableBody += '<table>';

                // FINALLY ADD THE NEWLY CREATED TABLE WITH JSON DATA TO A CONTAINER.

                var divContainer = document.getElementById("showData");
                divContainer.innerHTML = tableBody;
            }
        }

    });
}

//po_serial applied

function get_value_of_po_serial(po_no, serial_no) {
    console.log("enetered in function block");
    var details;
    frappe.call({

        method: "jiq.www.CertificationDocuments.po_serial",
        args: {
            "serial_no": serial_no,
            "po_no": po_no
        },
        async: false,
        callback: function(r) {

            details = r.message;
            console.log("details", details);

            var all_data = details;

            console.log("get_value_of_data", details);
            if (all_data == "") {

                frappe.msgprint("Nothing to Display - Please change filters and try again");
            } else {

                var tableBody = '<table width="100%" cellpadding="3" align="center" style="border-collapse:collapse;border-color: lightgray;" border="1"><tr style="font-weight:bold;text-align:center;background-color: #8c8a8a;"><td style="color:white;">Item Name</td><td style="color:white;">Item Serial No</td><td style="color:white;">COC</td><td style="color:white;">Pressure Test</td><td style="color:white;">Build Sheet</td><td style="color:white;">DNV-GL Product Certificate</td><td style="color:white;">EU Declaration of Conformity</td><td style="color:white;">Docpack</td><td style="color:white;">Customer PO</td><td style="color:white;">Delivery Note</td><td style="color:white;">Delivery Note Date</td></tr>';

                all_data.forEach(function(d) {
                    tableBody += '<tr><td style="text-align:left;border-color: lightgray;">' + d.item_name + '</td><td style="text-align:left;border-color: lightgray;">' + d.serial_no + '</td><td style="text-align:center;border-color: lightgray;">' + d.pch1_coc + '</td><td style="text-align:center;border-color: lightgray;">' + d.pch1_pressure_test + '</td><td style="text-align:center;border-color: lightgray;">' + d.pch1_build_sheet + '</td><td style="text-align:center;border-color: lightgray;">' + d.pch1_dnv_gl_product_certificate + '</td><td style="text-align:center;border-color: lightgray;">' + d.pch1_eu_declaration_of_conformity + '</td><td style="text-align:center;border-color: lightgray;">' + d.pch1_combined_pdf + '</td><td style="text-align:center;border-color: lightgray;">' + d.po_no + '</td><td style="text-align:left;border-color: lightgray;">' + d.delivery_document_no + '</td><td style="text-align:center;border-color: lightgray;">' + d.delivery_date + '</td></tr>';
                });
                tableBody += '<table>';

                // FINALLY ADD THE NEWLY CREATED TABLE WITH JSON DATA TO A CONTAINER.

                var divContainer = document.getElementById("showData");
                divContainer.innerHTML = tableBody;
            }
        }

    });
}

//all filters applied

function get_value_of_all_filters(po_no, delivery_document_no, serial_no) {
    console.log("enetered in function block");
    var details;
    frappe.call({

        method: "jiq.www.CertificationDocuments.all_filters_applied",
        args: {
            "po_no": po_no,
            "delivery_document_no": delivery_document_no,
            "serial_no": serial_no
        },
        async: false,
        callback: function(r) {

            details = r.message;
            console.log("details", details);

            var all_data = details;

            console.log("get_value_of_data", details);
            if (all_data == "") {

                frappe.msgprint("Nothing to Display - Please change filters and try again");
            } else {

                var tableBody = '<table width="100%" cellpadding="3" align="center" style="border-collapse:collapse;border-color: lightgray;" border="1"><tr style="font-weight:bold;text-align:center;background-color: #8c8a8a;"><td style="color:white;">Item Name</td><td style="color:white;">Item Serial No</td><td style="color:white;">COC</td><td style="color:white;">Pressure Test</td><td style="color:white;">Build Sheet</td><td style="color:white;">DNV-GL Product Certificate</td><td style="color:white;">EU Declaration of Conformity</td><td style="color:white;">Docpack</td><td style="color:white;">Customer PO</td><td style="color:white;">Delivery Note</td><td style="color:white;">Delivery Note Date</td></tr>';

                all_data.forEach(function(d) {
                    tableBody += '<tr><td style="text-align:left;border-color: lightgray;">' + d.item_name + '</td><td style="text-align:left;border-color: lightgray;">' + d.serial_no + '</td><td style="text-align:center;border-color: lightgray;">' + d.pch1_coc + '</td><td style="text-align:center;border-color: lightgray;">' + d.pch1_pressure_test + '</td><td style="text-align:center;border-color: lightgray;">' + d.pch1_build_sheet + '</td><td style="text-align:center;border-color: lightgray;">' + d.pch1_dnv_gl_product_certificate + '</td><td style="text-align:center;border-color: lightgray;">' + d.pch1_eu_declaration_of_conformity + '</td><td style="text-align:center;border-color: lightgray;">' + d.pch1_combined_pdf + '</td><td style="text-align:center;border-color: lightgray;">' + d.po_no + '</td><td style="text-align:left;border-color: lightgray;">' + d.delivery_document_no + '</td><td style="text-align:center;border-color: lightgray;">' + d.delivery_date + '</td></tr>';
                });
                tableBody += '<table>';
                // FINALLY ADD THE NEWLY CREATED TABLE WITH JSON DATA TO A CONTAINER.

                var divContainer = document.getElementById("showData");
                divContainer.innerHTML = tableBody;
            }
        }

    });
}




//this function get all data when nothing is selected in filters
function get_all() {
    frappe.call({

        method: "jiq.www.CertificationDocuments.api_user",

        async: false,
        callback: function(r) {

            details = r.message;
            console.log("inside", details);
            var all_data = details;
            console.log("all_data", all_data);
            if (all_data == "") {

                frappe.msgprint("Nothing to Display - Please change filters and try again");
            } else {

                var tableBody = '<table width="100%" cellpadding="3" align="center" style="border-collapse:collapse;border-color: lightgray;" border="1"><tr style="font-weight:bold;text-align:center;background-color: #8c8a8a;"><td style="color:white;">Item Name</td><td style="color:white;">Item Serial No</td><td style="color:white;">COC</td><td style="color:white;">Pressure Test</td><td style="color:white;">Build Sheet</td><td style="color:white;">DNV-GL Product Certificate</td><td style="color:white;">EU Declaration of Conformity</td><td style="color:white;">Docpack</td><td style="color:white;">Customer PO</td><td style="color:white;">Delivery Note</td><td style="color:white;">Delivery Note Date</td></tr>';

                all_data.forEach(function(d) {
                    tableBody += '<tr><td style="text-align:left;border-color: lightgray;">' + d.item_name + '</td><td style="text-align:left;border-color: lightgray;">' + d.serial_no + '</td><td style="text-align:center;border-color: lightgray;">' + d.pch1_coc + '</td><td style="text-align:center;border-color: lightgray;">' + d.pch1_pressure_test + '</td><td style="text-align:center;border-color: lightgray;">' + d.pch1_build_sheet + '</td><td style="text-align:center;border-color: lightgray;">' + d.pch1_dnv_gl_product_certificate + '</td><td style="text-align:center;border-color: lightgray;">' + d.pch1_eu_declaration_of_conformity + '</td><td style="text-align:center;border-color: lightgray;">' + d.pch1_combined_pdf + '</td><td style="text-align:center;border-color: lightgray;">' + d.po_no + '</td><td style="text-align:left;border-color: lightgray;">' + d.delivery_document_no + '</td><td style="text-align:center;border-color: lightgray;">' + d.delivery_date + '</td></tr>';
                });
                tableBody += '<table>';
                // FINALLY ADD THE NEWLY CREATED TABLE WITH JSON DATA TO A CONTAINER.

                var divContainer = document.getElementById("showData");
                divContainer.innerHTML = tableBody;
            }
        }

    });

}

//to get po
function get_po_no(po_no) {
    console.log("enetered in function block");
    var details;
    frappe.call({

        method: "jiq.www.CertificationDocuments.po_no",
        args: {
            "po_no": po_no
        },
        async: false,
        callback: function(r) {

            details = r.message;
            console.log("details", details);

            var all_data = details;
            console.log("get_po_no", details);
            if (all_data == "") {

                frappe.msgprint("Nothing to Display - Please change filters and try again");
            } else {

                var tableBody = '<table width="100%" cellpadding="3" align="center" style="border-collapse:collapse;border-color: lightgray;" border="1"><tr style="font-weight:bold;text-align:center;background-color: #8c8a8a;"><td style="color:white;">Item Name</td><td style="color:white;">Item Serial No</td><td style="color:white;">COC</td><td style="color:white;">Pressure Test</td><td style="color:white;">Build Sheet</td><td style="color:white;">DNV-GL Product Certificate</td><td style="color:white;">EU Declaration of Conformity</td><td style="color:white;">Docpack</td><td style="color:white;">Customer PO</td><td style="color:white;">Delivery Note</td><td style="color:white;">Delivery Note Date</td></tr>';

                all_data.forEach(function(d) {
                    tableBody += '<tr><td style="text-align:left;border-color: lightgray;">' + d.item_name + '</td><td style="text-align:left;border-color: lightgray;">' + d.serial_no + '</td><td style="text-align:center;border-color: lightgray;">' + d.pch1_coc + '</td><td style="text-align:center;border-color: lightgray;">' + d.pch1_pressure_test + '</td><td style="text-align:center;border-color: lightgray;">' + d.pch1_build_sheet + '</td><td style="text-align:center;border-color: lightgray;">' + d.pch1_dnv_gl_product_certificate + '</td><td style="text-align:center;border-color: lightgray;">' + d.pch1_eu_declaration_of_conformity + '</td><td style="text-align:center;border-color: lightgray;">' + d.pch1_combined_pdf + '</td><td style="text-align:center;border-color: lightgray;">' + d.po_no + '</td><td style="text-align:left;border-color: lightgray;">' + d.delivery_document_no + '</td><td style="text-align:center;border-color: lightgray;">' + d.delivery_date + '</td></tr>';
                });
                tableBody += '<table>';

                // FINALLY ADD THE NEWLY CREATED TABLE WITH JSON DATA TO A CONTAINER.

                var divContainer = document.getElementById("showData");
                divContainer.innerHTML = tableBody;
            }
        }
    });
}

//get delivery document no
function get_delivery_document_no(delivery_document_no) {
    console.log("enetered in function block");
    var details;
    frappe.call({

        method: "jiq.www.CertificationDocuments.delivery_document_no",
        args: {
            "delivery_document_no": delivery_document_no
        },
        async: false,
        callback: function(r) {

            details = r.message;
            console.log("details", details);

            var all_data = details;

            console.log("get_delivery_document_no", details);
            if (all_data == "") {

                frappe.msgprint("Nothing to Display - Please change filters and try again");
            } else {

                var tableBody = '<table width="100%" cellpadding="3" align="center" style="border-collapse:collapse;border-color: lightgray;" border="1"><tr style="font-weight:bold;text-align:center;background-color: #8c8a8a;"><td style="color:white;">Item Name</td><td style="color:white;">Item Serial No</td><td style="color:white;">COC</td><td style="color:white;">Pressure Test</td><td style="color:white;">Build Sheet</td><td style="color:white;">DNV-GL Product Certificate</td><td style="color:white;">EU Declaration of Conformity</td><td style="color:white;">Docpack</td><td style="color:white;">Customer PO</td><td style="color:white;">Delivery Note</td><td style="color:white;">Delivery Note Date</td></tr>';

                all_data.forEach(function(d) {
                    tableBody += '<tr><td style="text-align:left;border-color: lightgray;">' + d.item_name + '</td><td style="text-align:left;border-color: lightgray;">' + d.serial_no + '</td><td style="text-align:center;border-color: lightgray;">' + d.pch1_coc + '</td><td style="text-align:center;border-color: lightgray;">' + d.pch1_pressure_test + '</td><td style="text-align:center;border-color: lightgray;">' + d.pch1_build_sheet + '</td><td style="text-align:center;border-color: lightgray;">' + d.pch1_dnv_gl_product_certificate + '</td><td style="text-align:center;border-color: lightgray;">' + d.pch1_eu_declaration_of_conformity + '</td><td style="text-align:center;border-color: lightgray;">' + d.pch1_combined_pdf + '</td><td style="text-align:center;border-color: lightgray;">' + d.po_no + '</td><td style="text-align:left;border-color: lightgray;">' + d.delivery_document_no + '</td><td style="text-align:center;border-color: lightgray;">' + d.delivery_date + '</td></tr>';
                });
                tableBody += '<table>';

                // FINALLY ADD THE NEWLY CREATED TABLE WITH JSON DATA TO A CONTAINER.

                var divContainer = document.getElementById("showData");
                divContainer.innerHTML = tableBody;
            }
        }
    });
}

//to get serial no
function get_serial_no(serial_no) {
    console.log("enetered in function block");
    var details;
    frappe.call({

        method: "jiq.www.CertificationDocuments.serial_no",
        args: {
            "serial_no": serial_no
        },
        async: false,
        callback: function(r) {

            details = r.message;
            console.log("details", details);

            var all_data = details;

            console.log("get_serial_no", details);
            if (all_data == "") {

                frappe.msgprint("Nothing to Display - Please change filters and try again");
            } else {

                var tableBody = '<table width="100%" cellpadding="3" align="center" style="border-collapse:collapse;border-color: lightgray;" border="1"><tr style="font-weight:bold;text-align:center;background-color: #8c8a8a;"><td style="color:white;">Item Name</td><td style="color:white;">Item Serial No</td><td style="color:white;">COC</td><td style="color:white;">Pressure Test</td><td style="color:white;">Build Sheet</td><td style="color:white;">DNV-GL Product Certificate</td><td style="color:white;">EU Declaration of Conformity</td><td style="color:white;">Docpack</td><td style="color:white;">Customer PO</td><td style="color:white;">Delivery Note</td><td style="color:white;">Delivery Note Date</td></tr>';

                all_data.forEach(function(d) {
                    tableBody += '<tr><td style="text-align:left;border-color: lightgray;">' + d.item_name + '</td><td style="text-align:left;border-color: lightgray;">' + d.serial_no + '</td><td style="text-align:center;border-color: lightgray;">' + d.pch1_coc + '</td><td style="text-align:center;border-color: lightgray;">' + d.pch1_pressure_test + '</td><td style="text-align:center;border-color: lightgray;">' + d.pch1_build_sheet + '</td><td style="text-align:center;border-color: lightgray;">' + d.pch1_dnv_gl_product_certificate + '</td><td style="text-align:center;border-color: lightgray;">' + d.pch1_eu_declaration_of_conformity + '</td><td style="text-align:center;border-color: lightgray;">' + d.pch1_combined_pdf + '</td><td style="text-align:center;border-color: lightgray;">' + d.po_no + '</td><td style="text-align:left;border-color: lightgray;">' + d.delivery_document_no + '</td><td style="text-align:center;border-color: lightgray;">' + d.delivery_date + '</td></tr>';
                });
                tableBody += '<table>';

                // FINALLY ADD THE NEWLY CREATED TABLE WITH JSON DATA TO A CONTAINER.

                var divContainer = document.getElementById("showData");
                divContainer.innerHTML = tableBody;
            }
        }

    });
}
