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
	user_name = frappe.db.sql("""select td.link_name from `tabContact` tc, `tabDynamic Link` td where td.link_doctype="Customer" and td.parent=tc.name and tc.user='"""+user+"""' """)
	#print("user_name",user_name);
	if(len(user_name)==1):
		for user_list in user_name:
			customer_list=user_list[0];
			delivery_note_list = frappe.db.sql("""select sn.item_name,sn.serial_no,sn.pch_coc,sn.pch_pressure_test,sn.pch_build_sheet,sn.pch1_combined_pdf,sn.pch_dnv_gl_product_certificate,sn.pch_eu_declaration,dn.po_no,sn.delivery_document_no,
	DATE_FORMAT(sn.delivery_date, '%d-%m-%Y') as delivery_date from `tabSerial No` sn ,`tabDelivery Note` dn where sn.delivery_document_type!="Null" and sn.delivery_document_type="Delivery Note"  and sn.delivery_document_no=dn.name and sn.serial_no  LIKE '"""+serial_no+"%""' and  sn.delivery_document_no  LIKE '"""+delivery_document_no+"%""' and sn.customer='"""+customer_list+"""' order by  delivery_date desc""" ,  as_dict = 1)
		#print("delivery_note_list",delivery_note_list)
		return delivery_note_list
	else:
		# List of tuple initialization
		contact_list = list(user_name)
		# using list comprehension
		list_primary_contact= [list_of_contact for t in contact_list for list_of_contact in t]
		customer_list=tuple(list_primary_contact);
		# printing output
		#print("customer_list",customer_list)
		delivery_note_list = frappe.db.sql("""select sn.item_name,sn.serial_no,sn.pch_coc,sn.pch_pressure_test,sn.pch_build_sheet,sn.pch1_combined_pdf,sn.pch_dnv_gl_product_certificate,sn.pch_eu_declaration,dn.po_no,sn.delivery_document_no,
	DATE_FORMAT(sn.delivery_date, '%d-%m-%Y') as delivery_date from `tabSerial No` sn ,`tabDelivery Note` dn where sn.delivery_document_type!="Null" and sn.delivery_document_type="Delivery Note"  and sn.delivery_document_no=dn.name and sn.serial_no  LIKE '"""+serial_no+"%""' and  sn.delivery_document_no  LIKE '"""+delivery_document_no+"%""' and sn.customer in """+str(customer_list)+""" order by  delivery_date desc""" ,  as_dict = 1)
		#print("delivery_note_list",delivery_note_list)
		return delivery_note_list

@frappe.whitelist()
def po_delivery(po_no,delivery_document_no):
	user=frappe.db.get_value("User",{"name":frappe.session.user},"name")
	#print("user",user);
	user_name = frappe.db.sql("""select td.link_name from `tabContact` tc, `tabDynamic Link` td where td.link_doctype="Customer" and td.parent=tc.name and tc.user='"""+user+"""' """)
	#print("user_name",user_name);
	if(len(user_name)==1):
		for user_list in user_name:
			customer_list=user_list[0];
			delivery_note_list = frappe.db.sql("""select sn.item_name,sn.serial_no,sn.pch_coc,sn.pch_pressure_test,sn.pch_build_sheet,sn.pch1_combined_pdf,sn.pch_dnv_gl_product_certificate,sn.pch_eu_declaration,dn.po_no,sn.delivery_document_no,
	DATE_FORMAT(sn.delivery_date, '%d-%m-%Y') as delivery_date from `tabSerial No` sn ,`tabDelivery Note` dn where sn.delivery_document_type!="Null" and sn.delivery_document_type="Delivery Note"  and sn.delivery_document_no=dn.name and dn.po_no  LIKE '"""+po_no+"%""' and  sn.delivery_document_no  LIKE '"""+delivery_document_no+"%""' and sn.customer='"""+customer_list+"""' order by  delivery_date desc""" ,  as_dict = 1)
		#print("delivery_note_list",delivery_note_list)
		return delivery_note_list
	else:
		# List of tuple initialization
		contact_list = list(user_name)
		# using list comprehension
		list_primary_contact= [list_of_contact for t in contact_list for list_of_contact in t]
		customer_list=tuple(list_primary_contact);
		# printing output
		#print("customer_list",customer_list)
		delivery_note_list = frappe.db.sql("""select sn.item_name,sn.serial_no,sn.pch_coc,sn.pch_pressure_test,sn.pch_build_sheet,sn.pch1_combined_pdf,sn.pch_dnv_gl_product_certificate,sn.pch_eu_declaration,dn.po_no,sn.delivery_document_no,
	DATE_FORMAT(sn.delivery_date, '%d-%m-%Y') as delivery_date from `tabSerial No` sn ,`tabDelivery Note` dn where sn.delivery_document_type!="Null" and sn.delivery_document_type="Delivery Note"  and sn.delivery_document_no=dn.name and dn.po_no  LIKE '"""+po_no+"%""' and  sn.delivery_document_no  LIKE '"""+delivery_document_no+"%""' and sn.customer in """+str(customer_list)+""" order by  delivery_date desc""" ,  as_dict = 1)
		#print("delivery_note_list",delivery_note_list)
		return delivery_note_list

