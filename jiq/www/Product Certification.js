//onload this frappe call will execute.It will get all data from database
var details;
var item_code = [];
var serial_no = [];
var sales_order = [];

console.log("before call", details);
frappe.call({

    method: "jiq.www.Product Certification.api_user",

    async: false,
    callback: function(r) {

        details = r.message;
        console.log("inside", details);

        var all_data = details;

        $(function() {
            $.each(all_data, function() {
                var tabledata = $('#itemList tbody').append('<tr><td style="text-align:left;padding-left: 4px;">' + this.item_name + '</td><td style="text-align:left;padding-left: 4px;">' + this.serial_no + '</td>' + ((this.pch_coc == "" || this.pch_coc == null) ? '<td></td>' : '<td style="text-align:center;">' + "<a href=" + this.pch_coc + " " + "target='_blank'><img src='/files/pdf.jpg'  width='25' height='25'></a>" + '</td>') + '' + ((this.pch_pressure_test == "" || this.pch_pressure_test == null) ? '<td></td>' : '<td style="text-align:center;">' + "<a href=" + this.pch_pressure_test + " " + "target='_blank'><img src='/files/pdf.jpg'  width='25' height='25'></a>" + '</td>') + '' + ((this.pch_build_sheet == "" || this.pch_build_sheet == null) ? '<td></td>' : '<td style="text-align:center;">' + "<a href=" + this.pch_build_sheet + " " + "target='_blank'><img src='/files/pdf.jpg'  width='25' height='25'></a>" + '</td>') + '' + ((this.pch_dnv_gl_product_certificate == "" || this.pch_dnv_gl_product_certificate == null) ? '<td></td>' : '<td style="text-align:center;">' + "<a href=" + this.pch_dnv_gl_product_certificate + " " + "target='_blank'><img src='/files/pdf.jpg'  width='25' height='25'></a>" + '</td>') + '' + ((this.pch_eu_declaration == "" || this.pch_eu_declaration == null) ? '<td></td>' : '<td style="text-align:center;">' + "<a href=" + this.pch_eu_declaration + " " + "target='_blank'><img src='/files/pdf.jpg'  width='25' height='25'></a>" + '</td>') + '' + ((this.pch1_combined_pdf == "" || this.pch1_combined_pdf == null) ? '<td></td>' : '<td style="text-align:center;">' + this.pch1_combined_pdf + '</td>') + '<td style="text-align:center;">' + this.po_no + '</td><td style="text-align:left;padding-left: 4px;">' + this.delivery_document_no + '</td><td style="text-align:center;">' + this.delivery_date + '</td></tr>');

            });
        });

        // FINALLY ADD THE NEWLY CREATED TABLE WITH JSON DATA TO A CONTAINER.
        document.getElementById("totalrows").innerText = "Total No Of Records:" + details.length;
        $(document).ready(function() {
            $('#itemList').after('<div  id="nav" style="text-align: center;"></div>');
            var rowsShown = 20;
            var rowsTotal = $('#itemList tbody tr').length;
            var numPages = rowsTotal / rowsShown;
            for (i = 0; i < numPages; i++) {
                var pageNum = i + 1;
                $('#nav').append('<a href="#" rel="' + i + '">' + pageNum + '</a> ');
            }
            $('#itemList tbody tr').hide();
            $('#itemList tbody tr').slice(0, rowsShown).show();
            $('#nav a:first').addClass('active');
            $('#nav a').bind('click', function() {

                $('#nav a').removeClass('active');
                $(this).addClass('active');
                var currPage = $(this).attr('rel');
                var startItem = currPage * rowsShown;
                var endItem = startItem + rowsShown;
                $('#itemList tbody tr').css('opacity', '0.0').hide().slice(startItem, endItem).
                css('display', 'table-row').animate({
                    opacity: 1
                }, 300);
            });
        });



    }


});




