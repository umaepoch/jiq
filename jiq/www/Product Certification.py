# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# MIT License. See license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
import frappe.www.list
import datetime

no_cache = 1
filtered_values = {}
def get_context(context):
	if frappe.session.user=='Guest':
		frappe.throw(_("You need to be logged in to access this page"), frappe.PermissionError)

	context.show_sidebar=True

@frappe.whitelist()
def delivery_serial(delivery_document_no,serial_no):
	user=frappe.db.get_value("User",{"name":frappe.session.user},"name")
	#print("user",user);
	customer_name = frappe.db.sql("""select  customer from `tabCustomer Profile` where docstatus=1 and user='"""+user+"""' """)
	#print("customer_name",customer_name);
	customer=""
	for customername in customer_name:customer=customername[0]
	delivery_serial_list = frappe.db.sql("""select sn.item_name,sn.serial_no,sn.pch_coc,sn.pch_pressure_test,sn.pch_build_sheet,sn.pch1_combined_pdf,sn.pch_dnv_gl_product_certificate,sn.pch_eu_declaration,dn.po_no,sn.delivery_document_no,
DATE_FORMAT(sn.delivery_date, '%d-%m-%Y') as delivery_date from `tabSerial No` sn ,`tabDelivery Note` dn where sn.delivery_document_type!="Null" and sn.delivery_document_type="Delivery Note"  and sn.delivery_document_no=dn.name   and sn.serial_no  LIKE '"""+serial_no+"%""' and  sn.delivery_document_no  LIKE '"""+delivery_document_no+"%""' and sn.customer='"""+customer+"""' """ ,  as_dict = 1)
	
	return delivery_serial_list

@frappe.whitelist()
def po_delivery(po_no,delivery_document_no):
	user=frappe.db.get_value("User",{"name":frappe.session.user},"name")
	#print("user",user);
	customer_name = frappe.db.sql("""select  customer from `tabCustomer Profile` where docstatus=1 and user='"""+user+"""' """)
	#print("customer_name",customer_name);
	customer=""
	for customername in customer_name:customer=customername[0]
	po_delivery_list = frappe.db.sql("""select sn.item_name,sn.serial_no,sn.pch_coc,sn.pch_pressure_test,sn.pch_build_sheet,sn.pch1_combined_pdf,sn.pch_dnv_gl_product_certificate,sn.pch_eu_declaration,dn.po_no,sn.delivery_document_no,
DATE_FORMAT(sn.delivery_date, '%d-%m-%Y') as delivery_date from `tabSerial No` sn ,`tabDelivery Note` dn where sn.delivery_document_type!="Null" and sn.delivery_document_type="Delivery Note"  and sn.delivery_document_no=dn.name   and dn.po_no  LIKE '"""+po_no+"%""' and  sn.delivery_document_no  LIKE '"""+delivery_document_no+"%""' and sn.customer='"""+customer+"""' """ ,  as_dict = 1)
	
	return po_delivery_list

@frappe.whitelist()
def po_serial(po_no,serial_no):
	user=frappe.db.get_value("User",{"name":frappe.session.user},"name")
	#print("user",user);
	customer_name = frappe.db.sql("""select  customer from `tabCustomer Profile` where docstatus=1 and user='"""+user+"""' """)
	#print("customer_name",customer_name);
	customer=""
	for customername in customer_name:customer=customername[0]
	po_serial_list = frappe.db.sql("""select sn.item_name,sn.serial_no,sn.pch_coc,sn.pch_pressure_test,sn.pch_build_sheet,sn.pch1_combined_pdf,sn.pch_dnv_gl_product_certificate,sn.pch_eu_declaration,dn.po_no,sn.delivery_document_no,
DATE_FORMAT(sn.delivery_date, '%d-%m-%Y') as delivery_date from `tabSerial No` sn ,`tabDelivery Note` dn where sn.delivery_document_type!="Null" and sn.delivery_document_type="Delivery Note"  and sn.delivery_document_no=dn.name   and dn.po_no  LIKE '"""+po_no+"%""' and  sn.serial_no  LIKE '"""+serial_no+"%""' and sn.customer='"""+customer+"""' """ ,  as_dict = 1)
	
	return po_serial_list

@frappe.whitelist()
def all_filters_applied(po_no,delivery_document_no,serial_no):
	user=frappe.db.get_value("User",{"name":frappe.session.user},"name")
	#print("user",user);
	customer_name = frappe.db.sql("""select  customer from `tabCustomer Profile` where docstatus=1 and user='"""+user+"""' """)
	#print("customer_name",customer_name);
	customer=""
	for customername in customer_name:customer=customername[0]
	list_of_all_data = frappe.db.sql("""select sn.item_name,sn.serial_no,sn.pch_coc,sn.pch_pressure_test,sn.pch_build_sheet,sn.pch1_combined_pdf,sn.pch_dnv_gl_product_certificate,sn.pch_eu_declaration,dn.po_no,sn.delivery_document_no,
DATE_FORMAT(sn.delivery_date, '%d-%m-%Y') as delivery_date from `tabSerial No` sn ,`tabDelivery Note` dn where sn.delivery_document_type!="Null" and sn.delivery_document_type="Delivery Note"  and sn.delivery_document_no=dn.name   and dn.po_no  LIKE '"""+po_no+"%""' and sn.serial_no  LIKE '"""+serial_no+"%""' and  sn.delivery_document_no  LIKE '"""+delivery_document_no+"%""' and sn.customer='"""+customer+"""' """ ,  as_dict = 1)
	
	return list_of_all_data