@frappe.whitelist()
def po_serial(po_no,serial_no):
	user=frappe.db.get_value("User",{"name":frappe.session.user},"name")
	#print("user",user);
	user_name = frappe.db.sql("""select td.link_name from `tabContact` tc, `tabDynamic Link` td where td.link_doctype="Customer" and td.parent=tc.name and tc.user='"""+user+"""' """)
	#print("user_name",user_name);
	if(len(user_name)==1):
		for user_list in user_name:
			customer_list=user_list[0];
			delivery_note_list = frappe.db.sql("""select sn.item_name,sn.serial_no,sn.pch_coc,sn.pch_pressure_test,sn.pch_build_sheet,sn.pch1_combined_pdf,sn.pch_dnv_gl_product_certificate,sn.pch_eu_declaration,dn.po_no,sn.delivery_document_no,
	DATE_FORMAT(sn.delivery_date, '%d-%m-%Y') as delivery_date from `tabSerial No` sn ,`tabDelivery Note` dn where sn.delivery_document_type!="Null" and sn.delivery_document_type="Delivery Note"  and sn.delivery_document_no=dn.name and dn.po_no  LIKE '"""+po_no+"%""' and  sn.serial_no  LIKE '"""+serial_no+"%""' and sn.customer='"""+customer_list+"""' order by  delivery_date desc""" ,  as_dict = 1)
		#print("delivery_note_list",delivery_note_list)
		return delivery_note_list
	else:
		# List of tuple initialization
		contact_list = list(user_name)
		# using list comprehension
		list_primary_contact= [list_of_contact for t in contact_list for list_of_contact in t]
		customer_list=tuple(list_primary_contact);
		# printing output
		#print("customer_list",customer_list)
		delivery_note_list = frappe.db.sql("""select sn.item_name,sn.serial_no,sn.pch_coc,sn.pch_pressure_test,sn.pch_build_sheet,sn.pch1_combined_pdf,sn.pch_dnv_gl_product_certificate,sn.pch_eu_declaration,dn.po_no,sn.delivery_document_no,
	DATE_FORMAT(sn.delivery_date, '%d-%m-%Y') as delivery_date from `tabSerial No` sn ,`tabDelivery Note` dn where sn.delivery_document_type!="Null" and sn.delivery_document_type="Delivery Note"  and sn.delivery_document_no=dn.name and dn.po_no  LIKE '"""+po_no+"%""' and  sn.serial_no  LIKE '"""+serial_no+"%""' and sn.customer in """+str(customer_list)+""" order by  delivery_date desc""" ,  as_dict = 1)
		#print("delivery_note_list",delivery_note_list)
		return delivery_note_list