$('#customer_po').keypress(function(e) {
    if (e.which == 13) { //Enter key pressed
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
});

$('#delivery_note').keypress(function(e) {
    if (e.which == 13) { //Enter key pressed


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
});

$('#item_serial_no').keypress(function(e) {
    if (e.which == 13) { //Enter key pressed


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

        method: "jiq.www.Product Certification.delivery_serial",
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
                $("#data-container").empty();
                $(function() {
                    $.each(all_data, function() {
                        var tabledata = $('#itemList tbody').append('<tr><td style="text-align:left;padding-left: 4px;">' + this.item_name + '</td><td style="text-align:left;padding-left: 4px;">' + this.serial_no + '</td>' + ((this.pch_coc == "" || this.pch_coc == null) ? '<td></td>' : '<td style="text-align:center;">' + "<a href=" + this.pch_coc + " " + "target='_blank'><img src='/files/pdf.jpg'  width='25' height='25'></a>" + '</td>') + '' + ((this.pch_pressure_test == "" || this.pch_pressure_test == null) ? '<td></td>' : '<td style="text-align:center;">' + "<a href=" + this.pch_pressure_test + " " + "target='_blank'><img src='/files/pdf.jpg'  width='25' height='25'></a>" + '</td>') + '' + ((this.pch_build_sheet == "" || this.pch_build_sheet == null) ? '<td></td>' : '<td style="text-align:center;">' + "<a href=" + this.pch_build_sheet + " " + "target='_blank'><img src='/files/pdf.jpg'  width='25' height='25'></a>" + '</td>') + '' + ((this.pch_dnv_gl_product_certificate == "" || this.pch_dnv_gl_product_certificate == null) ? '<td></td>' : '<td style="text-align:center;">' + "<a href=" + this.pch_dnv_gl_product_certificate + " " + "target='_blank'><img src='/files/pdf.jpg'  width='25' height='25'></a>" + '</td>') + '' + ((this.pch_eu_declaration == "" || this.pch_eu_declaration == null) ? '<td></td>' : '<td style="text-align:center;">' + "<a href=" + this.pch_eu_declaration + " " + "target='_blank'><img src='/files/pdf.jpg'  width='25' height='25'></a>" + '</td>') + '' + ((this.pch1_combined_pdf == "" || this.pch1_combined_pdf == null) ? '<td></td>' : '<td style="text-align:center;">' + this.pch1_combined_pdf + '</td>') + '<td style="text-align:center;">' + this.po_no + '</td><td style="text-align:left;padding-left: 4px;">' + this.delivery_document_no + '</td><td style="text-align:center;">' + this.delivery_date + '</td></tr>');
                    });
                });
                // FINALLY ADD THE NEWLY CREATED TABLE WITH JSON DATA TO A CONTAINER.
                document.getElementById("totalrows").innerText = "Total No Of Records:" + details.length;
                
        $(document).ready(function() {
            
            $("#nav").remove();
            $('#itemList').after('<div id="nav" style="text-align: center;"></div>');
            var rowsShown = 20;
            var rowsTotal = $('#itemList tbody tr').length;
            var numPages = rowsTotal / rowsShown;
            for (i = 0; i < numPages; i++) {
                var pageNum = i + 1;
                $('#nav').append('<a href="#" rel="' + i + '">' + pageNum + '</a> ');
            }
            $('#itemList tbody tr').hide();
            $('#itemList tbody tr').slice(0, rowsShown).show();
            $('#nav a:first').addClass('active');
            $('#nav a').bind('click', function() {

                $('#nav a').removeClass('active');
                $(this).addClass('active');
                var currPage = $(this).attr('rel');
                var startItem = currPage * rowsShown;
                var endItem = startItem + rowsShown;
                $('#itemList tbody tr').css('opacity', '0.0').hide().slice(startItem, endItem).
                css('display', 'table-row').animate({
                    opacity: 1
                }, 300);
            });
        });
            }
        }

    });

}


//po_no and delivery note