@frappe.whitelist()
def po_no(po_no):
	user=frappe.db.get_value("User",{"name":frappe.session.user},"name")
	#print("user",user);
	customer_name = frappe.db.sql("""select  customer from `tabCustomer Profile` where docstatus=1 and user='"""+user+"""' """)
	#print("customer_name",customer_name);
	customer=""
	for customername in customer_name:customer=customername[0]
	po_no_list = frappe.db.sql("""select sn.item_name,sn.serial_no,sn.pch_coc,sn.pch_pressure_test,sn.pch_build_sheet,sn.pch1_combined_pdf,sn.pch_dnv_gl_product_certificate,sn.pch_eu_declaration,dn.po_no,sn.delivery_document_no,
DATE_FORMAT(sn.delivery_date, '%d-%m-%Y') as delivery_date from `tabSerial No` sn ,`tabDelivery Note` dn where sn.delivery_document_type!="Null" and sn.delivery_document_type="Delivery Note"  and sn.delivery_document_no=dn.name  and dn.po_no  LIKE '"""+po_no+"%""' and sn.customer='"""+customer+"""' """ ,  as_dict = 1)
	return po_no_list

@frappe.whitelist()
def delivery_document_no(delivery_document_no):
	user=frappe.db.get_value("User",{"name":frappe.session.user},"name")
	#print("user",user);
	customer_name = frappe.db.sql("""select  customer from `tabCustomer Profile` where docstatus=1 and user='"""+user+"""' """)
	#print("customer_name",customer_name);
	customer=""
	for customername in customer_name:customer=customername[0]
	delivery_document_no_list = frappe.db.sql("""select sn.item_name,sn.serial_no,sn.pch_coc,sn.pch_pressure_test,sn.pch_build_sheet,sn.pch1_combined_pdf,sn.pch_dnv_gl_product_certificate,sn.pch_eu_declaration,dn.po_no,sn.delivery_document_no,
DATE_FORMAT(sn.delivery_date, '%d-%m-%Y') as delivery_date from `tabSerial No` sn ,`tabDelivery Note` dn where sn.delivery_document_type!="Null" and sn.delivery_document_type="Delivery Note"  and sn.delivery_document_no=dn.name  and sn.delivery_document_no  LIKE '"""+delivery_document_no+"%""' and sn.customer='"""+customer+"""' """ ,  as_dict = 1)
	return delivery_document_no_list

@frappe.whitelist()
def serial_no(serial_no):
	user=frappe.db.get_value("User",{"name":frappe.session.user},"name")
	#print("user",user);
	customer_name = frappe.db.sql("""select  customer from `tabCustomer Profile` where docstatus=1 and user='"""+user+"""' """)
	#print("customer_name",customer_name);
	customer=""
	for customername in customer_name:customer=customername[0]
	serial_no_list = frappe.db.sql("""select sn.item_name,sn.serial_no,sn.pch_coc,sn.pch_pressure_test,sn.pch_build_sheet,sn.pch1_combined_pdf,sn.pch_dnv_gl_product_certificate,sn.pch_eu_declaration,dn.po_no,sn.delivery_document_no,
DATE_FORMAT(sn.delivery_date, '%d-%m-%Y') as delivery_date from `tabSerial No` sn ,`tabDelivery Note` dn where sn.delivery_document_type!="Null" and sn.delivery_document_type="Delivery Note"  and sn.delivery_document_no=dn.name  and sn.serial_no  LIKE '"""+serial_no+"%""' and sn.customer='"""+customer+"""' """ ,  as_dict = 1)
	print("serial_no",serial_no_list)
	return serial_no_list



@frappe.whitelist()
def api_user():
	user=frappe.db.get_value("User",{"name":frappe.session.user},"name")
	#print("user",user);
	customer_name = frappe.db.sql("""select  customer from `tabCustomer Profile` where docstatus=1 and user='"""+user+"""' """)
	#print("customer_name",customer_name);
	customer=""
	for customername in customer_name:customer=customername[0]
	delivery_note_list = frappe.db.sql("""select sn.item_name,sn.serial_no,sn.pch_coc,sn.pch_pressure_test,sn.pch_build_sheet,sn.pch1_combined_pdf,sn.pch_dnv_gl_product_certificate,sn.pch_eu_declaration,dn.po_no,sn.delivery_document_no,
DATE_FORMAT(sn.delivery_date, '%d-%m-%Y') as delivery_date from `tabSerial No` sn ,`tabDelivery Note` dn where sn.delivery_document_type!="Null" and sn.delivery_document_type="Delivery Note"  and sn.delivery_document_no=dn.name and sn.customer='"""+customer+"""' """ ,  as_dict = 1)
	return delivery_note_list