@frappe.whitelist()
def all_filters_applied(po_no,delivery_document_no,serial_no):
	user=frappe.db.get_value("User",{"name":frappe.session.user},"name")
	#print("user",user);
	user_name = frappe.db.sql("""select td.link_name from `tabContact` tc, `tabDynamic Link` td where td.link_doctype="Customer" and td.parent=tc.name and tc.user='"""+user+"""' """)
	#print("user_name",user_name);
	if(len(user_name)==1):
		for user_list in user_name:
			customer_list=user_list[0];
			delivery_note_list = frappe.db.sql("""select sn.item_name,sn.serial_no,sn.pch_coc,sn.pch_pressure_test,sn.pch_build_sheet,sn.pch1_combined_pdf,sn.pch_dnv_gl_product_certificate,sn.pch_eu_declaration,dn.po_no,sn.delivery_document_no,
	DATE_FORMAT(sn.delivery_date, '%d-%m-%Y') as delivery_date from `tabSerial No` sn ,`tabDelivery Note` dn where sn.delivery_document_type!="Null" and sn.delivery_document_type="Delivery Note"  and sn.delivery_document_no=dn.name and dn.po_no  LIKE '"""+po_no+"%""' and sn.serial_no  LIKE '"""+serial_no+"%""' and  sn.delivery_document_no  LIKE '"""+delivery_document_no+"%""' and sn.customer='"""+customer_list+"""' order by  delivery_date desc""" ,  as_dict = 1)
		#print("delivery_note_list",delivery_note_list)
		return delivery_note_list
	else:
		# List of tuple initialization
		contact_list = list(user_name)
		# using list comprehension
		list_primary_contact= [list_of_contact for t in contact_list for list_of_contact in t]
		customer_list=tuple(list_primary_contact);
		# printing output
		#print("customer_list",customer_list)
		delivery_note_list = frappe.db.sql("""select sn.item_name,sn.serial_no,sn.pch_coc,sn.pch_pressure_test,sn.pch_build_sheet,sn.pch1_combined_pdf,sn.pch_dnv_gl_product_certificate,sn.pch_eu_declaration,dn.po_no,sn.delivery_document_no,
	DATE_FORMAT(sn.delivery_date, '%d-%m-%Y') as delivery_date from `tabSerial No` sn ,`tabDelivery Note` dn where sn.delivery_document_type!="Null" and sn.delivery_document_type="Delivery Note"  and sn.delivery_document_no=dn.name and dn.po_no  LIKE '"""+po_no+"%""' and sn.serial_no  LIKE '"""+serial_no+"%""' and  sn.delivery_document_no  LIKE '"""+delivery_document_no+"%""' and sn.customer in """+str(customer_list)+""" order by  delivery_date desc""" ,  as_dict = 1)
		#print("delivery_note_list",delivery_note_list)
		return delivery_note_list


@frappe.whitelist()
def po_no(po_no):
	user=frappe.db.get_value("User",{"name":frappe.session.user},"name")
	#print("user",user);
	user_name = frappe.db.sql("""select td.link_name from `tabContact` tc, `tabDynamic Link` td where td.link_doctype="Customer" and td.parent=tc.name and tc.user='"""+user+"""' """)
	#print("user_name",user_name);
	if(len(user_name)==1):
		for user_list in user_name:
			customer_list=user_list[0];
			delivery_note_list = frappe.db.sql("""select sn.item_name,sn.serial_no,sn.pch_coc,sn.pch_pressure_test,sn.pch_build_sheet,sn.pch1_combined_pdf,sn.pch_dnv_gl_product_certificate,sn.pch_eu_declaration,dn.po_no,sn.delivery_document_no,
	DATE_FORMAT(sn.delivery_date, '%d-%m-%Y') as delivery_date from `tabSerial No` sn ,`tabDelivery Note` dn where sn.delivery_document_type!="Null" and sn.delivery_document_type="Delivery Note"  and sn.delivery_document_no=dn.name and dn.po_no  LIKE '"""+po_no+"%""' and sn.customer='"""+customer_list+"""' order by  delivery_date desc""" ,  as_dict = 1)
		#print("delivery_note_list",delivery_note_list)
		return delivery_note_list
	else:
		# List of tuple initialization
		contact_list = list(user_name)
		# using list comprehension
		list_primary_contact= [list_of_contact for t in contact_list for list_of_contact in t]
		customer_list=tuple(list_primary_contact);
		# printing output
		#print("customer_list",customer_list)
		delivery_note_list = frappe.db.sql("""select sn.item_name,sn.serial_no,sn.pch_coc,sn.pch_pressure_test,sn.pch_build_sheet,sn.pch1_combined_pdf,sn.pch_dnv_gl_product_certificate,sn.pch_eu_declaration,dn.po_no,sn.delivery_document_no,
	DATE_FORMAT(sn.delivery_date, '%d-%m-%Y') as delivery_date from `tabSerial No` sn ,`tabDelivery Note` dn where sn.delivery_document_type!="Null" and sn.delivery_document_type="Delivery Note"  and sn.delivery_document_no=dn.name and dn.po_no  LIKE '"""+po_no+"%""' and sn.customer in """+str(customer_list)+""" order by  delivery_date desc""" ,  as_dict = 1)
		#print("delivery_note_list",delivery_note_list)
		return delivery_note_list