function get_value_of_po_delivery(po_no, delivery_document_no) {
    console.log("enetered in function block");
    var details;
    frappe.call({

        method: "jiq.www.Product Certification.po_delivery",
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
                $("#data-container").empty();
                $(function() {
                    $.each(all_data, function() {
                        var tabledata = $('#itemList tbody').append('<tr><td style="text-align:left;padding-left: 4px;">' + this.item_name + '</td><td style="text-align:left;padding-left: 4px;">' + this.serial_no + '</td>' + ((this.pch_coc == "" || this.pch_coc == null) ? '<td></td>' : '<td style="text-align:center;">' + "<a href=" + this.pch_coc + " " + "target='_blank'><img src='/files/pdf.jpg'  width='25' height='25'></a>" + '</td>') + '' + ((this.pch_pressure_test == "" || this.pch_pressure_test == null) ? '<td></td>' : '<td style="text-align:center;">' + "<a href=" + this.pch_pressure_test + " " + "target='_blank'><img src='/files/pdf.jpg'  width='25' height='25'></a>" + '</td>') + '' + ((this.pch_build_sheet == "" || this.pch_build_sheet == null) ? '<td></td>' : '<td style="text-align:center;">' + "<a href=" + this.pch_build_sheet + " " + "target='_blank'><img src='/files/pdf.jpg'  width='25' height='25'></a>" + '</td>') + '' + ((this.pch_dnv_gl_product_certificate == "" || this.pch_dnv_gl_product_certificate == null) ? '<td></td>' : '<td style="text-align:center;">' + "<a href=" + this.pch_dnv_gl_product_certificate + " " + "target='_blank'><img src='/files/pdf.jpg'  width='25' height='25'></a>" + '</td>') + '' + ((this.pch_eu_declaration == "" || this.pch_eu_declaration == null) ? '<td></td>' : '<td style="text-align:center;">' + "<a href=" + this.pch_eu_declaration + " " + "target='_blank'><img src='/files/pdf.jpg'  width='25' height='25'></a>" + '</td>') + '' + ((this.pch1_combined_pdf == "" || this.pch1_combined_pdf == null) ? '<td></td>' : '<td style="text-align:center;">' + this.pch1_combined_pdf + '</td>') + '<td style="text-align:center;">' + this.po_no + '</td><td style="text-align:left;padding-left: 4px;">' + this.delivery_document_no + '</td><td style="text-align:center;">' + this.delivery_date + '</td></tr>');
                    });
                });
                // FINALLY ADD THE NEWLY CREATED TABLE WITH JSON DATA TO A CONTAINER.
                
                document.getElementById("totalrows").innerText = "Total No Of Records:" + details.length;
        $(document).ready(function() {
            
            $("#nav").remove();
            $('#itemList').after('<div id="nav" style="text-align: center;"></div>');
            var rowsShown = 20;
            var rowsTotal = $('#itemList tbody tr').length;
            var numPages = rowsTotal / rowsShown;
            for (i = 0; i < numPages; i++) {
                var pageNum = i + 1;
                $('#nav').append('<a href="#" rel="' + i + '">' + pageNum + '</a> ');
            }
            $('#itemList tbody tr').hide();
            $('#itemList tbody tr').slice(0, rowsShown).show();
            $('#nav a:first').addClass('active');
            $('#nav a').bind('click', function() {

                $('#nav a').removeClass('active');
                $(this).addClass('active');
                var currPage = $(this).attr('rel');
                var startItem = currPage * rowsShown;
                var endItem = startItem + rowsShown;
                $('#itemList tbody tr').css('opacity', '0.0').hide().slice(startItem, endItem).
                css('display', 'table-row').animate({
                    opacity: 1
                }, 300);
            });
        });
            }
        }

    });

}


//po_serial applied