@frappe.whitelist()
def delivery_document_no(delivery_document_no):
	user=frappe.db.get_value("User",{"name":frappe.session.user},"name")
	#print("user",user);
	user_name = frappe.db.sql("""select td.link_name from `tabContact` tc, `tabDynamic Link` td where td.link_doctype="Customer" and td.parent=tc.name and tc.user='"""+user+"""' """)
	#print("user_name",user_name);
	if(len(user_name)==1):
		for user_list in user_name:
			customer_list=user_list[0];
			delivery_note_list = frappe.db.sql("""select sn.item_name,sn.serial_no,sn.pch_coc,sn.pch_pressure_test,sn.pch_build_sheet,sn.pch1_combined_pdf,sn.pch_dnv_gl_product_certificate,sn.pch_eu_declaration,dn.po_no,sn.delivery_document_no,
	DATE_FORMAT(sn.delivery_date, '%d-%m-%Y') as delivery_date from `tabSerial No` sn ,`tabDelivery Note` dn where sn.delivery_document_type!="Null" and sn.delivery_document_type="Delivery Note"  and sn.delivery_document_no=dn.name and sn.delivery_document_no  LIKE '"""+delivery_document_no+"%""' and sn.customer='"""+customer_list+"""' order by  delivery_date desc""" ,  as_dict = 1)
		#print("delivery_note_list",delivery_note_list)
		return delivery_note_list
	else:
		# List of tuple initialization
		contact_list = list(user_name)
		# using list comprehension
		list_primary_contact= [list_of_contact for t in contact_list for list_of_contact in t]
		customer_list=tuple(list_primary_contact);
		# printing output
		#print("customer_list",customer_list)
		delivery_note_list = frappe.db.sql("""select sn.item_name,sn.serial_no,sn.pch_coc,sn.pch_pressure_test,sn.pch_build_sheet,sn.pch1_combined_pdf,sn.pch_dnv_gl_product_certificate,sn.pch_eu_declaration,dn.po_no,sn.delivery_document_no,
	DATE_FORMAT(sn.delivery_date, '%d-%m-%Y') as delivery_date from `tabSerial No` sn ,`tabDelivery Note` dn where sn.delivery_document_type!="Null" and sn.delivery_document_type="Delivery Note"  and sn.delivery_document_no=dn.name and sn.delivery_document_no  LIKE '"""+delivery_document_no+"%""' and sn.customer in """+str(customer_list)+""" order by  delivery_date desc""" ,  as_dict = 1)
		#print("delivery_note_list",delivery_note_list)
		return delivery_note_list

@frappe.whitelist()
def serial_no(serial_no):
	user=frappe.db.get_value("User",{"name":frappe.session.user},"name")
	#print("user",user);
	user_name = frappe.db.sql("""select td.link_name from `tabContact` tc, `tabDynamic Link` td where td.link_doctype="Customer" and td.parent=tc.name and tc.user='"""+user+"""' """)
	#print("user_name",user_name);
	if(len(user_name)==1):
		for user_list in user_name:
			customer_list=user_list[0];
			delivery_note_list = frappe.db.sql("""select sn.item_name,sn.serial_no,sn.pch_coc,sn.pch_pressure_test,sn.pch_build_sheet,sn.pch1_combined_pdf,sn.pch_dnv_gl_product_certificate,sn.pch_eu_declaration,dn.po_no,sn.delivery_document_no,
	DATE_FORMAT(sn.delivery_date, '%d-%m-%Y') as delivery_date from `tabSerial No` sn ,`tabDelivery Note` dn where sn.delivery_document_type!="Null" and sn.delivery_document_type="Delivery Note"  and sn.delivery_document_no=dn.name and sn.serial_no  LIKE '"""+serial_no+"%""' and sn.customer='"""+customer_list+"""' order by  delivery_date desc""" ,  as_dict = 1)
		#print("delivery_note_list",delivery_note_list)
		return delivery_note_list
	else:
		# List of tuple initialization
		contact_list = list(user_name)
		# using list comprehension
		list_primary_contact= [list_of_contact for t in contact_list for list_of_contact in t]
		customer_list=tuple(list_primary_contact);
		# printing output
		#print("customer_list",customer_list)
		delivery_note_list = frappe.db.sql("""select sn.item_name,sn.serial_no,sn.pch_coc,sn.pch_pressure_test,sn.pch_build_sheet,sn.pch1_combined_pdf,sn.pch_dnv_gl_product_certificate,sn.pch_eu_declaration,dn.po_no,sn.delivery_document_no,
	DATE_FORMAT(sn.delivery_date, '%d-%m-%Y') as delivery_date from `tabSerial No` sn ,`tabDelivery Note` dn where sn.delivery_document_type!="Null" and sn.delivery_document_type="Delivery Note"  and sn.delivery_document_no=dn.name and sn.serial_no  LIKE '"""+serial_no+"%""' and sn.customer in """+str(customer_list)+""" order by  delivery_date desc""" ,  as_dict = 1)
		#print("delivery_note_list",delivery_note_list)
		return delivery_note_list

@frappe.whitelist()
def api_user():
	user=frappe.db.get_value("User",{"name":frappe.session.user},"name")
	#print("user",user);
	user_name = frappe.db.sql("""select td.link_name from `tabContact` tc, `tabDynamic Link` td where td.link_doctype="Customer" and td.parent=tc.name and tc.user='"""+user+"""' """)
	#print("user_name",user_name);
	if(len(user_name)==1):
		for user_list in user_name:
			customer_list=user_list[0];
			delivery_note_list = frappe.db.sql("""select sn.item_name,sn.serial_no,sn.pch_coc,sn.pch_pressure_test,sn.pch_build_sheet,sn.pch1_combined_pdf,sn.pch_dnv_gl_product_certificate,sn.pch_eu_declaration,dn.po_no,sn.delivery_document_no,
	DATE_FORMAT(sn.delivery_date, '%d-%m-%Y') as delivery_date from `tabSerial No` sn ,`tabDelivery Note` dn where sn.delivery_document_type!="Null" and sn.delivery_document_type="Delivery Note"  and sn.delivery_document_no=dn.name and sn.customer='"""+customer_list+"""' order by  delivery_date desc""" ,  as_dict = 1)
		#print("delivery_note_list",delivery_note_list)
		return delivery_note_list
	else:
		# List of tuple initialization
		contact_list = list(user_name)
		# using list comprehension
		list_primary_contact= [list_of_contact for t in contact_list for list_of_contact in t]
		customer_list=tuple(list_primary_contact);
		# printing output
		#print("customer_list",customer_list)
		delivery_note_list = frappe.db.sql("""select sn.item_name,sn.serial_no,sn.pch_coc,sn.pch_pressure_test,sn.pch_build_sheet,sn.pch1_combined_pdf,sn.pch_dnv_gl_product_certificate,sn.pch_eu_declaration,dn.po_no,sn.delivery_document_no,
	DATE_FORMAT(sn.delivery_date, '%d-%m-%Y') as delivery_date from `tabSerial No` sn ,`tabDelivery Note` dn where sn.delivery_document_type!="Null" and sn.delivery_document_type="Delivery Note"  and sn.delivery_document_no=dn.name and sn.customer in """+str(customer_list)+""" order by  delivery_date desc""" ,  as_dict = 1)
		#print("delivery_note_list",delivery_note_list)
		return delivery_note_list