function get_value_of_po_serial(po_no, serial_no) {
    console.log("enetered in function block");
    var details;
    frappe.call({

        method: "jiq.www.Product Certification.po_serial",
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
                $("#data-container").empty();
                $(function() {
                    $.each(all_data, function() {
                        var tabledata = $('#itemList tbody').append('<tr><td style="text-align:left;padding-left: 4px;">' + this.item_name + '</td><td style="text-align:left;padding-left: 4px;">' + this.serial_no + '</td>' + ((this.pch_coc == "" || this.pch_coc == null) ? '<td></td>' : '<td style="text-align:center;">' + "<a href=" + this.pch_coc + " " + "target='_blank'><img src='/files/pdf.jpg'  width='25' height='25'></a>" + '</td>') + '' + ((this.pch_pressure_test == "" || this.pch_pressure_test == null) ? '<td></td>' : '<td style="text-align:center;">' + "<a href=" + this.pch_pressure_test + " " + "target='_blank'><img src='/files/pdf.jpg'  width='25' height='25'></a>" + '</td>') + '' + ((this.pch_build_sheet == "" || this.pch_build_sheet == null) ? '<td></td>' : '<td style="text-align:center;">' + "<a href=" + this.pch_build_sheet + " " + "target='_blank'><img src='/files/pdf.jpg'  width='25' height='25'></a>" + '</td>') + '' + ((this.pch_dnv_gl_product_certificate == "" || this.pch_dnv_gl_product_certificate == null) ? '<td></td>' : '<td style="text-align:center;">' + "<a href=" + this.pch_dnv_gl_product_certificate + " " + "target='_blank'><img src='/files/pdf.jpg'  width='25' height='25'></a>" + '</td>') + '' + ((this.pch_eu_declaration == "" || this.pch_eu_declaration == null) ? '<td></td>' : '<td style="text-align:center;">' + "<a href=" + this.pch_eu_declaration + " " + "target='_blank'><img src='/files/pdf.jpg'  width='25' height='25'></a>" + '</td>') + '' + ((this.pch1_combined_pdf == "" || this.pch1_combined_pdf == null) ? '<td></td>' : '<td style="text-align:center;">' + this.pch1_combined_pdf + '</td>') + '<td style="text-align:center;">' + this.po_no + '</td><td style="text-align:left;padding-left: 4px;">' + this.delivery_document_no + '</td><td style="text-align:center;">' + this.delivery_date + '</td></tr>');
                    });
                });

                // FINALLY ADD THE NEWLY CREATED TABLE WITH JSON DATA TO A CONTAINER.
                
                document.getElementById("totalrows").innerText = "Total No Of Records:" + details.length;
                $(document).ready(function() {
                    
                    $("#nav").remove();
                    $('#itemList').after('<div id="nav" style="text-align: center;"></div>');
                    var rowsShown = 20;
                    var rowsTotal = $('#itemList tbody tr').length;
                    var numPages = rowsTotal / rowsShown;
                    for (i = 0; i < numPages; i++) {
                        var pageNum = i + 1;
                        $('#nav').append('<a href="#" rel="' + i + '">' + pageNum + '</a> ');
                    }
                    $('#itemList tbody tr').hide();
                    $('#itemList tbody tr').slice(0, rowsShown).show();
                    $('#nav a:first').addClass('active');
                    $('#nav a').bind('click', function() {
        
                        $('#nav a').removeClass('active');
                        $(this).addClass('active');
                        var currPage = $(this).attr('rel');
                        var startItem = currPage * rowsShown;
                        var endItem = startItem + rowsShown;
                        $('#itemList tbody tr').css('opacity', '0.0').hide().slice(startItem, endItem).
                        css('display', 'table-row').animate({
                            opacity: 1
                        }, 300);
                    });
                });
                    }
                }
        
            });
        
        }
        

//all filters applied

function get_value_of_all_filters(po_no, delivery_document_no, serial_no) {
    console.log("enetered in function block");
    var details;
    frappe.call({

        method: "jiq.www.Product Certification.all_filters_applied",
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
                $("#data-container").empty();
                $(function() {
                    $.each(all_data, function() {
                        var tabledata = $('#itemList tbody').append('<tr><td style="text-align:left;padding-left: 4px;">' + this.item_name + '</td><td style="text-align:left;padding-left: 4px;">' + this.serial_no + '</td>' + ((this.pch_coc == "" || this.pch_coc == null) ? '<td></td>' : '<td style="text-align:center;">' + "<a href=" + this.pch_coc + " " + "target='_blank'><img src='/files/pdf.jpg'  width='25' height='25'></a>" + '</td>') + '' + ((this.pch_pressure_test == "" || this.pch_pressure_test == null) ? '<td></td>' : '<td style="text-align:center;">' + "<a href=" + this.pch_pressure_test + " " + "target='_blank'><img src='/files/pdf.jpg'  width='25' height='25'></a>" + '</td>') + '' + ((this.pch_build_sheet == "" || this.pch_build_sheet == null) ? '<td></td>' : '<td style="text-align:center;">' + "<a href=" + this.pch_build_sheet + " " + "target='_blank'><img src='/files/pdf.jpg'  width='25' height='25'></a>" + '</td>') + '' + ((this.pch_dnv_gl_product_certificate == "" || this.pch_dnv_gl_product_certificate == null) ? '<td></td>' : '<td style="text-align:center;">' + "<a href=" + this.pch_dnv_gl_product_certificate + " " + "target='_blank'><img src='/files/pdf.jpg'  width='25' height='25'></a>" + '</td>') + '' + ((this.pch_eu_declaration == "" || this.pch_eu_declaration == null) ? '<td></td>' : '<td style="text-align:center;">' + "<a href=" + this.pch_eu_declaration + " " + "target='_blank'><img src='/files/pdf.jpg'  width='25' height='25'></a>" + '</td>') + '' + ((this.pch1_combined_pdf == "" || this.pch1_combined_pdf == null) ? '<td></td>' : '<td style="text-align:center;">' + this.pch1_combined_pdf + '</td>') + '<td style="text-align:center;">' + this.po_no + '</td><td style="text-align:left;padding-left: 4px;">' + this.delivery_document_no + '</td><td style="text-align:center;">' + this.delivery_date + '</td></tr>');
                    });
                });
                // FINALLY ADD THE NEWLY CREATED TABLE WITH JSON DATA TO A CONTAINER.
                document.getElementById("totalrows").innerText = "Total No Of Records:" + details.length;
        $(document).ready(function() {
            
            $("#nav").remove();
            $('#itemList').after('<div id="nav" style="text-align: center;"></div>');
            var rowsShown = 20;
            var rowsTotal = $('#itemList tbody tr').length;
            var numPages = rowsTotal / rowsShown;
            for (i = 0; i < numPages; i++) {
                var pageNum = i + 1;
                $('#nav').append('<a href="#" rel="' + i + '">' + pageNum + '</a> ');
            }
            $('#itemList tbody tr').hide();
            $('#itemList tbody tr').slice(0, rowsShown).show();
            $('#nav a:first').addClass('active');
            $('#nav a').bind('click', function() {

                $('#nav a').removeClass('active');
                $(this).addClass('active');
                var currPage = $(this).attr('rel');
                var startItem = currPage * rowsShown;
                var endItem = startItem + rowsShown;
                $('#itemList tbody tr').css('opacity', '0.0').hide().slice(startItem, endItem).
                css('display', 'table-row').animate({
                    opacity: 1
                }, 300);
            });
        });
            }
        }

    });

}



//this function get all data when nothing is selected in filters
function get_all() {
    frappe.call({

        method: "jiq.www.Product Certification.api_user",

        async: false,
        callback: function(r) {

            details = r.message;
            console.log("inside", details);
            var all_data = details;
            console.log("all_data", all_data);
            if (all_data == "") {

                frappe.msgprint("Nothing to Display - Please change filters and try again");
            } else {
                $("#data-container").empty();
                $(function() {
                    $.each(all_data, function() {
                        var tabledata = $('#itemList tbody').append('<tr><td style="text-align:left;padding-left: 4px;">' + this.item_name + '</td><td style="text-align:left;padding-left: 4px;">' + this.serial_no + '</td>' + ((this.pch_coc == "" || this.pch_coc == null) ? '<td></td>' : '<td style="text-align:center;">' + "<a href=" + this.pch_coc + " " + "target='_blank'><img src='/files/pdf.jpg'  width='25' height='25'></a>" + '</td>') + '' + ((this.pch_pressure_test == "" || this.pch_pressure_test == null) ? '<td></td>' : '<td style="text-align:center;">' + "<a href=" + this.pch_pressure_test + " " + "target='_blank'><img src='/files/pdf.jpg'  width='25' height='25'></a>" + '</td>') + '' + ((this.pch_build_sheet == "" || this.pch_build_sheet == null) ? '<td></td>' : '<td style="text-align:center;">' + "<a href=" + this.pch_build_sheet + " " + "target='_blank'><img src='/files/pdf.jpg'  width='25' height='25'></a>" + '</td>') + '' + ((this.pch_dnv_gl_product_certificate == "" || this.pch_dnv_gl_product_certificate == null) ? '<td></td>' : '<td style="text-align:center;">' + "<a href=" + this.pch_dnv_gl_product_certificate + " " + "target='_blank'><img src='/files/pdf.jpg'  width='25' height='25'></a>" + '</td>') + '' + ((this.pch_eu_declaration == "" || this.pch_eu_declaration == null) ? '<td></td>' : '<td style="text-align:center;">' + "<a href=" + this.pch_eu_declaration + " " + "target='_blank'><img src='/files/pdf.jpg'  width='25' height='25'></a>" + '</td>') + '' + ((this.pch1_combined_pdf == "" || this.pch1_combined_pdf == null) ? '<td></td>' : '<td style="text-align:center;">' + this.pch1_combined_pdf + '</td>') + '<td style="text-align:center;">' + this.po_no + '</td><td style="text-align:left;padding-left: 4px;">' + this.delivery_document_no + '</td><td style="text-align:center;">' + this.delivery_date + '</td></tr>');
                    });
                });
                // FINALLY ADD THE NEWLY CREATED TABLE WITH JSON DATA TO A CONTAINER.
                document.getElementById("totalrows").innerText = "Total No Of Records:" + details.length;
        $(document).ready(function() {
            
            $("#nav").remove();
            $('#itemList').after('<div id="nav" style="text-align: center;"></div>');
            var rowsShown = 20;
            var rowsTotal = $('#itemList tbody tr').length;
            var numPages = rowsTotal / rowsShown;
            for (i = 0; i < numPages; i++) {
                var pageNum = i + 1;
                $('#nav').append('<a href="#" rel="' + i + '">' + pageNum + '</a> ');
            }
            $('#itemList tbody tr').hide();
            $('#itemList tbody tr').slice(0, rowsShown).show();
            $('#nav a:first').addClass('active');
            $('#nav a').bind('click', function() {

                $('#nav a').removeClass('active');
                $(this).addClass('active');
                var currPage = $(this).attr('rel');
                var startItem = currPage * rowsShown;
                var endItem = startItem + rowsShown;
                $('#itemList tbody tr').css('opacity', '0.0').hide().slice(startItem, endItem).
                css('display', 'table-row').animate({
                    opacity: 1
                }, 300);
            });
        });
            }
        }

    });

}

//to get po
function get_po_no(po_no) {
    console.log("enetered in function block");
    var details;
    frappe.call({

        method: "jiq.www.Product Certification.po_no",
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
                $("#data-container").empty();
                var po_detials = details;
                console.log("po_detials", po_detials);
                $(function() {
                    $.each(po_detials, function() {
                        var tabledata = $('#itemList tbody').append('<tr><td style="text-align:left;padding-left: 4px;">' + this.item_name + '</td><td style="text-align:left;padding-left: 4px;">' + this.serial_no + '</td>' + ((this.pch_coc == "" || this.pch_coc == null) ? '<td></td>' : '<td style="text-align:center;">' + "<a href=" + this.pch_coc + " " + "target='_blank'><img src='/files/pdf.jpg'  width='25' height='25'></a>" + '</td>') + '' + ((this.pch_pressure_test == "" || this.pch_pressure_test == null) ? '<td></td>' : '<td style="text-align:center;">' + "<a href=" + this.pch_pressure_test + " " + "target='_blank'><img src='/files/pdf.jpg'  width='25' height='25'></a>" + '</td>') + '' + ((this.pch_build_sheet == "" || this.pch_build_sheet == null) ? '<td></td>' : '<td style="text-align:center;">' + "<a href=" + this.pch_build_sheet + " " + "target='_blank'><img src='/files/pdf.jpg'  width='25' height='25'></a>" + '</td>') + '' + ((this.pch_dnv_gl_product_certificate == "" || this.pch_dnv_gl_product_certificate == null) ? '<td></td>' : '<td style="text-align:center;">' + "<a href=" + this.pch_dnv_gl_product_certificate + " " + "target='_blank'><img src='/files/pdf.jpg'  width='25' height='25'></a>" + '</td>') + '' + ((this.pch_eu_declaration == "" || this.pch_eu_declaration == null) ? '<td></td>' : '<td style="text-align:center;">' + "<a href=" + this.pch_eu_declaration + " " + "target='_blank'><img src='/files/pdf.jpg'  width='25' height='25'></a>" + '</td>') + '' + ((this.pch1_combined_pdf == "" || this.pch1_combined_pdf == null) ? '<td></td>' : '<td style="text-align:center;">' + this.pch1_combined_pdf + '</td>') + '<td style="text-align:center;">' + this.po_no + '</td><td style="text-align:left;padding-left: 4px;">' + this.delivery_document_no + '</td><td style="text-align:center;">' + this.delivery_date + '</td></tr>');
                    });
                });
                document.getElementById("totalrows").innerText = "Total No Of Records:" + details.length;
                $(document).ready(function() {
            
                    $("#nav").remove();
                    $('#itemList').after('<div id="nav" style="text-align: center;"></div>');
                    var rowsShown = 20;
                    var rowsTotal = $('#itemList tbody tr').length;
                    var numPages = rowsTotal / rowsShown;
                    for (i = 0; i < numPages; i++) {
                        var pageNum = i + 1;
                        $('#nav').append('<a href="#" rel="' + i + '">' + pageNum + '</a> ');
                    }
                    $('#itemList tbody tr').hide();
                    $('#itemList tbody tr').slice(0, rowsShown).show();
                    $('#nav a:first').addClass('active');
                    $('#nav a').bind('click', function() {
        
                        $('#nav a').removeClass('active');
                        $(this).addClass('active');
                        var currPage = $(this).attr('rel');
                        var startItem = currPage * rowsShown;
                        var endItem = startItem + rowsShown;
                        $('#itemList tbody tr').css('opacity', '0.0').hide().slice(startItem, endItem).
                        css('display', 'table-row').animate({
                            opacity: 1
                        }, 300);
                    });
                });
                    }
                }
        
            });
        
        }

//get delivery document no
function get_delivery_document_no(delivery_document_no) {
    console.log("enetered in function block");
    var details;
    frappe.call({

        method: "jiq.www.Product Certification.delivery_document_no",
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
                $("#data-container").empty();
                $(function() {
                    $.each(all_data, function() {
                        var tabledata = $('#itemList tbody').append('<tr><td style="text-align:left;padding-left: 4px;">' + this.item_name + '</td><td style="text-align:left;padding-left: 4px;">' + this.serial_no + '</td>' + ((this.pch_coc == "" || this.pch_coc == null) ? '<td></td>' : '<td style="text-align:center;">' + "<a href=" + this.pch_coc + " " + "target='_blank'><img src='/files/pdf.jpg'  width='25' height='25'></a>" + '</td>') + '' + ((this.pch_pressure_test == "" || this.pch_pressure_test == null) ? '<td></td>' : '<td style="text-align:center;">' + "<a href=" + this.pch_pressure_test + " " + "target='_blank'><img src='/files/pdf.jpg'  width='25' height='25'></a>" + '</td>') + '' + ((this.pch_build_sheet == "" || this.pch_build_sheet == null) ? '<td></td>' : '<td style="text-align:center;">' + "<a href=" + this.pch_build_sheet + " " + "target='_blank'><img src='/files/pdf.jpg'  width='25' height='25'></a>" + '</td>') + '' + ((this.pch_dnv_gl_product_certificate == "" || this.pch_dnv_gl_product_certificate == null) ? '<td></td>' : '<td style="text-align:center;">' + "<a href=" + this.pch_dnv_gl_product_certificate + " " + "target='_blank'><img src='/files/pdf.jpg'  width='25' height='25'></a>" + '</td>') + '' + ((this.pch_eu_declaration == "" || this.pch_eu_declaration == null) ? '<td></td>' : '<td style="text-align:center;">' + "<a href=" + this.pch_eu_declaration + " " + "target='_blank'><img src='/files/pdf.jpg'  width='25' height='25'></a>" + '</td>') + '' + ((this.pch1_combined_pdf == "" || this.pch1_combined_pdf == null) ? '<td></td>' : '<td style="text-align:center;">' + this.pch1_combined_pdf + '</td>') + '<td style="text-align:center;">' + this.po_no + '</td><td style="text-align:left;padding-left: 4px;">' + this.delivery_document_no + '</td><td style="text-align:center;">' + this.delivery_date + '</td></tr>');
                    });
                });
                // FINALLY ADD THE NEWLY CREATED TABLE WITH JSON DATA TO A CONTAINER.
                document.getElementById("totalrows").innerText = "Total No Of Records:" + details.length;
                $(document).ready(function() {
            
                    $("#nav").remove();
                    $('#itemList').after('<div id="nav" style="text-align: center;"></div>');
                    var rowsShown = 20;
                    var rowsTotal = $('#itemList tbody tr').length;
                    var numPages = rowsTotal / rowsShown;
                    for (i = 0; i < numPages; i++) {
                        var pageNum = i + 1;
                        $('#nav').append('<a href="#" rel="' + i + '">' + pageNum + '</a> ');
                    }
                    $('#itemList tbody tr').hide();
                    $('#itemList tbody tr').slice(0, rowsShown).show();
                    $('#nav a:first').addClass('active');
                    $('#nav a').bind('click', function() {
        
                        $('#nav a').removeClass('active');
                        $(this).addClass('active');
                        var currPage = $(this).attr('rel');
                        var startItem = currPage * rowsShown;
                        var endItem = startItem + rowsShown;
                        $('#itemList tbody tr').css('opacity', '0.0').hide().slice(startItem, endItem).
                        css('display', 'table-row').animate({
                            opacity: 1
                        }, 300);
                    });
                });
                    }
                }
        
            });
        
        }


//to get serial no
function get_serial_no(serial_no) {
    console.log("enetered in function block");
    var details;
    frappe.call({

        method: "jiq.www.Product Certification.serial_no",
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
                $("#data-container").empty();
                $(function() {
                    $.each(all_data, function() {
                        var tabledata = $('#itemList tbody').append('<tr><td style="text-align:left;padding-left: 4px;">' + this.item_name + '</td><td style="text-align:left;padding-left: 4px;">' + this.serial_no + '</td>' + ((this.pch_coc == "" || this.pch_coc == null) ? '<td></td>' : '<td style="text-align:center;">' + "<a href=" + this.pch_coc + " " + "target='_blank'><img src='/files/pdf.jpg'  width='25' height='25'></a>" + '</td>') + '' + ((this.pch_pressure_test == "" || this.pch_pressure_test == null) ? '<td></td>' : '<td style="text-align:center;">' + "<a href=" + this.pch_pressure_test + " " + "target='_blank'><img src='/files/pdf.jpg'  width='25' height='25'></a>" + '</td>') + '' + ((this.pch_build_sheet == "" || this.pch_build_sheet == null) ? '<td></td>' : '<td style="text-align:center;">' + "<a href=" + this.pch_build_sheet + " " + "target='_blank'><img src='/files/pdf.jpg'  width='25' height='25'></a>" + '</td>') + '' + ((this.pch_dnv_gl_product_certificate == "" || this.pch_dnv_gl_product_certificate == null) ? '<td></td>' : '<td style="text-align:center;">' + "<a href=" + this.pch_dnv_gl_product_certificate + " " + "target='_blank'><img src='/files/pdf.jpg'  width='25' height='25'></a>" + '</td>') + '' + ((this.pch_eu_declaration == "" || this.pch_eu_declaration == null) ? '<td></td>' : '<td style="text-align:center;">' + "<a href=" + this.pch_eu_declaration + " " + "target='_blank'><img src='/files/pdf.jpg'  width='25' height='25'></a>" + '</td>') + '' + ((this.pch1_combined_pdf == "" || this.pch1_combined_pdf == null) ? '<td></td>' : '<td style="text-align:center;">' + this.pch1_combined_pdf + '</td>') + '<td style="text-align:center;">' + this.po_no + '</td><td style="text-align:left;padding-left: 4px;">' + this.delivery_document_no + '</td><td style="text-align:center;">' + this.delivery_date + '</td></tr>');
                    });
                });

                // FINALLY ADD THE NEWLY CREATED TABLE WITH JSON DATA TO A CONTAINER.
                document.getElementById("totalrows").innerText = "Total No Of Records:" + details.length;
                $(document).ready(function() {
            
                    $("#nav").remove();
                    $('#itemList').after('<div id="nav" style="text-align: center;"></div>');
                    var rowsShown = 20;
                    var rowsTotal = $('#itemList tbody tr').length;
                    var numPages = rowsTotal / rowsShown;
                    for (i = 0; i < numPages; i++) {
                        var pageNum = i + 1;
                        $('#nav').append('<a href="#" rel="' + i + '">' + pageNum + '</a> ');
                    }
                    $('#itemList tbody tr').hide();
                    $('#itemList tbody tr').slice(0, rowsShown).show();
                    $('#nav a:first').addClass('active');
                    $('#nav a').bind('click', function() {
        
                        $('#nav a').removeClass('active');
                        $(this).addClass('active');
                        var currPage = $(this).attr('rel');
                        var startItem = currPage * rowsShown;
                        var endItem = startItem + rowsShown;
                        $('#itemList tbody tr').css('opacity', '0.0').hide().slice(startItem, endItem).
                        css('display', 'table-row').animate({
                            opacity: 1
                        }, 300);
                    });
                });
                    }
                }
        
            });
        
        }
