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

@frappe.whitelist()
def item_name_asc():
	user=frappe.db.get_value("User",{"name":frappe.session.user},"name")
	#print("user",user);
	user_name = frappe.db.sql("""select td.link_name from `tabContact` tc, `tabDynamic Link` td where td.link_doctype="Customer" and td.parent=tc.name and tc.user='"""+user+"""' """)
	#print("user_name",user_name);
	if(len(user_name)==1):
		for user_list in user_name:
			customer_list=user_list[0];
			delivery_note_list = frappe.db.sql("""select sn.item_name,sn.serial_no,sn.pch_coc,sn.pch_pressure_test,sn.pch_build_sheet,sn.pch1_combined_pdf,sn.pch_dnv_gl_product_certificate,sn.pch_eu_declaration,dn.po_no,sn.delivery_document_no,
	DATE_FORMAT(sn.delivery_date, '%d-%m-%Y') as delivery_date from `tabSerial No` sn ,`tabDelivery Note` dn where sn.delivery_document_type!="Null" and sn.delivery_document_type="Delivery Note"  and sn.delivery_document_no=dn.name and sn.customer='"""+customer_list+"""' order by  sn.item_name asc""" ,  as_dict = 1)
		#print("delivery_note_list",delivery_note_list)
		return delivery_note_list

@frappe.whitelist()
def serial_no_asc():
	user=frappe.db.get_value("User",{"name":frappe.session.user},"name")
	#print("user",user);
	user_name = frappe.db.sql("""select td.link_name from `tabContact` tc, `tabDynamic Link` td where td.link_doctype="Customer" and td.parent=tc.name and tc.user='"""+user+"""' """)
	#print("user_name",user_name);
	if(len(user_name)==1):
		for user_list in user_name:
			customer_list=user_list[0];
			delivery_note_list = frappe.db.sql("""select sn.item_name,sn.serial_no,sn.pch_coc,sn.pch_pressure_test,sn.pch_build_sheet,sn.pch1_combined_pdf,sn.pch_dnv_gl_product_certificate,sn.pch_eu_declaration,dn.po_no,sn.delivery_document_no,
	DATE_FORMAT(sn.delivery_date, '%d-%m-%Y') as delivery_date from `tabSerial No` sn ,`tabDelivery Note` dn where sn.delivery_document_type!="Null" and sn.delivery_document_type="Delivery Note"  and sn.delivery_document_no=dn.name and sn.customer='"""+customer_list+"""' order by  sn.serial_no asc""" ,  as_dict = 1)
		#print("delivery_note_list",delivery_note_list)
		return delivery_note_list

@frappe.whitelist()
def po_no_asc():
	user=frappe.db.get_value("User",{"name":frappe.session.user},"name")
	#print("user",user);
	user_name = frappe.db.sql("""select td.link_name from `tabContact` tc, `tabDynamic Link` td where td.link_doctype="Customer" and td.parent=tc.name and tc.user='"""+user+"""' """)
	#print("user_name",user_name);
	if(len(user_name)==1):
		for user_list in user_name:
			customer_list=user_list[0];
			delivery_note_list = frappe.db.sql("""select sn.item_name,sn.serial_no,sn.pch_coc,sn.pch_pressure_test,sn.pch_build_sheet,sn.pch1_combined_pdf,sn.pch_dnv_gl_product_certificate,sn.pch_eu_declaration,dn.po_no,sn.delivery_document_no,
	DATE_FORMAT(sn.delivery_date, '%d-%m-%Y') as delivery_date from `tabSerial No` sn ,`tabDelivery Note` dn where sn.delivery_document_type!="Null" and sn.delivery_document_type="Delivery Note"  and sn.delivery_document_no=dn.name and sn.customer='"""+customer_list+"""' order by  dn.po_no asc""" ,  as_dict = 1)
		#print("delivery_note_list",delivery_note_list)
		return delivery_note_list

@frappe.whitelist()
def delivery_note_asc():
	user=frappe.db.get_value("User",{"name":frappe.session.user},"name")
	#print("user",user);
	user_name = frappe.db.sql("""select td.link_name from `tabContact` tc, `tabDynamic Link` td where td.link_doctype="Customer" and td.parent=tc.name and tc.user='"""+user+"""' """)
	#print("user_name",user_name);
	if(len(user_name)==1):
		for user_list in user_name:
			customer_list=user_list[0];
			delivery_note_list = frappe.db.sql("""select sn.item_name,sn.serial_no,sn.pch_coc,sn.pch_pressure_test,sn.pch_build_sheet,sn.pch1_combined_pdf,sn.pch_dnv_gl_product_certificate,sn.pch_eu_declaration,dn.po_no,sn.delivery_document_no,
	DATE_FORMAT(sn.delivery_date, '%d-%m-%Y') as delivery_date from `tabSerial No` sn ,`tabDelivery Note` dn where sn.delivery_document_type!="Null" and sn.delivery_document_type="Delivery Note"  and sn.delivery_document_no=dn.name and sn.customer='"""+customer_list+"""' order by  sn.delivery_document_no asc""" ,  as_dict = 1)
		#print("delivery_note_list",delivery_note_list)
		return delivery_note_list

@frappe.whitelist()
def delivery_date_asc():
	user=frappe.db.get_value("User",{"name":frappe.session.user},"name")
	#print("user",user);
	user_name = frappe.db.sql("""select td.link_name from `tabContact` tc, `tabDynamic Link` td where td.link_doctype="Customer" and td.parent=tc.name and tc.user='"""+user+"""' """)
	#print("user_name",user_name);
	if(len(user_name)==1):
		for user_list in user_name:
			customer_list=user_list[0];
			delivery_note_list = frappe.db.sql("""select sn.item_name,sn.serial_no,sn.pch_coc,sn.pch_pressure_test,sn.pch_build_sheet,sn.pch1_combined_pdf,sn.pch_dnv_gl_product_certificate,sn.pch_eu_declaration,dn.po_no,sn.delivery_document_no,
	DATE_FORMAT(sn.delivery_date, '%d-%m-%Y') as delivery_date from `tabSerial No` sn ,`tabDelivery Note` dn where sn.delivery_document_type!="Null" and sn.delivery_document_type="Delivery Note"  and sn.delivery_document_no=dn.name and sn.customer='"""+customer_list+"""' order by  delivery_date asc""" ,  as_dict = 1)
		#print("delivery_note_list",delivery_note_list)
		return delivery_note_list


@frappe.whitelist()
def delivery_serial_item_name_asc(delivery_document_no,serial_no):
	user=frappe.db.get_value("User",{"name":frappe.session.user},"name")
	#print("user",user);
	user_name = frappe.db.sql("""select td.link_name from `tabContact` tc, `tabDynamic Link` td where td.link_doctype="Customer" and td.parent=tc.name and tc.user='"""+user+"""' """)
	#print("user_name",user_name);
	if(len(user_name)==1):
		for user_list in user_name:
			customer_list=user_list[0];
			delivery_note_list = frappe.db.sql("""select sn.item_name,sn.serial_no,sn.pch_coc,sn.pch_pressure_test,sn.pch_build_sheet,sn.pch1_combined_pdf,sn.pch_dnv_gl_product_certificate,sn.pch_eu_declaration,dn.po_no,sn.delivery_document_no,
	DATE_FORMAT(sn.delivery_date, '%d-%m-%Y') as delivery_date from `tabSerial No` sn ,`tabDelivery Note` dn where sn.delivery_document_type!="Null" and sn.delivery_document_type="Delivery Note"  and sn.delivery_document_no=dn.name and sn.serial_no  LIKE '"""+serial_no+"%""' and  sn.delivery_document_no  LIKE '"""+delivery_document_no+"%""' and sn.customer='"""+customer_list+"""' order by  sn.item_name asc""" ,  as_dict = 1)
		#print("delivery_note_list",delivery_note_list)
		return delivery_note_list

@frappe.whitelist()
def delivery_serial_item_serial_asc(delivery_document_no,serial_no):
	user=frappe.db.get_value("User",{"name":frappe.session.user},"name")
	#print("user",user);
	user_name = frappe.db.sql("""select td.link_name from `tabContact` tc, `tabDynamic Link` td where td.link_doctype="Customer" and td.parent=tc.name and tc.user='"""+user+"""' """)
	#print("user_name",user_name);
	if(len(user_name)==1):
		for user_list in user_name:
			customer_list=user_list[0];
			delivery_note_list = frappe.db.sql("""select sn.item_name,sn.serial_no,sn.pch_coc,sn.pch_pressure_test,sn.pch_build_sheet,sn.pch1_combined_pdf,sn.pch_dnv_gl_product_certificate,sn.pch_eu_declaration,dn.po_no,sn.delivery_document_no,
	DATE_FORMAT(sn.delivery_date, '%d-%m-%Y') as delivery_date from `tabSerial No` sn ,`tabDelivery Note` dn where sn.delivery_document_type!="Null" and sn.delivery_document_type="Delivery Note"  and sn.delivery_document_no=dn.name and sn.serial_no  LIKE '"""+serial_no+"%""' and  sn.delivery_document_no  LIKE '"""+delivery_document_no+"%""' and sn.customer='"""+customer_list+"""' order by  sn.serial_no asc""" ,  as_dict = 1)
		#print("delivery_note_list",delivery_note_list)
		return delivery_note_list

@frappe.whitelist()
def delivery_serial_po_asc(delivery_document_no,serial_no):
	user=frappe.db.get_value("User",{"name":frappe.session.user},"name")
	#print("user",user);
	user_name = frappe.db.sql("""select td.link_name from `tabContact` tc, `tabDynamic Link` td where td.link_doctype="Customer" and td.parent=tc.name and tc.user='"""+user+"""' """)
	#print("user_name",user_name);
	if(len(user_name)==1):
		for user_list in user_name:
			customer_list=user_list[0];
			delivery_note_list = frappe.db.sql("""select sn.item_name,sn.serial_no,sn.pch_coc,sn.pch_pressure_test,sn.pch_build_sheet,sn.pch1_combined_pdf,sn.pch_dnv_gl_product_certificate,sn.pch_eu_declaration,dn.po_no,sn.delivery_document_no,
	DATE_FORMAT(sn.delivery_date, '%d-%m-%Y') as delivery_date from `tabSerial No` sn ,`tabDelivery Note` dn where sn.delivery_document_type!="Null" and sn.delivery_document_type="Delivery Note"  and sn.delivery_document_no=dn.name and sn.serial_no  LIKE '"""+serial_no+"%""' and  sn.delivery_document_no  LIKE '"""+delivery_document_no+"%""' and sn.customer='"""+customer_list+"""' order by  dn.po_no asc""" ,  as_dict = 1)
		#print("delivery_note_list",delivery_note_list)
		return delivery_note_list

@frappe.whitelist()
def delivery_serial_delivery_no_asc(delivery_document_no,serial_no):
	user=frappe.db.get_value("User",{"name":frappe.session.user},"name")
	#print("user",user);
	user_name = frappe.db.sql("""select td.link_name from `tabContact` tc, `tabDynamic Link` td where td.link_doctype="Customer" and td.parent=tc.name and tc.user='"""+user+"""' """)
	#print("user_name",user_name);
	if(len(user_name)==1):
		for user_list in user_name:
			customer_list=user_list[0];
			delivery_note_list = frappe.db.sql("""select sn.item_name,sn.serial_no,sn.pch_coc,sn.pch_pressure_test,sn.pch_build_sheet,sn.pch1_combined_pdf,sn.pch_dnv_gl_product_certificate,sn.pch_eu_declaration,dn.po_no,sn.delivery_document_no,
	DATE_FORMAT(sn.delivery_date, '%d-%m-%Y') as delivery_date from `tabSerial No` sn ,`tabDelivery Note` dn where sn.delivery_document_type!="Null" and sn.delivery_document_type="Delivery Note"  and sn.delivery_document_no=dn.name and sn.serial_no  LIKE '"""+serial_no+"%""' and  sn.delivery_document_no  LIKE '"""+delivery_document_no+"%""' and sn.customer='"""+customer_list+"""' order by  sn.delivery_document_no asc""" ,  as_dict = 1)
		#print("delivery_note_list",delivery_note_list)
		return delivery_note_list

@frappe.whitelist()
def delivery_serial_delivery_date_asc(delivery_document_no,serial_no):
	user=frappe.db.get_value("User",{"name":frappe.session.user},"name")
	#print("user",user);
	user_name = frappe.db.sql("""select td.link_name from `tabContact` tc, `tabDynamic Link` td where td.link_doctype="Customer" and td.parent=tc.name and tc.user='"""+user+"""' """)
	#print("user_name",user_name);
	if(len(user_name)==1):
		for user_list in user_name:
			customer_list=user_list[0];
			delivery_note_list = frappe.db.sql("""select sn.item_name,sn.serial_no,sn.pch_coc,sn.pch_pressure_test,sn.pch_build_sheet,sn.pch1_combined_pdf,sn.pch_dnv_gl_product_certificate,sn.pch_eu_declaration,dn.po_no,sn.delivery_document_no,
	DATE_FORMAT(sn.delivery_date, '%d-%m-%Y') as delivery_date from `tabSerial No` sn ,`tabDelivery Note` dn where sn.delivery_document_type!="Null" and sn.delivery_document_type="Delivery Note"  and sn.delivery_document_no=dn.name and sn.serial_no  LIKE '"""+serial_no+"%""' and  sn.delivery_document_no  LIKE '"""+delivery_document_no+"%""' and sn.customer='"""+customer_list+"""' order by  delivery_date asc""" ,  as_dict = 1)
		#print("delivery_note_list",delivery_note_list)
		return delivery_note_list

@frappe.whitelist()
def po_delivery_item_name_asc(po_no,delivery_document_no):
	user=frappe.db.get_value("User",{"name":frappe.session.user},"name")
	#print("user",user);
	user_name = frappe.db.sql("""select td.link_name from `tabContact` tc, `tabDynamic Link` td where td.link_doctype="Customer" and td.parent=tc.name and tc.user='"""+user+"""' """)
	#print("user_name",user_name);
	if(len(user_name)==1):
		for user_list in user_name:
			customer_list=user_list[0];
			delivery_note_list = frappe.db.sql("""select sn.item_name,sn.serial_no,sn.pch_coc,sn.pch_pressure_test,sn.pch_build_sheet,sn.pch1_combined_pdf,sn.pch_dnv_gl_product_certificate,sn.pch_eu_declaration,dn.po_no,sn.delivery_document_no,
	DATE_FORMAT(sn.delivery_date, '%d-%m-%Y') as delivery_date from `tabSerial No` sn ,`tabDelivery Note` dn where sn.delivery_document_type!="Null" and sn.delivery_document_type="Delivery Note"  and sn.delivery_document_no=dn.name and dn.po_no  LIKE '"""+po_no+"%""' and  sn.delivery_document_no  LIKE '"""+delivery_document_no+"%""' and sn.customer='"""+customer_list+"""' order by  sn.item_name asc""" ,  as_dict = 1)
		#print("delivery_note_list",delivery_note_list)
		return delivery_note_list

@frappe.whitelist()
def po_delivery_item_serial_asc(po_no,delivery_document_no):
	user=frappe.db.get_value("User",{"name":frappe.session.user},"name")
	#print("user",user);
	user_name = frappe.db.sql("""select td.link_name from `tabContact` tc, `tabDynamic Link` td where td.link_doctype="Customer" and td.parent=tc.name and tc.user='"""+user+"""' """)
	#print("user_name",user_name);
	if(len(user_name)==1):
		for user_list in user_name:
			customer_list=user_list[0];
			delivery_note_list = frappe.db.sql("""select sn.item_name,sn.serial_no,sn.pch_coc,sn.pch_pressure_test,sn.pch_build_sheet,sn.pch1_combined_pdf,sn.pch_dnv_gl_product_certificate,sn.pch_eu_declaration,dn.po_no,sn.delivery_document_no,
	DATE_FORMAT(sn.delivery_date, '%d-%m-%Y') as delivery_date from `tabSerial No` sn ,`tabDelivery Note` dn where sn.delivery_document_type!="Null" and sn.delivery_document_type="Delivery Note"  and sn.delivery_document_no=dn.name and dn.po_no  LIKE '"""+po_no+"%""' and  sn.delivery_document_no  LIKE '"""+delivery_document_no+"%""' and sn.customer='"""+customer_list+"""' order by  sn.serial_no asc""" ,  as_dict = 1)
		#print("delivery_note_list",delivery_note_list)
		return delivery_note_list

@frappe.whitelist()
def po_delivery_po_no_asc(po_no,delivery_document_no):
	user=frappe.db.get_value("User",{"name":frappe.session.user},"name")
	#print("user",user);
	user_name = frappe.db.sql("""select td.link_name from `tabContact` tc, `tabDynamic Link` td where td.link_doctype="Customer" and td.parent=tc.name and tc.user='"""+user+"""' """)
	#print("user_name",user_name);
	if(len(user_name)==1):
		for user_list in user_name:
			customer_list=user_list[0];
			delivery_note_list = frappe.db.sql("""select sn.item_name,sn.serial_no,sn.pch_coc,sn.pch_pressure_test,sn.pch_build_sheet,sn.pch1_combined_pdf,sn.pch_dnv_gl_product_certificate,sn.pch_eu_declaration,dn.po_no,sn.delivery_document_no,
	DATE_FORMAT(sn.delivery_date, '%d-%m-%Y') as delivery_date from `tabSerial No` sn ,`tabDelivery Note` dn where sn.delivery_document_type!="Null" and sn.delivery_document_type="Delivery Note"  and sn.delivery_document_no=dn.name and dn.po_no  LIKE '"""+po_no+"%""' and  sn.delivery_document_no  LIKE '"""+delivery_document_no+"%""' and sn.customer='"""+customer_list+"""' order by  dn.po_no asc""" ,  as_dict = 1)
		#print("delivery_note_list",delivery_note_list)
		return delivery_note_list

@frappe.whitelist()
def po_delivery_delivery_no_asc(po_no,delivery_document_no):
	user=frappe.db.get_value("User",{"name":frappe.session.user},"name")
	#print("user",user);
	user_name = frappe.db.sql("""select td.link_name from `tabContact` tc, `tabDynamic Link` td where td.link_doctype="Customer" and td.parent=tc.name and tc.user='"""+user+"""' """)
	#print("user_name",user_name);
	if(len(user_name)==1):
		for user_list in user_name:
			customer_list=user_list[0];
			delivery_note_list = frappe.db.sql("""select sn.item_name,sn.serial_no,sn.pch_coc,sn.pch_pressure_test,sn.pch_build_sheet,sn.pch1_combined_pdf,sn.pch_dnv_gl_product_certificate,sn.pch_eu_declaration,dn.po_no,sn.delivery_document_no,
	DATE_FORMAT(sn.delivery_date, '%d-%m-%Y') as delivery_date from `tabSerial No` sn ,`tabDelivery Note` dn where sn.delivery_document_type!="Null" and sn.delivery_document_type="Delivery Note"  and sn.delivery_document_no=dn.name and dn.po_no  LIKE '"""+po_no+"%""' and  sn.delivery_document_no  LIKE '"""+delivery_document_no+"%""' and sn.customer='"""+customer_list+"""' order by  sn.delivery_document_no asc""" ,  as_dict = 1)
		#print("delivery_note_list",delivery_note_list)
		return delivery_note_list

@frappe.whitelist()
def po_delivery_delivery_date_asc(po_no,delivery_document_no):
	user=frappe.db.get_value("User",{"name":frappe.session.user},"name")
	#print("user",user);
	user_name = frappe.db.sql("""select td.link_name from `tabContact` tc, `tabDynamic Link` td where td.link_doctype="Customer" and td.parent=tc.name and tc.user='"""+user+"""' """)
	#print("user_name",user_name);
	if(len(user_name)==1):
		for user_list in user_name:
			customer_list=user_list[0];
			delivery_note_list = frappe.db.sql("""select sn.item_name,sn.serial_no,sn.pch_coc,sn.pch_pressure_test,sn.pch_build_sheet,sn.pch1_combined_pdf,sn.pch_dnv_gl_product_certificate,sn.pch_eu_declaration,dn.po_no,sn.delivery_document_no,
	DATE_FORMAT(sn.delivery_date, '%d-%m-%Y') as delivery_date from `tabSerial No` sn ,`tabDelivery Note` dn where sn.delivery_document_type!="Null" and sn.delivery_document_type="Delivery Note"  and sn.delivery_document_no=dn.name and dn.po_no  LIKE '"""+po_no+"%""' and  sn.delivery_document_no  LIKE '"""+delivery_document_no+"%""' and sn.customer='"""+customer_list+"""' order by  delivery_date asc""" ,  as_dict = 1)
		#print("delivery_note_list",delivery_note_list)
		return delivery_note_list

@frappe.whitelist()
def po_serial_item_name_asc(po_no,serial_no):
	user=frappe.db.get_value("User",{"name":frappe.session.user},"name")
	#print("user",user);
	user_name = frappe.db.sql("""select td.link_name from `tabContact` tc, `tabDynamic Link` td where td.link_doctype="Customer" and td.parent=tc.name and tc.user='"""+user+"""' """)
	#print("user_name",user_name);
	if(len(user_name)==1):
		for user_list in user_name:
			customer_list=user_list[0];
			delivery_note_list = frappe.db.sql("""select sn.item_name,sn.serial_no,sn.pch_coc,sn.pch_pressure_test,sn.pch_build_sheet,sn.pch1_combined_pdf,sn.pch_dnv_gl_product_certificate,sn.pch_eu_declaration,dn.po_no,sn.delivery_document_no,
	DATE_FORMAT(sn.delivery_date, '%d-%m-%Y') as delivery_date from `tabSerial No` sn ,`tabDelivery Note` dn where sn.delivery_document_type!="Null" and sn.delivery_document_type="Delivery Note"  and sn.delivery_document_no=dn.name and dn.po_no  LIKE '"""+po_no+"%""' and  sn.serial_no  LIKE '"""+serial_no+"%""' and sn.customer='"""+customer_list+"""' order by  sn.item_name asc""" ,  as_dict = 1)
		#print("delivery_note_list",delivery_note_list)
		return delivery_note_list
@frappe.whitelist()
def po_serial_item_serial_asc(po_no,serial_no):
	user=frappe.db.get_value("User",{"name":frappe.session.user},"name")
	#print("user",user);
	user_name = frappe.db.sql("""select td.link_name from `tabContact` tc, `tabDynamic Link` td where td.link_doctype="Customer" and td.parent=tc.name and tc.user='"""+user+"""' """)
	#print("user_name",user_name);
	if(len(user_name)==1):
		for user_list in user_name:
			customer_list=user_list[0];
			delivery_note_list = frappe.db.sql("""select sn.item_name,sn.serial_no,sn.pch_coc,sn.pch_pressure_test,sn.pch_build_sheet,sn.pch1_combined_pdf,sn.pch_dnv_gl_product_certificate,sn.pch_eu_declaration,dn.po_no,sn.delivery_document_no,
	DATE_FORMAT(sn.delivery_date, '%d-%m-%Y') as delivery_date from `tabSerial No` sn ,`tabDelivery Note` dn where sn.delivery_document_type!="Null" and sn.delivery_document_type="Delivery Note"  and sn.delivery_document_no=dn.name and dn.po_no  LIKE '"""+po_no+"%""' and  sn.serial_no  LIKE '"""+serial_no+"%""' and sn.customer='"""+customer_list+"""' order by  sn.serial_no asc""" ,  as_dict = 1)
		#print("delivery_note_list",delivery_note_list)
		return delivery_note_list

@frappe.whitelist()
def po_serial_po_no_asc(po_no,serial_no):
	user=frappe.db.get_value("User",{"name":frappe.session.user},"name")
	#print("user",user);
	user_name = frappe.db.sql("""select td.link_name from `tabContact` tc, `tabDynamic Link` td where td.link_doctype="Customer" and td.parent=tc.name and tc.user='"""+user+"""' """)
	#print("user_name",user_name);
	if(len(user_name)==1):
		for user_list in user_name:
			customer_list=user_list[0];
			delivery_note_list = frappe.db.sql("""select sn.item_name,sn.serial_no,sn.pch_coc,sn.pch_pressure_test,sn.pch_build_sheet,sn.pch1_combined_pdf,sn.pch_dnv_gl_product_certificate,sn.pch_eu_declaration,dn.po_no,sn.delivery_document_no,
	DATE_FORMAT(sn.delivery_date, '%d-%m-%Y') as delivery_date from `tabSerial No` sn ,`tabDelivery Note` dn where sn.delivery_document_type!="Null" and sn.delivery_document_type="Delivery Note"  and sn.delivery_document_no=dn.name and dn.po_no  LIKE '"""+po_no+"%""' and  sn.serial_no  LIKE '"""+serial_no+"%""' and sn.customer='"""+customer_list+"""' order by  dn.po_no asc""" ,  as_dict = 1)
		#print("delivery_note_list",delivery_note_list)
		return delivery_note_list

@frappe.whitelist()
def po_serial_delivery_no_asc(po_no,serial_no):
	user=frappe.db.get_value("User",{"name":frappe.session.user},"name")
	#print("user",user);
	user_name = frappe.db.sql("""select td.link_name from `tabContact` tc, `tabDynamic Link` td where td.link_doctype="Customer" and td.parent=tc.name and tc.user='"""+user+"""' """)
	#print("user_name",user_name);
	if(len(user_name)==1):
		for user_list in user_name:
			customer_list=user_list[0];
			delivery_note_list = frappe.db.sql("""select sn.item_name,sn.serial_no,sn.pch_coc,sn.pch_pressure_test,sn.pch_build_sheet,sn.pch1_combined_pdf,sn.pch_dnv_gl_product_certificate,sn.pch_eu_declaration,dn.po_no,sn.delivery_document_no,
	DATE_FORMAT(sn.delivery_date, '%d-%m-%Y') as delivery_date from `tabSerial No` sn ,`tabDelivery Note` dn where sn.delivery_document_type!="Null" and sn.delivery_document_type="Delivery Note"  and sn.delivery_document_no=dn.name and dn.po_no  LIKE '"""+po_no+"%""' and  sn.serial_no  LIKE '"""+serial_no+"%""' and sn.customer='"""+customer_list+"""' order by  sn.delivery_document_no asc""" ,  as_dict = 1)
		#print("delivery_note_list",delivery_note_list)
		return delivery_note_list

@frappe.whitelist()
def po_serial_delivery_date_asc(po_no,serial_no):
	user=frappe.db.get_value("User",{"name":frappe.session.user},"name")
	#print("user",user);
	user_name = frappe.db.sql("""select td.link_name from `tabContact` tc, `tabDynamic Link` td where td.link_doctype="Customer" and td.parent=tc.name and tc.user='"""+user+"""' """)
	#print("user_name",user_name);
	if(len(user_name)==1):
		for user_list in user_name:
			customer_list=user_list[0];
			delivery_note_list = frappe.db.sql("""select sn.item_name,sn.serial_no,sn.pch_coc,sn.pch_pressure_test,sn.pch_build_sheet,sn.pch1_combined_pdf,sn.pch_dnv_gl_product_certificate,sn.pch_eu_declaration,dn.po_no,sn.delivery_document_no,
	DATE_FORMAT(sn.delivery_date, '%d-%m-%Y') as delivery_date from `tabSerial No` sn ,`tabDelivery Note` dn where sn.delivery_document_type!="Null" and sn.delivery_document_type="Delivery Note"  and sn.delivery_document_no=dn.name and dn.po_no  LIKE '"""+po_no+"%""' and  sn.serial_no  LIKE '"""+serial_no+"%""' and sn.customer='"""+customer_list+"""' order by  delivery_date asc""" ,  as_dict = 1)
		#print("delivery_note_list",delivery_note_list)
		return delivery_note_list

@frappe.whitelist()
def all_filters_applied_item_name_asc(po_no,delivery_document_no,serial_no):
	user=frappe.db.get_value("User",{"name":frappe.session.user},"name")
	#print("user",user);
	user_name = frappe.db.sql("""select td.link_name from `tabContact` tc, `tabDynamic Link` td where td.link_doctype="Customer" and td.parent=tc.name and tc.user='"""+user+"""' """)
	#print("user_name",user_name);
	if(len(user_name)==1):
		for user_list in user_name:
			customer_list=user_list[0];
			delivery_note_list = frappe.db.sql("""select sn.item_name,sn.serial_no,sn.pch_coc,sn.pch_pressure_test,sn.pch_build_sheet,sn.pch1_combined_pdf,sn.pch_dnv_gl_product_certificate,sn.pch_eu_declaration,dn.po_no,sn.delivery_document_no,
	DATE_FORMAT(sn.delivery_date, '%d-%m-%Y') as delivery_date from `tabSerial No` sn ,`tabDelivery Note` dn where sn.delivery_document_type!="Null" and sn.delivery_document_type="Delivery Note"  and sn.delivery_document_no=dn.name and dn.po_no  LIKE '"""+po_no+"%""' and sn.serial_no  LIKE '"""+serial_no+"%""' and  sn.delivery_document_no  LIKE '"""+delivery_document_no+"%""' and sn.customer='"""+customer_list+"""' order by  sn.item_name asc""" ,  as_dict = 1)
		#print("delivery_note_list",delivery_note_list)
		return delivery_note_list

@frappe.whitelist()
def all_filters_applied_item_serial_asc(po_no,delivery_document_no,serial_no):
	user=frappe.db.get_value("User",{"name":frappe.session.user},"name")
	#print("user",user);
	user_name = frappe.db.sql("""select td.link_name from `tabContact` tc, `tabDynamic Link` td where td.link_doctype="Customer" and td.parent=tc.name and tc.user='"""+user+"""' """)
	#print("user_name",user_name);
	if(len(user_name)==1):
		for user_list in user_name:
			customer_list=user_list[0];
			delivery_note_list = frappe.db.sql("""select sn.item_name,sn.serial_no,sn.pch_coc,sn.pch_pressure_test,sn.pch_build_sheet,sn.pch1_combined_pdf,sn.pch_dnv_gl_product_certificate,sn.pch_eu_declaration,dn.po_no,sn.delivery_document_no,
	DATE_FORMAT(sn.delivery_date, '%d-%m-%Y') as delivery_date from `tabSerial No` sn ,`tabDelivery Note` dn where sn.delivery_document_type!="Null" and sn.delivery_document_type="Delivery Note"  and sn.delivery_document_no=dn.name and dn.po_no  LIKE '"""+po_no+"%""' and sn.serial_no  LIKE '"""+serial_no+"%""' and  sn.delivery_document_no  LIKE '"""+delivery_document_no+"%""' and sn.customer='"""+customer_list+"""' order by  sn.serial_no asc""" ,  as_dict = 1)
		#print("delivery_note_list",delivery_note_list)
		return delivery_note_list

@frappe.whitelist()
def all_filters_applied_po_no_asc(po_no,delivery_document_no,serial_no):
	user=frappe.db.get_value("User",{"name":frappe.session.user},"name")
	#print("user",user);
	user_name = frappe.db.sql("""select td.link_name from `tabContact` tc, `tabDynamic Link` td where td.link_doctype="Customer" and td.parent=tc.name and tc.user='"""+user+"""' """)
	#print("user_name",user_name);
	if(len(user_name)==1):
		for user_list in user_name:
			customer_list=user_list[0];
			delivery_note_list = frappe.db.sql("""select sn.item_name,sn.serial_no,sn.pch_coc,sn.pch_pressure_test,sn.pch_build_sheet,sn.pch1_combined_pdf,sn.pch_dnv_gl_product_certificate,sn.pch_eu_declaration,dn.po_no,sn.delivery_document_no,
	DATE_FORMAT(sn.delivery_date, '%d-%m-%Y') as delivery_date from `tabSerial No` sn ,`tabDelivery Note` dn where sn.delivery_document_type!="Null" and sn.delivery_document_type="Delivery Note"  and sn.delivery_document_no=dn.name and dn.po_no  LIKE '"""+po_no+"%""' and sn.serial_no  LIKE '"""+serial_no+"%""' and  sn.delivery_document_no  LIKE '"""+delivery_document_no+"%""' and sn.customer='"""+customer_list+"""' order by  dn.po_no asc""" ,  as_dict = 1)
		#print("delivery_note_list",delivery_note_list)
		return delivery_note_list


@frappe.whitelist()
def all_filters_applied_delivery_no_asc(po_no,delivery_document_no,serial_no):
	user=frappe.db.get_value("User",{"name":frappe.session.user},"name")
	#print("user",user);
	user_name = frappe.db.sql("""select td.link_name from `tabContact` tc, `tabDynamic Link` td where td.link_doctype="Customer" and td.parent=tc.name and tc.user='"""+user+"""' """)
	#print("user_name",user_name);
	if(len(user_name)==1):
		for user_list in user_name:
			customer_list=user_list[0];
			delivery_note_list = frappe.db.sql("""select sn.item_name,sn.serial_no,sn.pch_coc,sn.pch_pressure_test,sn.pch_build_sheet,sn.pch1_combined_pdf,sn.pch_dnv_gl_product_certificate,sn.pch_eu_declaration,dn.po_no,sn.delivery_document_no,
	DATE_FORMAT(sn.delivery_date, '%d-%m-%Y') as delivery_date from `tabSerial No` sn ,`tabDelivery Note` dn where sn.delivery_document_type!="Null" and sn.delivery_document_type="Delivery Note"  and sn.delivery_document_no=dn.name and dn.po_no  LIKE '"""+po_no+"%""' and sn.serial_no  LIKE '"""+serial_no+"%""' and  sn.delivery_document_no  LIKE '"""+delivery_document_no+"%""' and sn.customer='"""+customer_list+"""' order by  sn.delivery_document_no asc""" ,  as_dict = 1)
		#print("delivery_note_list",delivery_note_list)
		return delivery_note_list

@frappe.whitelist()
def all_filters_applied_delivery_date_asc(po_no,delivery_document_no,serial_no):
	user=frappe.db.get_value("User",{"name":frappe.session.user},"name")
	#print("user",user);
	user_name = frappe.db.sql("""select td.link_name from `tabContact` tc, `tabDynamic Link` td where td.link_doctype="Customer" and td.parent=tc.name and tc.user='"""+user+"""' """)
	#print("user_name",user_name);
	if(len(user_name)==1):
		for user_list in user_name:
			customer_list=user_list[0];
			delivery_note_list = frappe.db.sql("""select sn.item_name,sn.serial_no,sn.pch_coc,sn.pch_pressure_test,sn.pch_build_sheet,sn.pch1_combined_pdf,sn.pch_dnv_gl_product_certificate,sn.pch_eu_declaration,dn.po_no,sn.delivery_document_no,
	DATE_FORMAT(sn.delivery_date, '%d-%m-%Y') as delivery_date from `tabSerial No` sn ,`tabDelivery Note` dn where sn.delivery_document_type!="Null" and sn.delivery_document_type="Delivery Note"  and sn.delivery_document_no=dn.name and dn.po_no  LIKE '"""+po_no+"%""' and sn.serial_no  LIKE '"""+serial_no+"%""' and  sn.delivery_document_no  LIKE '"""+delivery_document_no+"%""' and sn.customer='"""+customer_list+"""' order by  delivery_date asc""" ,  as_dict = 1)
		#print("delivery_note_list",delivery_note_list)
		return delivery_note_list

@frappe.whitelist()
def po_no_item_name_asc(po_no):
	user=frappe.db.get_value("User",{"name":frappe.session.user},"name")
	#print("user",user);
	user_name = frappe.db.sql("""select td.link_name from `tabContact` tc, `tabDynamic Link` td where td.link_doctype="Customer" and td.parent=tc.name and tc.user='"""+user+"""' """)
	#print("user_name",user_name);
	if(len(user_name)==1):
		for user_list in user_name:
			customer_list=user_list[0];
			delivery_note_list = frappe.db.sql("""select sn.item_name,sn.serial_no,sn.pch_coc,sn.pch_pressure_test,sn.pch_build_sheet,sn.pch1_combined_pdf,sn.pch_dnv_gl_product_certificate,sn.pch_eu_declaration,dn.po_no,sn.delivery_document_no,
	DATE_FORMAT(sn.delivery_date, '%d-%m-%Y') as delivery_date from `tabSerial No` sn ,`tabDelivery Note` dn where sn.delivery_document_type!="Null" and sn.delivery_document_type="Delivery Note"  and sn.delivery_document_no=dn.name and dn.po_no  LIKE '"""+po_no+"%""' and sn.customer='"""+customer_list+"""' order by  sn.item_name asc""" ,  as_dict = 1)
		#print("delivery_note_list",delivery_note_list)
		return delivery_note_list

@frappe.whitelist()
def po_no_item_serial_asc(po_no):
	user=frappe.db.get_value("User",{"name":frappe.session.user},"name")
	#print("user",user);
	user_name = frappe.db.sql("""select td.link_name from `tabContact` tc, `tabDynamic Link` td where td.link_doctype="Customer" and td.parent=tc.name and tc.user='"""+user+"""' """)
	#print("user_name",user_name);
	if(len(user_name)==1):
		for user_list in user_name:
			customer_list=user_list[0];
			delivery_note_list = frappe.db.sql("""select sn.item_name,sn.serial_no,sn.pch_coc,sn.pch_pressure_test,sn.pch_build_sheet,sn.pch1_combined_pdf,sn.pch_dnv_gl_product_certificate,sn.pch_eu_declaration,dn.po_no,sn.delivery_document_no,
	DATE_FORMAT(sn.delivery_date, '%d-%m-%Y') as delivery_date from `tabSerial No` sn ,`tabDelivery Note` dn where sn.delivery_document_type!="Null" and sn.delivery_document_type="Delivery Note"  and sn.delivery_document_no=dn.name and dn.po_no  LIKE '"""+po_no+"%""' and sn.customer='"""+customer_list+"""' order by  sn.serial_no asc""" ,  as_dict = 1)
		#print("delivery_note_list",delivery_note_list)
		return delivery_note_list

@frappe.whitelist()
def po_no_po_asc(po_no):
	user=frappe.db.get_value("User",{"name":frappe.session.user},"name")
	#print("user",user);
	user_name = frappe.db.sql("""select td.link_name from `tabContact` tc, `tabDynamic Link` td where td.link_doctype="Customer" and td.parent=tc.name and tc.user='"""+user+"""' """)
	#print("user_name",user_name);
	if(len(user_name)==1):
		for user_list in user_name:
			customer_list=user_list[0];
			delivery_note_list = frappe.db.sql("""select sn.item_name,sn.serial_no,sn.pch_coc,sn.pch_pressure_test,sn.pch_build_sheet,sn.pch1_combined_pdf,sn.pch_dnv_gl_product_certificate,sn.pch_eu_declaration,dn.po_no,sn.delivery_document_no,
	DATE_FORMAT(sn.delivery_date, '%d-%m-%Y') as delivery_date from `tabSerial No` sn ,`tabDelivery Note` dn where sn.delivery_document_type!="Null" and sn.delivery_document_type="Delivery Note"  and sn.delivery_document_no=dn.name and dn.po_no  LIKE '"""+po_no+"%""' and sn.customer='"""+customer_list+"""' order by  dn.po_no asc""" ,  as_dict = 1)
		#print("delivery_note_list",delivery_note_list)
		return delivery_note_list

@frappe.whitelist()
def po_no_delivery_no_asc(po_no):
	user=frappe.db.get_value("User",{"name":frappe.session.user},"name")
	#print("user",user);
	user_name = frappe.db.sql("""select td.link_name from `tabContact` tc, `tabDynamic Link` td where td.link_doctype="Customer" and td.parent=tc.name and tc.user='"""+user+"""' """)
	#print("user_name",user_name);
	if(len(user_name)==1):
		for user_list in user_name:
			customer_list=user_list[0];
			delivery_note_list = frappe.db.sql("""select sn.item_name,sn.serial_no,sn.pch_coc,sn.pch_pressure_test,sn.pch_build_sheet,sn.pch1_combined_pdf,sn.pch_dnv_gl_product_certificate,sn.pch_eu_declaration,dn.po_no,sn.delivery_document_no,
	DATE_FORMAT(sn.delivery_date, '%d-%m-%Y') as delivery_date from `tabSerial No` sn ,`tabDelivery Note` dn where sn.delivery_document_type!="Null" and sn.delivery_document_type="Delivery Note"  and sn.delivery_document_no=dn.name and dn.po_no  LIKE '"""+po_no+"%""' and sn.customer='"""+customer_list+"""' order by  sn.delivery_document_no asc""" ,  as_dict = 1)
		#print("delivery_note_list",delivery_note_list)
		return delivery_note_list

@frappe.whitelist()
def po_no_delivery_date_asc(po_no):
	user=frappe.db.get_value("User",{"name":frappe.session.user},"name")
	#print("user",user);
	user_name = frappe.db.sql("""select td.link_name from `tabContact` tc, `tabDynamic Link` td where td.link_doctype="Customer" and td.parent=tc.name and tc.user='"""+user+"""' """)
	#print("user_name",user_name);
	if(len(user_name)==1):
		for user_list in user_name:
			customer_list=user_list[0];
			delivery_note_list = frappe.db.sql("""select sn.item_name,sn.serial_no,sn.pch_coc,sn.pch_pressure_test,sn.pch_build_sheet,sn.pch1_combined_pdf,sn.pch_dnv_gl_product_certificate,sn.pch_eu_declaration,dn.po_no,sn.delivery_document_no,
	DATE_FORMAT(sn.delivery_date, '%d-%m-%Y') as delivery_date from `tabSerial No` sn ,`tabDelivery Note` dn where sn.delivery_document_type!="Null" and sn.delivery_document_type="Delivery Note"  and sn.delivery_document_no=dn.name and dn.po_no  LIKE '"""+po_no+"%""' and sn.customer='"""+customer_list+"""' order by  delivery_date asc""" ,  as_dict = 1)
		#print("delivery_note_list",delivery_note_list)
		return delivery_note_list

@frappe.whitelist()
def delivery_document_no_item_name_asc(delivery_document_no):
	user=frappe.db.get_value("User",{"name":frappe.session.user},"name")
	#print("user",user);
	user_name = frappe.db.sql("""select td.link_name from `tabContact` tc, `tabDynamic Link` td where td.link_doctype="Customer" and td.parent=tc.name and tc.user='"""+user+"""' """)
	#print("user_name",user_name);
	if(len(user_name)==1):
		for user_list in user_name:
			customer_list=user_list[0];
			delivery_note_list = frappe.db.sql("""select sn.item_name,sn.serial_no,sn.pch_coc,sn.pch_pressure_test,sn.pch_build_sheet,sn.pch1_combined_pdf,sn.pch_dnv_gl_product_certificate,sn.pch_eu_declaration,dn.po_no,sn.delivery_document_no,
	DATE_FORMAT(sn.delivery_date, '%d-%m-%Y') as delivery_date from `tabSerial No` sn ,`tabDelivery Note` dn where sn.delivery_document_type!="Null" and sn.delivery_document_type="Delivery Note"  and sn.delivery_document_no=dn.name and sn.delivery_document_no  LIKE '"""+delivery_document_no+"%""' and sn.customer='"""+customer_list+"""' order by  sn.item_name asc""" ,  as_dict = 1)
		#print("delivery_note_list",delivery_note_list)
		return delivery_note_list

@frappe.whitelist()
def delivery_document_no_item_serial_asc(delivery_document_no):
	user=frappe.db.get_value("User",{"name":frappe.session.user},"name")
	#print("user",user);
	user_name = frappe.db.sql("""select td.link_name from `tabContact` tc, `tabDynamic Link` td where td.link_doctype="Customer" and td.parent=tc.name and tc.user='"""+user+"""' """)
	#print("user_name",user_name);
	if(len(user_name)==1):
		for user_list in user_name:
			customer_list=user_list[0];
			delivery_note_list = frappe.db.sql("""select sn.item_name,sn.serial_no,sn.pch_coc,sn.pch_pressure_test,sn.pch_build_sheet,sn.pch1_combined_pdf,sn.pch_dnv_gl_product_certificate,sn.pch_eu_declaration,dn.po_no,sn.delivery_document_no,
	DATE_FORMAT(sn.delivery_date, '%d-%m-%Y') as delivery_date from `tabSerial No` sn ,`tabDelivery Note` dn where sn.delivery_document_type!="Null" and sn.delivery_document_type="Delivery Note"  and sn.delivery_document_no=dn.name and sn.delivery_document_no  LIKE '"""+delivery_document_no+"%""' and sn.customer='"""+customer_list+"""' order by  sn.serial_no asc""" ,  as_dict = 1)
		#print("delivery_note_list",delivery_note_list)
		return delivery_note_list

@frappe.whitelist()
def delivery_document_no_po_no_asc(delivery_document_no):
	user=frappe.db.get_value("User",{"name":frappe.session.user},"name")
	#print("user",user);
	user_name = frappe.db.sql("""select td.link_name from `tabContact` tc, `tabDynamic Link` td where td.link_doctype="Customer" and td.parent=tc.name and tc.user='"""+user+"""' """)
	#print("user_name",user_name);
	if(len(user_name)==1):
		for user_list in user_name:
			customer_list=user_list[0];
			delivery_note_list = frappe.db.sql("""select sn.item_name,sn.serial_no,sn.pch_coc,sn.pch_pressure_test,sn.pch_build_sheet,sn.pch1_combined_pdf,sn.pch_dnv_gl_product_certificate,sn.pch_eu_declaration,dn.po_no,sn.delivery_document_no,
	DATE_FORMAT(sn.delivery_date, '%d-%m-%Y') as delivery_date from `tabSerial No` sn ,`tabDelivery Note` dn where sn.delivery_document_type!="Null" and sn.delivery_document_type="Delivery Note"  and sn.delivery_document_no=dn.name and sn.delivery_document_no  LIKE '"""+delivery_document_no+"%""' and sn.customer='"""+customer_list+"""' order by  dn.po_no asc""" ,  as_dict = 1)
		#print("delivery_note_list",delivery_note_list)
		return delivery_note_list

@frappe.whitelist()
def delivery_document_no_delivery_no_asc(delivery_document_no):
	user=frappe.db.get_value("User",{"name":frappe.session.user},"name")
	#print("user",user);
	user_name = frappe.db.sql("""select td.link_name from `tabContact` tc, `tabDynamic Link` td where td.link_doctype="Customer" and td.parent=tc.name and tc.user='"""+user+"""' """)
	#print("user_name",user_name);
	if(len(user_name)==1):
		for user_list in user_name:
			customer_list=user_list[0];
			delivery_note_list = frappe.db.sql("""select sn.item_name,sn.serial_no,sn.pch_coc,sn.pch_pressure_test,sn.pch_build_sheet,sn.pch1_combined_pdf,sn.pch_dnv_gl_product_certificate,sn.pch_eu_declaration,dn.po_no,sn.delivery_document_no,
	DATE_FORMAT(sn.delivery_date, '%d-%m-%Y') as delivery_date from `tabSerial No` sn ,`tabDelivery Note` dn where sn.delivery_document_type!="Null" and sn.delivery_document_type="Delivery Note"  and sn.delivery_document_no=dn.name and sn.delivery_document_no  LIKE '"""+delivery_document_no+"%""' and sn.customer='"""+customer_list+"""' order by  sn.delivery_document_no asc""" ,  as_dict = 1)
		#print("delivery_note_list",delivery_note_list)
		return delivery_note_list

@frappe.whitelist()
def delivery_document_no_delivery_date_asc(delivery_document_no):
	user=frappe.db.get_value("User",{"name":frappe.session.user},"name")
	#print("user",user);
	user_name = frappe.db.sql("""select td.link_name from `tabContact` tc, `tabDynamic Link` td where td.link_doctype="Customer" and td.parent=tc.name and tc.user='"""+user+"""' """)
	#print("user_name",user_name);
	if(len(user_name)==1):
		for user_list in user_name:
			customer_list=user_list[0];
			delivery_note_list = frappe.db.sql("""select sn.item_name,sn.serial_no,sn.pch_coc,sn.pch_pressure_test,sn.pch_build_sheet,sn.pch1_combined_pdf,sn.pch_dnv_gl_product_certificate,sn.pch_eu_declaration,dn.po_no,sn.delivery_document_no,
	DATE_FORMAT(sn.delivery_date, '%d-%m-%Y') as delivery_date from `tabSerial No` sn ,`tabDelivery Note` dn where sn.delivery_document_type!="Null" and sn.delivery_document_type="Delivery Note"  and sn.delivery_document_no=dn.name and sn.delivery_document_no  LIKE '"""+delivery_document_no+"%""' and sn.customer='"""+customer_list+"""' order by  delivery_date asc""" ,  as_dict = 1)
		#print("delivery_note_list",delivery_note_list)
		return delivery_note_list

@frappe.whitelist()
def serial_no_item_name_asc(serial_no):
	user=frappe.db.get_value("User",{"name":frappe.session.user},"name")
	#print("user",user);
	user_name = frappe.db.sql("""select td.link_name from `tabContact` tc, `tabDynamic Link` td where td.link_doctype="Customer" and td.parent=tc.name and tc.user='"""+user+"""' """)
	#print("user_name",user_name);
	if(len(user_name)==1):
		for user_list in user_name:
			customer_list=user_list[0];
			delivery_note_list = frappe.db.sql("""select sn.item_name,sn.serial_no,sn.pch_coc,sn.pch_pressure_test,sn.pch_build_sheet,sn.pch1_combined_pdf,sn.pch_dnv_gl_product_certificate,sn.pch_eu_declaration,dn.po_no,sn.delivery_document_no,
	DATE_FORMAT(sn.delivery_date, '%d-%m-%Y') as delivery_date from `tabSerial No` sn ,`tabDelivery Note` dn where sn.delivery_document_type!="Null" and sn.delivery_document_type="Delivery Note"  and sn.delivery_document_no=dn.name and sn.serial_no  LIKE '"""+serial_no+"%""' and sn.customer='"""+customer_list+"""' order by  sn.item_name asc""" ,  as_dict = 1)
		#print("delivery_note_list",delivery_note_list)
		return delivery_note_list

@frappe.whitelist()
def serial_no_item_serial_asc(serial_no):
	user=frappe.db.get_value("User",{"name":frappe.session.user},"name")
	#print("user",user);
	user_name = frappe.db.sql("""select td.link_name from `tabContact` tc, `tabDynamic Link` td where td.link_doctype="Customer" and td.parent=tc.name and tc.user='"""+user+"""' """)
	#print("user_name",user_name);
	if(len(user_name)==1):
		for user_list in user_name:
			customer_list=user_list[0];
			delivery_note_list = frappe.db.sql("""select sn.item_name,sn.serial_no,sn.pch_coc,sn.pch_pressure_test,sn.pch_build_sheet,sn.pch1_combined_pdf,sn.pch_dnv_gl_product_certificate,sn.pch_eu_declaration,dn.po_no,sn.delivery_document_no,
	DATE_FORMAT(sn.delivery_date, '%d-%m-%Y') as delivery_date from `tabSerial No` sn ,`tabDelivery Note` dn where sn.delivery_document_type!="Null" and sn.delivery_document_type="Delivery Note"  and sn.delivery_document_no=dn.name and sn.serial_no  LIKE '"""+serial_no+"%""' and sn.customer='"""+customer_list+"""' order by  sn.serial_no asc""" ,  as_dict = 1)
		#print("delivery_note_list",delivery_note_list)
		return delivery_note_list

@frappe.whitelist()
def serial_no_po_no_asc(serial_no):
	user=frappe.db.get_value("User",{"name":frappe.session.user},"name")
	#print("user",user);
	user_name = frappe.db.sql("""select td.link_name from `tabContact` tc, `tabDynamic Link` td where td.link_doctype="Customer" and td.parent=tc.name and tc.user='"""+user+"""' """)
	#print("user_name",user_name);
	if(len(user_name)==1):
		for user_list in user_name:
			customer_list=user_list[0];
			delivery_note_list = frappe.db.sql("""select sn.item_name,sn.serial_no,sn.pch_coc,sn.pch_pressure_test,sn.pch_build_sheet,sn.pch1_combined_pdf,sn.pch_dnv_gl_product_certificate,sn.pch_eu_declaration,dn.po_no,sn.delivery_document_no,
	DATE_FORMAT(sn.delivery_date, '%d-%m-%Y') as delivery_date from `tabSerial No` sn ,`tabDelivery Note` dn where sn.delivery_document_type!="Null" and sn.delivery_document_type="Delivery Note"  and sn.delivery_document_no=dn.name and sn.serial_no  LIKE '"""+serial_no+"%""' and sn.customer='"""+customer_list+"""' order by  dn.po_no asc""" ,  as_dict = 1)
		#print("delivery_note_list",delivery_note_list)
		return delivery_note_list

@frappe.whitelist()
def serial_no_delivery_no_asc(serial_no):
	user=frappe.db.get_value("User",{"name":frappe.session.user},"name")
	#print("user",user);
	user_name = frappe.db.sql("""select td.link_name from `tabContact` tc, `tabDynamic Link` td where td.link_doctype="Customer" and td.parent=tc.name and tc.user='"""+user+"""' """)
	#print("user_name",user_name);
	if(len(user_name)==1):
		for user_list in user_name:
			customer_list=user_list[0];
			delivery_note_list = frappe.db.sql("""select sn.item_name,sn.serial_no,sn.pch_coc,sn.pch_pressure_test,sn.pch_build_sheet,sn.pch1_combined_pdf,sn.pch_dnv_gl_product_certificate,sn.pch_eu_declaration,dn.po_no,sn.delivery_document_no,
	DATE_FORMAT(sn.delivery_date, '%d-%m-%Y') as delivery_date from `tabSerial No` sn ,`tabDelivery Note` dn where sn.delivery_document_type!="Null" and sn.delivery_document_type="Delivery Note"  and sn.delivery_document_no=dn.name and sn.serial_no  LIKE '"""+serial_no+"%""' and sn.customer='"""+customer_list+"""' order by  sn.delivery_document_no asc""" ,  as_dict = 1)
		#print("delivery_note_list",delivery_note_list)
		return delivery_note_list

@frappe.whitelist()
def serial_no_delivery_date_asc(serial_no):
	user=frappe.db.get_value("User",{"name":frappe.session.user},"name")
	#print("user",user);
	user_name = frappe.db.sql("""select td.link_name from `tabContact` tc, `tabDynamic Link` td where td.link_doctype="Customer" and td.parent=tc.name and tc.user='"""+user+"""' """)
	#print("user_name",user_name);
	if(len(user_name)==1):
		for user_list in user_name:
			customer_list=user_list[0];
			delivery_note_list = frappe.db.sql("""select sn.item_name,sn.serial_no,sn.pch_coc,sn.pch_pressure_test,sn.pch_build_sheet,sn.pch1_combined_pdf,sn.pch_dnv_gl_product_certificate,sn.pch_eu_declaration,dn.po_no,sn.delivery_document_no,
	DATE_FORMAT(sn.delivery_date, '%d-%m-%Y') as delivery_date from `tabSerial No` sn ,`tabDelivery Note` dn where sn.delivery_document_type!="Null" and sn.delivery_document_type="Delivery Note"  and sn.delivery_document_no=dn.name and sn.serial_no  LIKE '"""+serial_no+"%""' and sn.customer='"""+customer_list+"""' order by  delivery_date asc""" ,  as_dict = 1)
		#print("delivery_note_list",delivery_note_list)
		return delivery_note_list

@frappe.whitelist()
def po_no_delivery_date_desc(po_no):
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

@frappe.whitelist()
def serial_no_delivery_date_desc(serial_no):
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

@frappe.whitelist()
def delivery_document_no_delivery_date_desc(delivery_document_no):
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

@frappe.whitelist()
def delivery_document_no_serial_no_desc(delivery_document_no):
	user=frappe.db.get_value("User",{"name":frappe.session.user},"name")
	#print("user",user);
	user_name = frappe.db.sql("""select td.link_name from `tabContact` tc, `tabDynamic Link` td where td.link_doctype="Customer" and td.parent=tc.name and tc.user='"""+user+"""' """)
	#print("user_name",user_name);
	if(len(user_name)==1):
		for user_list in user_name:
			customer_list=user_list[0];
			delivery_note_list = frappe.db.sql("""select sn.item_name,sn.serial_no,sn.pch_coc,sn.pch_pressure_test,sn.pch_build_sheet,sn.pch1_combined_pdf,sn.pch_dnv_gl_product_certificate,sn.pch_eu_declaration,dn.po_no,sn.delivery_document_no,
	DATE_FORMAT(sn.delivery_date, '%d-%m-%Y') as delivery_date from `tabSerial No` sn ,`tabDelivery Note` dn where sn.delivery_document_type!="Null" and sn.delivery_document_type="Delivery Note"  and sn.delivery_document_no=dn.name and sn.delivery_document_no  LIKE '"""+delivery_document_no+"%""' and sn.customer='"""+customer_list+"""' order by  sn.serial_no desc""" ,  as_dict = 1)
		#print("delivery_note_list",delivery_note_list)
		return delivery_note_list

@frappe.whitelist()
def delivery_document_no_item_name_desc(delivery_document_no):
	user=frappe.db.get_value("User",{"name":frappe.session.user},"name")
	#print("user",user);
	user_name = frappe.db.sql("""select td.link_name from `tabContact` tc, `tabDynamic Link` td where td.link_doctype="Customer" and td.parent=tc.name and tc.user='"""+user+"""' """)
	#print("user_name",user_name);
	if(len(user_name)==1):
		for user_list in user_name:
			customer_list=user_list[0];
			delivery_note_list = frappe.db.sql("""select sn.item_name,sn.serial_no,sn.pch_coc,sn.pch_pressure_test,sn.pch_build_sheet,sn.pch1_combined_pdf,sn.pch_dnv_gl_product_certificate,sn.pch_eu_declaration,dn.po_no,sn.delivery_document_no,
	DATE_FORMAT(sn.delivery_date, '%d-%m-%Y') as delivery_date from `tabSerial No` sn ,`tabDelivery Note` dn where sn.delivery_document_type!="Null" and sn.delivery_document_type="Delivery Note"  and sn.delivery_document_no=dn.name and sn.delivery_document_no  LIKE '"""+delivery_document_no+"%""' and sn.customer='"""+customer_list+"""' order by  sn.item_name desc""" ,  as_dict = 1)
		#print("delivery_note_list",delivery_note_list)
		return delivery_note_list

@frappe.whitelist()
def delivery_serial_delivery_date_desc(delivery_document_no,serial_no):
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

@frappe.whitelist()
def po_serial_delivery_date_desc(po_no,serial_no):
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

@frappe.whitelist()
def po_delivery_delivery_date_desc(po_no,delivery_document_no):
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

@frappe.whitelist()
def all_filters_applied_delivery_date_desc(po_no,delivery_document_no,serial_no):
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

@frappe.whitelist()
def delivery_date_desc():
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


#delivery no ascending api
@frappe.whitelist()
def po_no_delivery_no_asc(po_no):
	user=frappe.db.get_value("User",{"name":frappe.session.user},"name")
	#print("user",user);
	user_name = frappe.db.sql("""select td.link_name from `tabContact` tc, `tabDynamic Link` td where td.link_doctype="Customer" and td.parent=tc.name and tc.user='"""+user+"""' """)
	#print("user_name",user_name);
	if(len(user_name)==1):
		for user_list in user_name:
			customer_list=user_list[0];
			delivery_note_list = frappe.db.sql("""select sn.item_name,sn.serial_no,sn.pch_coc,sn.pch_pressure_test,sn.pch_build_sheet,sn.pch1_combined_pdf,sn.pch_dnv_gl_product_certificate,sn.pch_eu_declaration,dn.po_no,sn.delivery_document_no,
	DATE_FORMAT(sn.delivery_date, '%d-%m-%Y') as delivery_date from `tabSerial No` sn ,`tabDelivery Note` dn where sn.delivery_document_type!="Null" and sn.delivery_document_type="Delivery Note"  and sn.delivery_document_no=dn.name and dn.po_no  LIKE '"""+po_no+"%""' and sn.customer='"""+customer_list+"""' order by  sn.delivery_document_no asc""" ,  as_dict = 1)
		#print("delivery_note_list",delivery_note_list)
		return delivery_note_list

@frappe.whitelist()
def serial_no_delivery_no_asc(serial_no):
	user=frappe.db.get_value("User",{"name":frappe.session.user},"name")
	#print("user",user);
	user_name = frappe.db.sql("""select td.link_name from `tabContact` tc, `tabDynamic Link` td where td.link_doctype="Customer" and td.parent=tc.name and tc.user='"""+user+"""' """)
	#print("user_name",user_name);
	if(len(user_name)==1):
		for user_list in user_name:
			customer_list=user_list[0];
			delivery_note_list = frappe.db.sql("""select sn.item_name,sn.serial_no,sn.pch_coc,sn.pch_pressure_test,sn.pch_build_sheet,sn.pch1_combined_pdf,sn.pch_dnv_gl_product_certificate,sn.pch_eu_declaration,dn.po_no,sn.delivery_document_no,
	DATE_FORMAT(sn.delivery_date, '%d-%m-%Y') as delivery_date from `tabSerial No` sn ,`tabDelivery Note` dn where sn.delivery_document_type!="Null" and sn.delivery_document_type="Delivery Note"  and sn.delivery_document_no=dn.name and sn.serial_no  LIKE '"""+serial_no+"%""' and sn.customer='"""+customer_list+"""' order by  sn.delivery_document_no asc""" ,  as_dict = 1)
		#print("delivery_note_list",delivery_note_list)
		return delivery_note_list

@frappe.whitelist()
def delivery_document_no_delivery_no_asc(delivery_document_no):
	user=frappe.db.get_value("User",{"name":frappe.session.user},"name")
	#print("user",user);
	user_name = frappe.db.sql("""select td.link_name from `tabContact` tc, `tabDynamic Link` td where td.link_doctype="Customer" and td.parent=tc.name and tc.user='"""+user+"""' """)
	#print("user_name",user_name);
	if(len(user_name)==1):
		for user_list in user_name:
			customer_list=user_list[0];
			delivery_note_list = frappe.db.sql("""select sn.item_name,sn.serial_no,sn.pch_coc,sn.pch_pressure_test,sn.pch_build_sheet,sn.pch1_combined_pdf,sn.pch_dnv_gl_product_certificate,sn.pch_eu_declaration,dn.po_no,sn.delivery_document_no,
	DATE_FORMAT(sn.delivery_date, '%d-%m-%Y') as delivery_date from `tabSerial No` sn ,`tabDelivery Note` dn where sn.delivery_document_type!="Null" and sn.delivery_document_type="Delivery Note"  and sn.delivery_document_no=dn.name and sn.delivery_document_no  LIKE '"""+delivery_document_no+"%""' and sn.customer='"""+customer_list+"""' order by  sn.delivery_document_no asc""" ,  as_dict = 1)
		#print("delivery_note_list",delivery_note_list)
		return delivery_note_list

@frappe.whitelist()
def delivery_serial_delivery_no_asc(delivery_document_no,serial_no):
	user=frappe.db.get_value("User",{"name":frappe.session.user},"name")
	#print("user",user);
	user_name = frappe.db.sql("""select td.link_name from `tabContact` tc, `tabDynamic Link` td where td.link_doctype="Customer" and td.parent=tc.name and tc.user='"""+user+"""' """)
	#print("user_name",user_name);
	if(len(user_name)==1):
		for user_list in user_name:
			customer_list=user_list[0];
			delivery_note_list = frappe.db.sql("""select sn.item_name,sn.serial_no,sn.pch_coc,sn.pch_pressure_test,sn.pch_build_sheet,sn.pch1_combined_pdf,sn.pch_dnv_gl_product_certificate,sn.pch_eu_declaration,dn.po_no,sn.delivery_document_no,
	DATE_FORMAT(sn.delivery_date, '%d-%m-%Y') as delivery_date from `tabSerial No` sn ,`tabDelivery Note` dn where sn.delivery_document_type!="Null" and sn.delivery_document_type="Delivery Note"  and sn.delivery_document_no=dn.name and sn.serial_no  LIKE '"""+serial_no+"%""' and  sn.delivery_document_no  LIKE '"""+delivery_document_no+"%""' and sn.customer='"""+customer_list+"""' order by  sn.delivery_document_no asc""" ,  as_dict = 1)
		#print("delivery_note_list",delivery_note_list)
		return delivery_note_list

@frappe.whitelist()
def po_serial_delivery_no_asc(po_no,serial_no):
	user=frappe.db.get_value("User",{"name":frappe.session.user},"name")
	#print("user",user);
	user_name = frappe.db.sql("""select td.link_name from `tabContact` tc, `tabDynamic Link` td where td.link_doctype="Customer" and td.parent=tc.name and tc.user='"""+user+"""' """)
	#print("user_name",user_name);
	if(len(user_name)==1):
		for user_list in user_name:
			customer_list=user_list[0];
			delivery_note_list = frappe.db.sql("""select sn.item_name,sn.serial_no,sn.pch_coc,sn.pch_pressure_test,sn.pch_build_sheet,sn.pch1_combined_pdf,sn.pch_dnv_gl_product_certificate,sn.pch_eu_declaration,dn.po_no,sn.delivery_document_no,
	DATE_FORMAT(sn.delivery_date, '%d-%m-%Y') as delivery_date from `tabSerial No` sn ,`tabDelivery Note` dn where sn.delivery_document_type!="Null" and sn.delivery_document_type="Delivery Note"  and sn.delivery_document_no=dn.name and dn.po_no  LIKE '"""+po_no+"%""' and  sn.serial_no  LIKE '"""+serial_no+"%""' and sn.customer='"""+customer_list+"""' order by  sn.delivery_document_no asc""" ,  as_dict = 1)
		#print("delivery_note_list",delivery_note_list)
		return delivery_note_list

@frappe.whitelist()
def po_delivery_delivery_no_asc(po_no,delivery_document_no):
	user=frappe.db.get_value("User",{"name":frappe.session.user},"name")
	#print("user",user);
	user_name = frappe.db.sql("""select td.link_name from `tabContact` tc, `tabDynamic Link` td where td.link_doctype="Customer" and td.parent=tc.name and tc.user='"""+user+"""' """)
	#print("user_name",user_name);
	if(len(user_name)==1):
		for user_list in user_name:
			customer_list=user_list[0];
			delivery_note_list = frappe.db.sql("""select sn.item_name,sn.serial_no,sn.pch_coc,sn.pch_pressure_test,sn.pch_build_sheet,sn.pch1_combined_pdf,sn.pch_dnv_gl_product_certificate,sn.pch_eu_declaration,dn.po_no,sn.delivery_document_no,
	DATE_FORMAT(sn.delivery_date, '%d-%m-%Y') as delivery_date from `tabSerial No` sn ,`tabDelivery Note` dn where sn.delivery_document_type!="Null" and sn.delivery_document_type="Delivery Note"  and sn.delivery_document_no=dn.name and dn.po_no  LIKE '"""+po_no+"%""' and  sn.delivery_document_no  LIKE '"""+delivery_document_no+"%""' and sn.customer='"""+customer_list+"""' order by  sn.delivery_document_no asc""" ,  as_dict = 1)
		#print("delivery_note_list",delivery_note_list)
		return delivery_note_list

@frappe.whitelist()
def all_filters_applied_delivery_no_asc(po_no,delivery_document_no,serial_no):
	user=frappe.db.get_value("User",{"name":frappe.session.user},"name")
	#print("user",user);
	user_name = frappe.db.sql("""select td.link_name from `tabContact` tc, `tabDynamic Link` td where td.link_doctype="Customer" and td.parent=tc.name and tc.user='"""+user+"""' """)
	#print("user_name",user_name);
	if(len(user_name)==1):
		for user_list in user_name:
			customer_list=user_list[0];
			delivery_note_list = frappe.db.sql("""select sn.item_name,sn.serial_no,sn.pch_coc,sn.pch_pressure_test,sn.pch_build_sheet,sn.pch1_combined_pdf,sn.pch_dnv_gl_product_certificate,sn.pch_eu_declaration,dn.po_no,sn.delivery_document_no,
	DATE_FORMAT(sn.delivery_date, '%d-%m-%Y') as delivery_date from `tabSerial No` sn ,`tabDelivery Note` dn where sn.delivery_document_type!="Null" and sn.delivery_document_type="Delivery Note"  and sn.delivery_document_no=dn.name and dn.po_no  LIKE '"""+po_no+"%""' and sn.serial_no  LIKE '"""+serial_no+"%""' and  sn.delivery_document_no  LIKE '"""+delivery_document_no+"%""' and sn.customer='"""+customer_list+"""' order by  sn.delivery_document_no asc""" ,  as_dict = 1)
		#print("delivery_note_list",delivery_note_list)
		return delivery_note_list

@frappe.whitelist()
def delivery_no_asc():
	user=frappe.db.get_value("User",{"name":frappe.session.user},"name")
	#print("user",user);
	user_name = frappe.db.sql("""select td.link_name from `tabContact` tc, `tabDynamic Link` td where td.link_doctype="Customer" and td.parent=tc.name and tc.user='"""+user+"""' """)
	#print("user_name",user_name);
	if(len(user_name)==1):
		for user_list in user_name:
			customer_list=user_list[0];
			delivery_note_list = frappe.db.sql("""select sn.item_name,sn.serial_no,sn.pch_coc,sn.pch_pressure_test,sn.pch_build_sheet,sn.pch1_combined_pdf,sn.pch_dnv_gl_product_certificate,sn.pch_eu_declaration,dn.po_no,sn.delivery_document_no,
	DATE_FORMAT(sn.delivery_date, '%d-%m-%Y') as delivery_date from `tabSerial No` sn ,`tabDelivery Note` dn where sn.delivery_document_type!="Null" and sn.delivery_document_type="Delivery Note"  and sn.delivery_document_no=dn.name and sn.customer='"""+customer_list+"""' order by  sn.delivery_document_no asc""" ,  as_dict = 1)
		#print("delivery_note_list",delivery_note_list)
		return delivery_note_list

#delivery no descending api
@frappe.whitelist()
def po_no_delivery_no_desc(po_no):
	user=frappe.db.get_value("User",{"name":frappe.session.user},"name")
	#print("user",user);
	user_name = frappe.db.sql("""select td.link_name from `tabContact` tc, `tabDynamic Link` td where td.link_doctype="Customer" and td.parent=tc.name and tc.user='"""+user+"""' """)
	#print("user_name",user_name);
	if(len(user_name)==1):
		for user_list in user_name:
			customer_list=user_list[0];
			delivery_note_list = frappe.db.sql("""select sn.item_name,sn.serial_no,sn.pch_coc,sn.pch_pressure_test,sn.pch_build_sheet,sn.pch1_combined_pdf,sn.pch_dnv_gl_product_certificate,sn.pch_eu_declaration,dn.po_no,sn.delivery_document_no,
	DATE_FORMAT(sn.delivery_date, '%d-%m-%Y') as delivery_date from `tabSerial No` sn ,`tabDelivery Note` dn where sn.delivery_document_type!="Null" and sn.delivery_document_type="Delivery Note"  and sn.delivery_document_no=dn.name and dn.po_no  LIKE '"""+po_no+"%""' and sn.customer='"""+customer_list+"""' order by  sn.delivery_document_no desc""" ,  as_dict = 1)
		#print("delivery_note_list",delivery_note_list)
		return delivery_note_list

@frappe.whitelist()
def serial_no_delivery_no_desc(serial_no):
	user=frappe.db.get_value("User",{"name":frappe.session.user},"name")
	#print("user",user);
	user_name = frappe.db.sql("""select td.link_name from `tabContact` tc, `tabDynamic Link` td where td.link_doctype="Customer" and td.parent=tc.name and tc.user='"""+user+"""' """)
	#print("user_name",user_name);
	if(len(user_name)==1):
		for user_list in user_name:
			customer_list=user_list[0];
			delivery_note_list = frappe.db.sql("""select sn.item_name,sn.serial_no,sn.pch_coc,sn.pch_pressure_test,sn.pch_build_sheet,sn.pch1_combined_pdf,sn.pch_dnv_gl_product_certificate,sn.pch_eu_declaration,dn.po_no,sn.delivery_document_no,
	DATE_FORMAT(sn.delivery_date, '%d-%m-%Y') as delivery_date from `tabSerial No` sn ,`tabDelivery Note` dn where sn.delivery_document_type!="Null" and sn.delivery_document_type="Delivery Note"  and sn.delivery_document_no=dn.name and sn.serial_no  LIKE '"""+serial_no+"%""' and sn.customer='"""+customer_list+"""' order by  sn.delivery_document_no desc""" ,  as_dict = 1)
		#print("delivery_note_list",delivery_note_list)
		return delivery_note_list

@frappe.whitelist()
def delivery_document_no_delivery_no_desc(delivery_document_no):
	user=frappe.db.get_value("User",{"name":frappe.session.user},"name")
	#print("user",user);
	user_name = frappe.db.sql("""select td.link_name from `tabContact` tc, `tabDynamic Link` td where td.link_doctype="Customer" and td.parent=tc.name and tc.user='"""+user+"""' """)
	#print("user_name",user_name);
	if(len(user_name)==1):
		for user_list in user_name:
			customer_list=user_list[0];
			delivery_note_list = frappe.db.sql("""select sn.item_name,sn.serial_no,sn.pch_coc,sn.pch_pressure_test,sn.pch_build_sheet,sn.pch1_combined_pdf,sn.pch_dnv_gl_product_certificate,sn.pch_eu_declaration,dn.po_no,sn.delivery_document_no,
	DATE_FORMAT(sn.delivery_date, '%d-%m-%Y') as delivery_date from `tabSerial No` sn ,`tabDelivery Note` dn where sn.delivery_document_type!="Null" and sn.delivery_document_type="Delivery Note"  and sn.delivery_document_no=dn.name and sn.delivery_document_no  LIKE '"""+delivery_document_no+"%""' and sn.customer='"""+customer_list+"""' order by  sn.delivery_document_no desc""" ,  as_dict = 1)
		#print("delivery_note_list",delivery_note_list)
		return delivery_note_list

@frappe.whitelist()
def delivery_serial_delivery_no_desc(delivery_document_no,serial_no):
	user=frappe.db.get_value("User",{"name":frappe.session.user},"name")
	#print("user",user);
	user_name = frappe.db.sql("""select td.link_name from `tabContact` tc, `tabDynamic Link` td where td.link_doctype="Customer" and td.parent=tc.name and tc.user='"""+user+"""' """)
	#print("user_name",user_name);
	if(len(user_name)==1):
		for user_list in user_name:
			customer_list=user_list[0];
			delivery_note_list = frappe.db.sql("""select sn.item_name,sn.serial_no,sn.pch_coc,sn.pch_pressure_test,sn.pch_build_sheet,sn.pch1_combined_pdf,sn.pch_dnv_gl_product_certificate,sn.pch_eu_declaration,dn.po_no,sn.delivery_document_no,
	DATE_FORMAT(sn.delivery_date, '%d-%m-%Y') as delivery_date from `tabSerial No` sn ,`tabDelivery Note` dn where sn.delivery_document_type!="Null" and sn.delivery_document_type="Delivery Note"  and sn.delivery_document_no=dn.name and sn.serial_no  LIKE '"""+serial_no+"%""' and  sn.delivery_document_no  LIKE '"""+delivery_document_no+"%""' and sn.customer='"""+customer_list+"""' order by  sn.delivery_document_no desc""" ,  as_dict = 1)
		#print("delivery_note_list",delivery_note_list)
		return delivery_note_list

@frappe.whitelist()
def po_serial_delivery_no_desc(po_no,serial_no):
	user=frappe.db.get_value("User",{"name":frappe.session.user},"name")
	#print("user",user);
	user_name = frappe.db.sql("""select td.link_name from `tabContact` tc, `tabDynamic Link` td where td.link_doctype="Customer" and td.parent=tc.name and tc.user='"""+user+"""' """)
	#print("user_name",user_name);
	if(len(user_name)==1):
		for user_list in user_name:
			customer_list=user_list[0];
			delivery_note_list = frappe.db.sql("""select sn.item_name,sn.serial_no,sn.pch_coc,sn.pch_pressure_test,sn.pch_build_sheet,sn.pch1_combined_pdf,sn.pch_dnv_gl_product_certificate,sn.pch_eu_declaration,dn.po_no,sn.delivery_document_no,
	DATE_FORMAT(sn.delivery_date, '%d-%m-%Y') as delivery_date from `tabSerial No` sn ,`tabDelivery Note` dn where sn.delivery_document_type!="Null" and sn.delivery_document_type="Delivery Note"  and sn.delivery_document_no=dn.name and dn.po_no  LIKE '"""+po_no+"%""' and  sn.serial_no  LIKE '"""+serial_no+"%""' and sn.customer='"""+customer_list+"""' order by  sn.delivery_document_no desc""" ,  as_dict = 1)
		#print("delivery_note_list",delivery_note_list)
		return delivery_note_list

@frappe.whitelist()
def po_delivery_delivery_no_desc(po_no,delivery_document_no):
	user=frappe.db.get_value("User",{"name":frappe.session.user},"name")
	#print("user",user);
	user_name = frappe.db.sql("""select td.link_name from `tabContact` tc, `tabDynamic Link` td where td.link_doctype="Customer" and td.parent=tc.name and tc.user='"""+user+"""' """)
	#print("user_name",user_name);
	if(len(user_name)==1):
		for user_list in user_name:
			customer_list=user_list[0];
			delivery_note_list = frappe.db.sql("""select sn.item_name,sn.serial_no,sn.pch_coc,sn.pch_pressure_test,sn.pch_build_sheet,sn.pch1_combined_pdf,sn.pch_dnv_gl_product_certificate,sn.pch_eu_declaration,dn.po_no,sn.delivery_document_no,
	DATE_FORMAT(sn.delivery_date, '%d-%m-%Y') as delivery_date from `tabSerial No` sn ,`tabDelivery Note` dn where sn.delivery_document_type!="Null" and sn.delivery_document_type="Delivery Note"  and sn.delivery_document_no=dn.name and dn.po_no  LIKE '"""+po_no+"%""' and  sn.delivery_document_no  LIKE '"""+delivery_document_no+"%""' and sn.customer='"""+customer_list+"""' order by  sn.delivery_document_no desc""" ,  as_dict = 1)
		#print("delivery_note_list",delivery_note_list)
		return delivery_note_list

@frappe.whitelist()
def all_filters_applied_delivery_no_desc(po_no,delivery_document_no,serial_no):
	user=frappe.db.get_value("User",{"name":frappe.session.user},"name")
	#print("user",user);
	user_name = frappe.db.sql("""select td.link_name from `tabContact` tc, `tabDynamic Link` td where td.link_doctype="Customer" and td.parent=tc.name and tc.user='"""+user+"""' """)
	#print("user_name",user_name);
	if(len(user_name)==1):
		for user_list in user_name:
			customer_list=user_list[0];
			delivery_note_list = frappe.db.sql("""select sn.item_name,sn.serial_no,sn.pch_coc,sn.pch_pressure_test,sn.pch_build_sheet,sn.pch1_combined_pdf,sn.pch_dnv_gl_product_certificate,sn.pch_eu_declaration,dn.po_no,sn.delivery_document_no,
	DATE_FORMAT(sn.delivery_date, '%d-%m-%Y') as delivery_date from `tabSerial No` sn ,`tabDelivery Note` dn where sn.delivery_document_type!="Null" and sn.delivery_document_type="Delivery Note"  and sn.delivery_document_no=dn.name and dn.po_no  LIKE '"""+po_no+"%""' and sn.serial_no  LIKE '"""+serial_no+"%""' and  sn.delivery_document_no  LIKE '"""+delivery_document_no+"%""' and sn.customer='"""+customer_list+"""' order by  sn.delivery_document_no desc""" ,  as_dict = 1)
		#print("delivery_note_list",delivery_note_list)
		return delivery_note_list

@frappe.whitelist()
def delivery_no_desc():
	user=frappe.db.get_value("User",{"name":frappe.session.user},"name")
	#print("user",user);
	user_name = frappe.db.sql("""select td.link_name from `tabContact` tc, `tabDynamic Link` td where td.link_doctype="Customer" and td.parent=tc.name and tc.user='"""+user+"""' """)
	#print("user_name",user_name);
	if(len(user_name)==1):
		for user_list in user_name:
			customer_list=user_list[0];
			delivery_note_list = frappe.db.sql("""select sn.item_name,sn.serial_no,sn.pch_coc,sn.pch_pressure_test,sn.pch_build_sheet,sn.pch1_combined_pdf,sn.pch_dnv_gl_product_certificate,sn.pch_eu_declaration,dn.po_no,sn.delivery_document_no,
	DATE_FORMAT(sn.delivery_date, '%d-%m-%Y') as delivery_date from `tabSerial No` sn ,`tabDelivery Note` dn where sn.delivery_document_type!="Null" and sn.delivery_document_type="Delivery Note"  and sn.delivery_document_no=dn.name and sn.customer='"""+customer_list+"""' order by  sn.delivery_document_no desc""" ,  as_dict = 1)
		#print("delivery_note_list",delivery_note_list)
		return delivery_note_list


#customer po
@frappe.whitelist()
def po_no_customer_po_desc(po_no):
	user=frappe.db.get_value("User",{"name":frappe.session.user},"name")
	#print("user",user);
	user_name = frappe.db.sql("""select td.link_name from `tabContact` tc, `tabDynamic Link` td where td.link_doctype="Customer" and td.parent=tc.name and tc.user='"""+user+"""' """)
	#print("user_name",user_name);
	if(len(user_name)==1):
		for user_list in user_name:
			customer_list=user_list[0];
			delivery_note_list = frappe.db.sql("""select sn.item_name,sn.serial_no,sn.pch_coc,sn.pch_pressure_test,sn.pch_build_sheet,sn.pch1_combined_pdf,sn.pch_dnv_gl_product_certificate,sn.pch_eu_declaration,dn.po_no,sn.delivery_document_no,
	DATE_FORMAT(sn.delivery_date, '%d-%m-%Y') as delivery_date from `tabSerial No` sn ,`tabDelivery Note` dn where sn.delivery_document_type!="Null" and sn.delivery_document_type="Delivery Note"  and sn.delivery_document_no=dn.name and dn.po_no  LIKE '"""+po_no+"%""' and sn.customer='"""+customer_list+"""' order by  dn.po_no desc""" ,  as_dict = 1)
		#print("delivery_note_list",delivery_note_list)
		return delivery_note_list

@frappe.whitelist()
def serial_no_customer_po_desc(serial_no):
	user=frappe.db.get_value("User",{"name":frappe.session.user},"name")
	#print("user",user);
	user_name = frappe.db.sql("""select td.link_name from `tabContact` tc, `tabDynamic Link` td where td.link_doctype="Customer" and td.parent=tc.name and tc.user='"""+user+"""' """)
	#print("user_name",user_name);
	if(len(user_name)==1):
		for user_list in user_name:
			customer_list=user_list[0];
			delivery_note_list = frappe.db.sql("""select sn.item_name,sn.serial_no,sn.pch_coc,sn.pch_pressure_test,sn.pch_build_sheet,sn.pch1_combined_pdf,sn.pch_dnv_gl_product_certificate,sn.pch_eu_declaration,dn.po_no,sn.delivery_document_no,
	DATE_FORMAT(sn.delivery_date, '%d-%m-%Y') as delivery_date from `tabSerial No` sn ,`tabDelivery Note` dn where sn.delivery_document_type!="Null" and sn.delivery_document_type="Delivery Note"  and sn.delivery_document_no=dn.name and sn.serial_no  LIKE '"""+serial_no+"%""' and sn.customer='"""+customer_list+"""' order by dn.po_no desc""" ,  as_dict = 1)
		#print("delivery_note_list",delivery_note_list)
		return delivery_note_list

@frappe.whitelist()
def delivery_document_no_customer_po_desc(delivery_document_no):
	user=frappe.db.get_value("User",{"name":frappe.session.user},"name")
	#print("user",user);
	user_name = frappe.db.sql("""select td.link_name from `tabContact` tc, `tabDynamic Link` td where td.link_doctype="Customer" and td.parent=tc.name and tc.user='"""+user+"""' """)
	#print("user_name",user_name);
	if(len(user_name)==1):
		for user_list in user_name:
			customer_list=user_list[0];
			delivery_note_list = frappe.db.sql("""select sn.item_name,sn.serial_no,sn.pch_coc,sn.pch_pressure_test,sn.pch_build_sheet,sn.pch1_combined_pdf,sn.pch_dnv_gl_product_certificate,sn.pch_eu_declaration,dn.po_no,sn.delivery_document_no,
	DATE_FORMAT(sn.delivery_date, '%d-%m-%Y') as delivery_date from `tabSerial No` sn ,`tabDelivery Note` dn where sn.delivery_document_type!="Null" and sn.delivery_document_type="Delivery Note"  and sn.delivery_document_no=dn.name and sn.delivery_document_no  LIKE '"""+delivery_document_no+"%""' and sn.customer='"""+customer_list+"""' order by  dn.po_no desc""" ,  as_dict = 1)
		#print("delivery_note_list",delivery_note_list)
		return delivery_note_list

@frappe.whitelist()
def delivery_serial_customer_po_desc(delivery_document_no,serial_no):
	user=frappe.db.get_value("User",{"name":frappe.session.user},"name")
	#print("user",user);
	user_name = frappe.db.sql("""select td.link_name from `tabContact` tc, `tabDynamic Link` td where td.link_doctype="Customer" and td.parent=tc.name and tc.user='"""+user+"""' """)
	#print("user_name",user_name);
	if(len(user_name)==1):
		for user_list in user_name:
			customer_list=user_list[0];
			delivery_note_list = frappe.db.sql("""select sn.item_name,sn.serial_no,sn.pch_coc,sn.pch_pressure_test,sn.pch_build_sheet,sn.pch1_combined_pdf,sn.pch_dnv_gl_product_certificate,sn.pch_eu_declaration,dn.po_no,sn.delivery_document_no,
	DATE_FORMAT(sn.delivery_date, '%d-%m-%Y') as delivery_date from `tabSerial No` sn ,`tabDelivery Note` dn where sn.delivery_document_type!="Null" and sn.delivery_document_type="Delivery Note"  and sn.delivery_document_no=dn.name and sn.serial_no  LIKE '"""+serial_no+"%""' and  sn.delivery_document_no  LIKE '"""+delivery_document_no+"%""' and sn.customer='"""+customer_list+"""' order by  dn.po_no desc""" ,  as_dict = 1)
		#print("delivery_note_list",delivery_note_list)
		return delivery_note_list

@frappe.whitelist()
def po_serial_customer_po_desc(po_no,serial_no):
	user=frappe.db.get_value("User",{"name":frappe.session.user},"name")
	#print("user",user);
	user_name = frappe.db.sql("""select td.link_name from `tabContact` tc, `tabDynamic Link` td where td.link_doctype="Customer" and td.parent=tc.name and tc.user='"""+user+"""' """)
	#print("user_name",user_name);
	if(len(user_name)==1):
		for user_list in user_name:
			customer_list=user_list[0];
			delivery_note_list = frappe.db.sql("""select sn.item_name,sn.serial_no,sn.pch_coc,sn.pch_pressure_test,sn.pch_build_sheet,sn.pch1_combined_pdf,sn.pch_dnv_gl_product_certificate,sn.pch_eu_declaration,dn.po_no,sn.delivery_document_no,
	DATE_FORMAT(sn.delivery_date, '%d-%m-%Y') as delivery_date from `tabSerial No` sn ,`tabDelivery Note` dn where sn.delivery_document_type!="Null" and sn.delivery_document_type="Delivery Note"  and sn.delivery_document_no=dn.name and dn.po_no  LIKE '"""+po_no+"%""' and  sn.serial_no  LIKE '"""+serial_no+"%""' and sn.customer='"""+customer_list+"""' order by  dn.po_no desc""" ,  as_dict = 1)
		#print("delivery_note_list",delivery_note_list)
		return delivery_note_list

@frappe.whitelist()
def po_delivery_customer_po_desc(po_no,delivery_document_no):
	user=frappe.db.get_value("User",{"name":frappe.session.user},"name")
	#print("user",user);
	user_name = frappe.db.sql("""select td.link_name from `tabContact` tc, `tabDynamic Link` td where td.link_doctype="Customer" and td.parent=tc.name and tc.user='"""+user+"""' """)
	#print("user_name",user_name);
	if(len(user_name)==1):
		for user_list in user_name:
			customer_list=user_list[0];
			delivery_note_list = frappe.db.sql("""select sn.item_name,sn.serial_no,sn.pch_coc,sn.pch_pressure_test,sn.pch_build_sheet,sn.pch1_combined_pdf,sn.pch_dnv_gl_product_certificate,sn.pch_eu_declaration,dn.po_no,sn.delivery_document_no,
	DATE_FORMAT(sn.delivery_date, '%d-%m-%Y') as delivery_date from `tabSerial No` sn ,`tabDelivery Note` dn where sn.delivery_document_type!="Null" and sn.delivery_document_type="Delivery Note"  and sn.delivery_document_no=dn.name and dn.po_no  LIKE '"""+po_no+"%""' and  sn.delivery_document_no  LIKE '"""+delivery_document_no+"%""' and sn.customer='"""+customer_list+"""' order by  dn.po_no desc""" ,  as_dict = 1)
		#print("delivery_note_list",delivery_note_list)
		return delivery_note_list

@frappe.whitelist()
def all_filters_applied_customer_po_desc(po_no,delivery_document_no,serial_no):
	user=frappe.db.get_value("User",{"name":frappe.session.user},"name")
	#print("user",user);
	user_name = frappe.db.sql("""select td.link_name from `tabContact` tc, `tabDynamic Link` td where td.link_doctype="Customer" and td.parent=tc.name and tc.user='"""+user+"""' """)
	#print("user_name",user_name);
	if(len(user_name)==1):
		for user_list in user_name:
			customer_list=user_list[0];
			delivery_note_list = frappe.db.sql("""select sn.item_name,sn.serial_no,sn.pch_coc,sn.pch_pressure_test,sn.pch_build_sheet,sn.pch1_combined_pdf,sn.pch_dnv_gl_product_certificate,sn.pch_eu_declaration,dn.po_no,sn.delivery_document_no,
	DATE_FORMAT(sn.delivery_date, '%d-%m-%Y') as delivery_date from `tabSerial No` sn ,`tabDelivery Note` dn where sn.delivery_document_type!="Null" and sn.delivery_document_type="Delivery Note"  and sn.delivery_document_no=dn.name and dn.po_no  LIKE '"""+po_no+"%""' and sn.serial_no  LIKE '"""+serial_no+"%""' and  sn.delivery_document_no  LIKE '"""+delivery_document_no+"%""' and sn.customer='"""+customer_list+"""' order by  dn.po_no desc""" ,  as_dict = 1)
		#print("delivery_note_list",delivery_note_list)
		return delivery_note_list

@frappe.whitelist()
def customer_po_desc():
	user=frappe.db.get_value("User",{"name":frappe.session.user},"name")
	#print("user",user);
	user_name = frappe.db.sql("""select td.link_name from `tabContact` tc, `tabDynamic Link` td where td.link_doctype="Customer" and td.parent=tc.name and tc.user='"""+user+"""' """)
	#print("user_name",user_name);
	if(len(user_name)==1):
		for user_list in user_name:
			customer_list=user_list[0];
			delivery_note_list = frappe.db.sql("""select sn.item_name,sn.serial_no,sn.pch_coc,sn.pch_pressure_test,sn.pch_build_sheet,sn.pch1_combined_pdf,sn.pch_dnv_gl_product_certificate,sn.pch_eu_declaration,dn.po_no,sn.delivery_document_no,
	DATE_FORMAT(sn.delivery_date, '%d-%m-%Y') as delivery_date from `tabSerial No` sn ,`tabDelivery Note` dn where sn.delivery_document_type!="Null" and sn.delivery_document_type="Delivery Note"  and sn.delivery_document_no=dn.name and sn.customer='"""+customer_list+"""' order by  dn.po_no desc""" ,  as_dict = 1)
		#print("delivery_note_list",delivery_note_list)
		return delivery_note_list


##Ascending
@frappe.whitelist()
def po_no_customer_po_asc(po_no):
	user=frappe.db.get_value("User",{"name":frappe.session.user},"name")
	#print("user",user);
	user_name = frappe.db.sql("""select td.link_name from `tabContact` tc, `tabDynamic Link` td where td.link_doctype="Customer" and td.parent=tc.name and tc.user='"""+user+"""' """)
	#print("user_name",user_name);
	if(len(user_name)==1):
		for user_list in user_name:
			customer_list=user_list[0];
			delivery_note_list = frappe.db.sql("""select sn.item_name,sn.serial_no,sn.pch_coc,sn.pch_pressure_test,sn.pch_build_sheet,sn.pch1_combined_pdf,sn.pch_dnv_gl_product_certificate,sn.pch_eu_declaration,dn.po_no,sn.delivery_document_no,
	DATE_FORMAT(sn.delivery_date, '%d-%m-%Y') as delivery_date from `tabSerial No` sn ,`tabDelivery Note` dn where sn.delivery_document_type!="Null" and sn.delivery_document_type="Delivery Note"  and sn.delivery_document_no=dn.name and dn.po_no  LIKE '"""+po_no+"%""' and sn.customer='"""+customer_list+"""' order by  dn.po_no asc""" ,  as_dict = 1)
		#print("delivery_note_list",delivery_note_list)
		return delivery_note_list

@frappe.whitelist()
def serial_no_customer_po_asc(serial_no):
	user=frappe.db.get_value("User",{"name":frappe.session.user},"name")
	#print("user",user);
	user_name = frappe.db.sql("""select td.link_name from `tabContact` tc, `tabDynamic Link` td where td.link_doctype="Customer" and td.parent=tc.name and tc.user='"""+user+"""' """)
	#print("user_name",user_name);
	if(len(user_name)==1):
		for user_list in user_name:
			customer_list=user_list[0];
			delivery_note_list = frappe.db.sql("""select sn.item_name,sn.serial_no,sn.pch_coc,sn.pch_pressure_test,sn.pch_build_sheet,sn.pch1_combined_pdf,sn.pch_dnv_gl_product_certificate,sn.pch_eu_declaration,dn.po_no,sn.delivery_document_no,
	DATE_FORMAT(sn.delivery_date, '%d-%m-%Y') as delivery_date from `tabSerial No` sn ,`tabDelivery Note` dn where sn.delivery_document_type!="Null" and sn.delivery_document_type="Delivery Note"  and sn.delivery_document_no=dn.name and sn.serial_no  LIKE '"""+serial_no+"%""' and sn.customer='"""+customer_list+"""' order by dn.po_no asc""" ,  as_dict = 1)
		#print("delivery_note_list",delivery_note_list)
		return delivery_note_list

@frappe.whitelist()
def delivery_document_no_customer_po_asc(delivery_document_no):
	user=frappe.db.get_value("User",{"name":frappe.session.user},"name")
	#print("user",user);
	user_name = frappe.db.sql("""select td.link_name from `tabContact` tc, `tabDynamic Link` td where td.link_doctype="Customer" and td.parent=tc.name and tc.user='"""+user+"""' """)
	#print("user_name",user_name);
	if(len(user_name)==1):
		for user_list in user_name:
			customer_list=user_list[0];
			delivery_note_list = frappe.db.sql("""select sn.item_name,sn.serial_no,sn.pch_coc,sn.pch_pressure_test,sn.pch_build_sheet,sn.pch1_combined_pdf,sn.pch_dnv_gl_product_certificate,sn.pch_eu_declaration,dn.po_no,sn.delivery_document_no,
	DATE_FORMAT(sn.delivery_date, '%d-%m-%Y') as delivery_date from `tabSerial No` sn ,`tabDelivery Note` dn where sn.delivery_document_type!="Null" and sn.delivery_document_type="Delivery Note"  and sn.delivery_document_no=dn.name and sn.delivery_document_no  LIKE '"""+delivery_document_no+"%""' and sn.customer='"""+customer_list+"""' order by  dn.po_no asc""" ,  as_dict = 1)
		#print("delivery_note_list",delivery_note_list)
		return delivery_note_list

@frappe.whitelist()
def delivery_serial_customer_po_asc(delivery_document_no,serial_no):
	user=frappe.db.get_value("User",{"name":frappe.session.user},"name")
	#print("user",user);
	user_name = frappe.db.sql("""select td.link_name from `tabContact` tc, `tabDynamic Link` td where td.link_doctype="Customer" and td.parent=tc.name and tc.user='"""+user+"""' """)
	#print("user_name",user_name);
	if(len(user_name)==1):
		for user_list in user_name:
			customer_list=user_list[0];
			delivery_note_list = frappe.db.sql("""select sn.item_name,sn.serial_no,sn.pch_coc,sn.pch_pressure_test,sn.pch_build_sheet,sn.pch1_combined_pdf,sn.pch_dnv_gl_product_certificate,sn.pch_eu_declaration,dn.po_no,sn.delivery_document_no,
	DATE_FORMAT(sn.delivery_date, '%d-%m-%Y') as delivery_date from `tabSerial No` sn ,`tabDelivery Note` dn where sn.delivery_document_type!="Null" and sn.delivery_document_type="Delivery Note"  and sn.delivery_document_no=dn.name and sn.serial_no  LIKE '"""+serial_no+"%""' and  sn.delivery_document_no  LIKE '"""+delivery_document_no+"%""' and sn.customer='"""+customer_list+"""' order by  dn.po_no asc""" ,  as_dict = 1)
		#print("delivery_note_list",delivery_note_list)
		return delivery_note_list

@frappe.whitelist()
def po_serial_customer_po_asc(po_no,serial_no):
	user=frappe.db.get_value("User",{"name":frappe.session.user},"name")
	#print("user",user);
	user_name = frappe.db.sql("""select td.link_name from `tabContact` tc, `tabDynamic Link` td where td.link_doctype="Customer" and td.parent=tc.name and tc.user='"""+user+"""' """)
	#print("user_name",user_name);
	if(len(user_name)==1):
		for user_list in user_name:
			customer_list=user_list[0];
			delivery_note_list = frappe.db.sql("""select sn.item_name,sn.serial_no,sn.pch_coc,sn.pch_pressure_test,sn.pch_build_sheet,sn.pch1_combined_pdf,sn.pch_dnv_gl_product_certificate,sn.pch_eu_declaration,dn.po_no,sn.delivery_document_no,
	DATE_FORMAT(sn.delivery_date, '%d-%m-%Y') as delivery_date from `tabSerial No` sn ,`tabDelivery Note` dn where sn.delivery_document_type!="Null" and sn.delivery_document_type="Delivery Note"  and sn.delivery_document_no=dn.name and dn.po_no  LIKE '"""+po_no+"%""' and  sn.serial_no  LIKE '"""+serial_no+"%""' and sn.customer='"""+customer_list+"""' order by  dn.po_no asc""" ,  as_dict = 1)
		#print("delivery_note_list",delivery_note_list)
		return delivery_note_list

@frappe.whitelist()
def po_delivery_customer_po_asc(po_no,delivery_document_no):
	user=frappe.db.get_value("User",{"name":frappe.session.user},"name")
	#print("user",user);
	user_name = frappe.db.sql("""select td.link_name from `tabContact` tc, `tabDynamic Link` td where td.link_doctype="Customer" and td.parent=tc.name and tc.user='"""+user+"""' """)
	#print("user_name",user_name);
	if(len(user_name)==1):
		for user_list in user_name:
			customer_list=user_list[0];
			delivery_note_list = frappe.db.sql("""select sn.item_name,sn.serial_no,sn.pch_coc,sn.pch_pressure_test,sn.pch_build_sheet,sn.pch1_combined_pdf,sn.pch_dnv_gl_product_certificate,sn.pch_eu_declaration,dn.po_no,sn.delivery_document_no,
	DATE_FORMAT(sn.delivery_date, '%d-%m-%Y') as delivery_date from `tabSerial No` sn ,`tabDelivery Note` dn where sn.delivery_document_type!="Null" and sn.delivery_document_type="Delivery Note"  and sn.delivery_document_no=dn.name and dn.po_no  LIKE '"""+po_no+"%""' and  sn.delivery_document_no  LIKE '"""+delivery_document_no+"%""' and sn.customer='"""+customer_list+"""' order by  dn.po_no asc""" ,  as_dict = 1)
		#print("delivery_note_list",delivery_note_list)
		return delivery_note_list

@frappe.whitelist()
def all_filters_applied_customer_po_asc(po_no,delivery_document_no,serial_no):
	user=frappe.db.get_value("User",{"name":frappe.session.user},"name")
	#print("user",user);
	user_name = frappe.db.sql("""select td.link_name from `tabContact` tc, `tabDynamic Link` td where td.link_doctype="Customer" and td.parent=tc.name and tc.user='"""+user+"""' """)
	#print("user_name",user_name);
	if(len(user_name)==1):
		for user_list in user_name:
			customer_list=user_list[0];
			delivery_note_list = frappe.db.sql("""select sn.item_name,sn.serial_no,sn.pch_coc,sn.pch_pressure_test,sn.pch_build_sheet,sn.pch1_combined_pdf,sn.pch_dnv_gl_product_certificate,sn.pch_eu_declaration,dn.po_no,sn.delivery_document_no,
	DATE_FORMAT(sn.delivery_date, '%d-%m-%Y') as delivery_date from `tabSerial No` sn ,`tabDelivery Note` dn where sn.delivery_document_type!="Null" and sn.delivery_document_type="Delivery Note"  and sn.delivery_document_no=dn.name and dn.po_no  LIKE '"""+po_no+"%""' and sn.serial_no  LIKE '"""+serial_no+"%""' and  sn.delivery_document_no  LIKE '"""+delivery_document_no+"%""' and sn.customer='"""+customer_list+"""' order by  dn.po_no asc""" ,  as_dict = 1)
		#print("delivery_note_list",delivery_note_list)
		return delivery_note_list

@frappe.whitelist()
def customer_po_asc():
	user=frappe.db.get_value("User",{"name":frappe.session.user},"name")
	#print("user",user);
	user_name = frappe.db.sql("""select td.link_name from `tabContact` tc, `tabDynamic Link` td where td.link_doctype="Customer" and td.parent=tc.name and tc.user='"""+user+"""' """)
	#print("user_name",user_name);
	if(len(user_name)==1):
		for user_list in user_name:
			customer_list=user_list[0];
			delivery_note_list = frappe.db.sql("""select sn.item_name,sn.serial_no,sn.pch_coc,sn.pch_pressure_test,sn.pch_build_sheet,sn.pch1_combined_pdf,sn.pch_dnv_gl_product_certificate,sn.pch_eu_declaration,dn.po_no,sn.delivery_document_no,
	DATE_FORMAT(sn.delivery_date, '%d-%m-%Y') as delivery_date from `tabSerial No` sn ,`tabDelivery Note` dn where sn.delivery_document_type!="Null" and sn.delivery_document_type="Delivery Note"  and sn.delivery_document_no=dn.name and sn.customer='"""+customer_list+"""' order by  dn.po_no asc""" ,  as_dict = 1)
		#print("delivery_note_list",delivery_note_list)
		return delivery_note_list

#asending serial No
@frappe.whitelist()
def po_no_serial_no_desc(po_no):
	user=frappe.db.get_value("User",{"name":frappe.session.user},"name")
	#print("user",user);
	user_name = frappe.db.sql("""select td.link_name from `tabContact` tc, `tabDynamic Link` td where td.link_doctype="Customer" and td.parent=tc.name and tc.user='"""+user+"""' """)
	#print("user_name",user_name);
	if(len(user_name)==1):
		for user_list in user_name:
			customer_list=user_list[0];
			delivery_note_list = frappe.db.sql("""select sn.item_name,sn.serial_no,sn.pch_coc,sn.pch_pressure_test,sn.pch_build_sheet,sn.pch1_combined_pdf,sn.pch_dnv_gl_product_certificate,sn.pch_eu_declaration,dn.po_no,sn.delivery_document_no,
	DATE_FORMAT(sn.delivery_date, '%d-%m-%Y') as delivery_date from `tabSerial No` sn ,`tabDelivery Note` dn where sn.delivery_document_type!="Null" and sn.delivery_document_type="Delivery Note"  and sn.delivery_document_no=dn.name and dn.po_no  LIKE '"""+po_no+"%""' and sn.customer='"""+customer_list+"""' order by  sn.serial_no desc""" ,  as_dict = 1)
		#print("delivery_note_list",delivery_note_list)
		return delivery_note_list

@frappe.whitelist()
def serial_no_serial_no_desc(serial_no):
	user=frappe.db.get_value("User",{"name":frappe.session.user},"name")
	#print("user",user);
	user_name = frappe.db.sql("""select td.link_name from `tabContact` tc, `tabDynamic Link` td where td.link_doctype="Customer" and td.parent=tc.name and tc.user='"""+user+"""' """)
	#print("user_name",user_name);
	if(len(user_name)==1):
		for user_list in user_name:
			customer_list=user_list[0];
			delivery_note_list = frappe.db.sql("""select sn.item_name,sn.serial_no,sn.pch_coc,sn.pch_pressure_test,sn.pch_build_sheet,sn.pch1_combined_pdf,sn.pch_dnv_gl_product_certificate,sn.pch_eu_declaration,dn.po_no,sn.delivery_document_no,
	DATE_FORMAT(sn.delivery_date, '%d-%m-%Y') as delivery_date from `tabSerial No` sn ,`tabDelivery Note` dn where sn.delivery_document_type!="Null" and sn.delivery_document_type="Delivery Note"  and sn.delivery_document_no=dn.name and sn.serial_no  LIKE '"""+serial_no+"%""' and sn.customer='"""+customer_list+"""' order by  sn.serial_no desc""" ,  as_dict = 1)
		#print("delivery_note_list",delivery_note_list)
		return delivery_note_list

@frappe.whitelist()
def delivery_serial_no_delivery_no_desc(delivery_document_no):
	user=frappe.db.get_value("User",{"name":frappe.session.user},"name")
	#print("user",user);
	user_name = frappe.db.sql("""select td.link_name from `tabContact` tc, `tabDynamic Link` td where td.link_doctype="Customer" and td.parent=tc.name and tc.user='"""+user+"""' """)
	#print("user_name",user_name);
	if(len(user_name)==1):
		for user_list in user_name:
			customer_list=user_list[0];
			delivery_note_list = frappe.db.sql("""select sn.item_name,sn.serial_no,sn.pch_coc,sn.pch_pressure_test,sn.pch_build_sheet,sn.pch1_combined_pdf,sn.pch_dnv_gl_product_certificate,sn.pch_eu_declaration,dn.po_no,sn.delivery_document_no,
	DATE_FORMAT(sn.delivery_date, '%d-%m-%Y') as delivery_date from `tabSerial No` sn ,`tabDelivery Note` dn where sn.delivery_document_type!="Null" and sn.delivery_document_type="Delivery Note"  and sn.delivery_document_no=dn.name and sn.delivery_document_no  LIKE '"""+delivery_document_no+"%""' and sn.customer='"""+customer_list+"""' order by  sn.serial_no desc""" ,  as_dict = 1)
		#print("delivery_note_list",delivery_note_list)
		return delivery_note_list

@frappe.whitelist()
def delivery_serial_serial_no_desc(delivery_document_no,serial_no):
	user=frappe.db.get_value("User",{"name":frappe.session.user},"name")
	#print("user",user);
	user_name = frappe.db.sql("""select td.link_name from `tabContact` tc, `tabDynamic Link` td where td.link_doctype="Customer" and td.parent=tc.name and tc.user='"""+user+"""' """)
	#print("user_name",user_name);
	if(len(user_name)==1):
		for user_list in user_name:
			customer_list=user_list[0];
			delivery_note_list = frappe.db.sql("""select sn.item_name,sn.serial_no,sn.pch_coc,sn.pch_pressure_test,sn.pch_build_sheet,sn.pch1_combined_pdf,sn.pch_dnv_gl_product_certificate,sn.pch_eu_declaration,dn.po_no,sn.delivery_document_no,
	DATE_FORMAT(sn.delivery_date, '%d-%m-%Y') as delivery_date from `tabSerial No` sn ,`tabDelivery Note` dn where sn.delivery_document_type!="Null" and sn.delivery_document_type="Delivery Note"  and sn.delivery_document_no=dn.name and sn.serial_no  LIKE '"""+serial_no+"%""' and  sn.delivery_document_no  LIKE '"""+delivery_document_no+"%""' and sn.customer='"""+customer_list+"""' order by  sn.serial_no desc""" ,  as_dict = 1)
		#print("delivery_note_list",delivery_note_list)
		return delivery_note_list

@frappe.whitelist()
def po_serial_serial_no_desc(po_no,serial_no):
	user=frappe.db.get_value("User",{"name":frappe.session.user},"name")
	#print("user",user);
	user_name = frappe.db.sql("""select td.link_name from `tabContact` tc, `tabDynamic Link` td where td.link_doctype="Customer" and td.parent=tc.name and tc.user='"""+user+"""' """)
	#print("user_name",user_name);
	if(len(user_name)==1):
		for user_list in user_name:
			customer_list=user_list[0];
			delivery_note_list = frappe.db.sql("""select sn.item_name,sn.serial_no,sn.pch_coc,sn.pch_pressure_test,sn.pch_build_sheet,sn.pch1_combined_pdf,sn.pch_dnv_gl_product_certificate,sn.pch_eu_declaration,dn.po_no,sn.delivery_document_no,
	DATE_FORMAT(sn.delivery_date, '%d-%m-%Y') as delivery_date from `tabSerial No` sn ,`tabDelivery Note` dn where sn.delivery_document_type!="Null" and sn.delivery_document_type="Delivery Note"  and sn.delivery_document_no=dn.name and dn.po_no  LIKE '"""+po_no+"%""' and  sn.serial_no  LIKE '"""+serial_no+"%""' and sn.customer='"""+customer_list+"""' order by  sn.serial_no desc""" ,  as_dict = 1)
		#print("delivery_note_list",delivery_note_list)
		return delivery_note_list

@frappe.whitelist()
def po_delivery_serial_no_desc(po_no,delivery_document_no):
	user=frappe.db.get_value("User",{"name":frappe.session.user},"name")
	#print("user",user);
	user_name = frappe.db.sql("""select td.link_name from `tabContact` tc, `tabDynamic Link` td where td.link_doctype="Customer" and td.parent=tc.name and tc.user='"""+user+"""' """)
	#print("user_name",user_name);
	if(len(user_name)==1):
		for user_list in user_name:
			customer_list=user_list[0];
			delivery_note_list = frappe.db.sql("""select sn.item_name,sn.serial_no,sn.pch_coc,sn.pch_pressure_test,sn.pch_build_sheet,sn.pch1_combined_pdf,sn.pch_dnv_gl_product_certificate,sn.pch_eu_declaration,dn.po_no,sn.delivery_document_no,
	DATE_FORMAT(sn.delivery_date, '%d-%m-%Y') as delivery_date from `tabSerial No` sn ,`tabDelivery Note` dn where sn.delivery_document_type!="Null" and sn.delivery_document_type="Delivery Note"  and sn.delivery_document_no=dn.name and dn.po_no  LIKE '"""+po_no+"%""' and  sn.delivery_document_no  LIKE '"""+delivery_document_no+"%""' and sn.customer='"""+customer_list+"""' order by  sn.serial_no desc""" ,  as_dict = 1)
		#print("delivery_note_list",delivery_note_list)
		return delivery_note_list

@frappe.whitelist()
def all_filters_applied_serial_no_desc(po_no,delivery_document_no,serial_no):
	user=frappe.db.get_value("User",{"name":frappe.session.user},"name")
	#print("user",user);
	user_name = frappe.db.sql("""select td.link_name from `tabContact` tc, `tabDynamic Link` td where td.link_doctype="Customer" and td.parent=tc.name and tc.user='"""+user+"""' """)
	#print("user_name",user_name);
	if(len(user_name)==1):
		for user_list in user_name:
			customer_list=user_list[0];
			delivery_note_list = frappe.db.sql("""select sn.item_name,sn.serial_no,sn.pch_coc,sn.pch_pressure_test,sn.pch_build_sheet,sn.pch1_combined_pdf,sn.pch_dnv_gl_product_certificate,sn.pch_eu_declaration,dn.po_no,sn.delivery_document_no,
	DATE_FORMAT(sn.delivery_date, '%d-%m-%Y') as delivery_date from `tabSerial No` sn ,`tabDelivery Note` dn where sn.delivery_document_type!="Null" and sn.delivery_document_type="Delivery Note"  and sn.delivery_document_no=dn.name and dn.po_no  LIKE '"""+po_no+"%""' and sn.serial_no  LIKE '"""+serial_no+"%""' and  sn.delivery_document_no  LIKE '"""+delivery_document_no+"%""' and sn.customer='"""+customer_list+"""' order by  sn.serial_no desc""" ,  as_dict = 1)
		#print("delivery_note_list",delivery_note_list)
		return delivery_note_list

@frappe.whitelist()
def serial_no_desc():
	user=frappe.db.get_value("User",{"name":frappe.session.user},"name")
	#print("user",user);
	user_name = frappe.db.sql("""select td.link_name from `tabContact` tc, `tabDynamic Link` td where td.link_doctype="Customer" and td.parent=tc.name and tc.user='"""+user+"""' """)
	#print("user_name",user_name);
	if(len(user_name)==1):
		for user_list in user_name:
			customer_list=user_list[0];
			delivery_note_list = frappe.db.sql("""select sn.item_name,sn.serial_no,sn.pch_coc,sn.pch_pressure_test,sn.pch_build_sheet,sn.pch1_combined_pdf,sn.pch_dnv_gl_product_certificate,sn.pch_eu_declaration,dn.po_no,sn.delivery_document_no,
	DATE_FORMAT(sn.delivery_date, '%d-%m-%Y') as delivery_date from `tabSerial No` sn ,`tabDelivery Note` dn where sn.delivery_document_type!="Null" and sn.delivery_document_type="Delivery Note"  and sn.delivery_document_no=dn.name and sn.customer='"""+customer_list+"""' order by  sn.serial_no desc""" ,  as_dict = 1)
		#print("delivery_note_list",delivery_note_list)
		return delivery_note_list


#asending serial No
@frappe.whitelist()
def po_no_serial_no_asc(po_no):
	user=frappe.db.get_value("User",{"name":frappe.session.user},"name")
	#print("user",user);
	user_name = frappe.db.sql("""select td.link_name from `tabContact` tc, `tabDynamic Link` td where td.link_doctype="Customer" and td.parent=tc.name and tc.user='"""+user+"""' """)
	#print("user_name",user_name);
	if(len(user_name)==1):
		for user_list in user_name:
			customer_list=user_list[0];
			delivery_note_list = frappe.db.sql("""select sn.item_name,sn.serial_no,sn.pch_coc,sn.pch_pressure_test,sn.pch_build_sheet,sn.pch1_combined_pdf,sn.pch_dnv_gl_product_certificate,sn.pch_eu_declaration,dn.po_no,sn.delivery_document_no,
	DATE_FORMAT(sn.delivery_date, '%d-%m-%Y') as delivery_date from `tabSerial No` sn ,`tabDelivery Note` dn where sn.delivery_document_type!="Null" and sn.delivery_document_type="Delivery Note"  and sn.delivery_document_no=dn.name and dn.po_no  LIKE '"""+po_no+"%""' and sn.customer='"""+customer_list+"""' order by  sn.serial_no asc""" ,  as_dict = 1)
		#print("delivery_note_list",delivery_note_list)
		return delivery_note_list

@frappe.whitelist()
def serial_no_serial_no_asc(serial_no):
	user=frappe.db.get_value("User",{"name":frappe.session.user},"name")
	#print("user",user);
	user_name = frappe.db.sql("""select td.link_name from `tabContact` tc, `tabDynamic Link` td where td.link_doctype="Customer" and td.parent=tc.name and tc.user='"""+user+"""' """)
	#print("user_name",user_name);
	if(len(user_name)==1):
		for user_list in user_name:
			customer_list=user_list[0];
			delivery_note_list = frappe.db.sql("""select sn.item_name,sn.serial_no,sn.pch_coc,sn.pch_pressure_test,sn.pch_build_sheet,sn.pch1_combined_pdf,sn.pch_dnv_gl_product_certificate,sn.pch_eu_declaration,dn.po_no,sn.delivery_document_no,
	DATE_FORMAT(sn.delivery_date, '%d-%m-%Y') as delivery_date from `tabSerial No` sn ,`tabDelivery Note` dn where sn.delivery_document_type!="Null" and sn.delivery_document_type="Delivery Note"  and sn.delivery_document_no=dn.name and sn.serial_no  LIKE '"""+serial_no+"%""' and sn.customer='"""+customer_list+"""' order by  sn.serial_no asc""" ,  as_dict = 1)
		#print("delivery_note_list",delivery_note_list)
		return delivery_note_list

@frappe.whitelist()
def delivery_serial_no_delivery_no_asc(delivery_document_no):
	user=frappe.db.get_value("User",{"name":frappe.session.user},"name")
	#print("user",user);
	user_name = frappe.db.sql("""select td.link_name from `tabContact` tc, `tabDynamic Link` td where td.link_doctype="Customer" and td.parent=tc.name and tc.user='"""+user+"""' """)
	#print("user_name",user_name);
	if(len(user_name)==1):
		for user_list in user_name:
			customer_list=user_list[0];
			delivery_note_list = frappe.db.sql("""select sn.item_name,sn.serial_no,sn.pch_coc,sn.pch_pressure_test,sn.pch_build_sheet,sn.pch1_combined_pdf,sn.pch_dnv_gl_product_certificate,sn.pch_eu_declaration,dn.po_no,sn.delivery_document_no,
	DATE_FORMAT(sn.delivery_date, '%d-%m-%Y') as delivery_date from `tabSerial No` sn ,`tabDelivery Note` dn where sn.delivery_document_type!="Null" and sn.delivery_document_type="Delivery Note"  and sn.delivery_document_no=dn.name and sn.delivery_document_no  LIKE '"""+delivery_document_no+"%""' and sn.customer='"""+customer_list+"""' order by  sn.serial_no asc""" ,  as_dict = 1)
		#print("delivery_note_list",delivery_note_list)
		return delivery_note_list

@frappe.whitelist()
def delivery_serial_serial_no_asc(delivery_document_no,serial_no):
	user=frappe.db.get_value("User",{"name":frappe.session.user},"name")
	#print("user",user);
	user_name = frappe.db.sql("""select td.link_name from `tabContact` tc, `tabDynamic Link` td where td.link_doctype="Customer" and td.parent=tc.name and tc.user='"""+user+"""' """)
	#print("user_name",user_name);
	if(len(user_name)==1):
		for user_list in user_name:
			customer_list=user_list[0];
			delivery_note_list = frappe.db.sql("""select sn.item_name,sn.serial_no,sn.pch_coc,sn.pch_pressure_test,sn.pch_build_sheet,sn.pch1_combined_pdf,sn.pch_dnv_gl_product_certificate,sn.pch_eu_declaration,dn.po_no,sn.delivery_document_no,
	DATE_FORMAT(sn.delivery_date, '%d-%m-%Y') as delivery_date from `tabSerial No` sn ,`tabDelivery Note` dn where sn.delivery_document_type!="Null" and sn.delivery_document_type="Delivery Note"  and sn.delivery_document_no=dn.name and sn.serial_no  LIKE '"""+serial_no+"%""' and  sn.delivery_document_no  LIKE '"""+delivery_document_no+"%""' and sn.customer='"""+customer_list+"""' order by  sn.serial_no asc""" ,  as_dict = 1)
		#print("delivery_note_list",delivery_note_list)
		return delivery_note_list

@frappe.whitelist()
def po_serial_serial_no_asc(po_no,serial_no):
	user=frappe.db.get_value("User",{"name":frappe.session.user},"name")
	#print("user",user);
	user_name = frappe.db.sql("""select td.link_name from `tabContact` tc, `tabDynamic Link` td where td.link_doctype="Customer" and td.parent=tc.name and tc.user='"""+user+"""' """)
	#print("user_name",user_name);
	if(len(user_name)==1):
		for user_list in user_name:
			customer_list=user_list[0];
			delivery_note_list = frappe.db.sql("""select sn.item_name,sn.serial_no,sn.pch_coc,sn.pch_pressure_test,sn.pch_build_sheet,sn.pch1_combined_pdf,sn.pch_dnv_gl_product_certificate,sn.pch_eu_declaration,dn.po_no,sn.delivery_document_no,
	DATE_FORMAT(sn.delivery_date, '%d-%m-%Y') as delivery_date from `tabSerial No` sn ,`tabDelivery Note` dn where sn.delivery_document_type!="Null" and sn.delivery_document_type="Delivery Note"  and sn.delivery_document_no=dn.name and dn.po_no  LIKE '"""+po_no+"%""' and  sn.serial_no  LIKE '"""+serial_no+"%""' and sn.customer='"""+customer_list+"""' order by  sn.serial_no asc""" ,  as_dict = 1)
		#print("delivery_note_list",delivery_note_list)
		return delivery_note_list

@frappe.whitelist()
def po_delivery_serial_no_asc(po_no,delivery_document_no):
	user=frappe.db.get_value("User",{"name":frappe.session.user},"name")
	#print("user",user);
	user_name = frappe.db.sql("""select td.link_name from `tabContact` tc, `tabDynamic Link` td where td.link_doctype="Customer" and td.parent=tc.name and tc.user='"""+user+"""' """)
	#print("user_name",user_name);
	if(len(user_name)==1):
		for user_list in user_name:
			customer_list=user_list[0];
			delivery_note_list = frappe.db.sql("""select sn.item_name,sn.serial_no,sn.pch_coc,sn.pch_pressure_test,sn.pch_build_sheet,sn.pch1_combined_pdf,sn.pch_dnv_gl_product_certificate,sn.pch_eu_declaration,dn.po_no,sn.delivery_document_no,
	DATE_FORMAT(sn.delivery_date, '%d-%m-%Y') as delivery_date from `tabSerial No` sn ,`tabDelivery Note` dn where sn.delivery_document_type!="Null" and sn.delivery_document_type="Delivery Note"  and sn.delivery_document_no=dn.name and dn.po_no  LIKE '"""+po_no+"%""' and  sn.delivery_document_no  LIKE '"""+delivery_document_no+"%""' and sn.customer='"""+customer_list+"""' order by  sn.serial_no asc""" ,  as_dict = 1)
		#print("delivery_note_list",delivery_note_list)
		return delivery_note_list

@frappe.whitelist()
def all_filters_applied_serial_no_asc(po_no,delivery_document_no,serial_no):
	user=frappe.db.get_value("User",{"name":frappe.session.user},"name")
	#print("user",user);
	user_name = frappe.db.sql("""select td.link_name from `tabContact` tc, `tabDynamic Link` td where td.link_doctype="Customer" and td.parent=tc.name and tc.user='"""+user+"""' """)
	#print("user_name",user_name);
	if(len(user_name)==1):
		for user_list in user_name:
			customer_list=user_list[0];
			delivery_note_list = frappe.db.sql("""select sn.item_name,sn.serial_no,sn.pch_coc,sn.pch_pressure_test,sn.pch_build_sheet,sn.pch1_combined_pdf,sn.pch_dnv_gl_product_certificate,sn.pch_eu_declaration,dn.po_no,sn.delivery_document_no,
	DATE_FORMAT(sn.delivery_date, '%d-%m-%Y') as delivery_date from `tabSerial No` sn ,`tabDelivery Note` dn where sn.delivery_document_type!="Null" and sn.delivery_document_type="Delivery Note"  and sn.delivery_document_no=dn.name and dn.po_no  LIKE '"""+po_no+"%""' and sn.serial_no  LIKE '"""+serial_no+"%""' and  sn.delivery_document_no  LIKE '"""+delivery_document_no+"%""' and sn.customer='"""+customer_list+"""' order by  sn.serial_no asc""" ,  as_dict = 1)
		#print("delivery_note_list",delivery_note_list)
		return delivery_note_list

@frappe.whitelist()
def serial_no_asc():
	user=frappe.db.get_value("User",{"name":frappe.session.user},"name")
	#print("user",user);
	user_name = frappe.db.sql("""select td.link_name from `tabContact` tc, `tabDynamic Link` td where td.link_doctype="Customer" and td.parent=tc.name and tc.user='"""+user+"""' """)
	#print("user_name",user_name);
	if(len(user_name)==1):
		for user_list in user_name:
			customer_list=user_list[0];
			delivery_note_list = frappe.db.sql("""select sn.item_name,sn.serial_no,sn.pch_coc,sn.pch_pressure_test,sn.pch_build_sheet,sn.pch1_combined_pdf,sn.pch_dnv_gl_product_certificate,sn.pch_eu_declaration,dn.po_no,sn.delivery_document_no,
	DATE_FORMAT(sn.delivery_date, '%d-%m-%Y') as delivery_date from `tabSerial No` sn ,`tabDelivery Note` dn where sn.delivery_document_type!="Null" and sn.delivery_document_type="Delivery Note"  and sn.delivery_document_no=dn.name and sn.customer='"""+customer_list+"""' order by  sn.serial_no asc""" ,  as_dict = 1)
		#print("delivery_note_list",delivery_note_list)
		return delivery_note_list

#descending item name
@frappe.whitelist()
def po_no_item_name_desc(po_no):
	user=frappe.db.get_value("User",{"name":frappe.session.user},"name")
	#print("user",user);
	user_name = frappe.db.sql("""select td.link_name from `tabContact` tc, `tabDynamic Link` td where td.link_doctype="Customer" and td.parent=tc.name and tc.user='"""+user+"""' """)
	#print("user_name",user_name);
	if(len(user_name)==1):
		for user_list in user_name:
			customer_list=user_list[0];
			delivery_note_list = frappe.db.sql("""select sn.item_name,sn.serial_no,sn.pch_coc,sn.pch_pressure_test,sn.pch_build_sheet,sn.pch1_combined_pdf,sn.pch_dnv_gl_product_certificate,sn.pch_eu_declaration,dn.po_no,sn.delivery_document_no,
	DATE_FORMAT(sn.delivery_date, '%d-%m-%Y') as delivery_date from `tabSerial No` sn ,`tabDelivery Note` dn where sn.delivery_document_type!="Null" and sn.delivery_document_type="Delivery Note"  and sn.delivery_document_no=dn.name and dn.po_no  LIKE '"""+po_no+"%""' and sn.customer='"""+customer_list+"""' order by  sn.item_name desc""" ,  as_dict = 1)
		#print("delivery_note_list",delivery_note_list)
		return delivery_note_list

@frappe.whitelist()
def serial_no_item_name_desc(serial_no):
	user=frappe.db.get_value("User",{"name":frappe.session.user},"name")
	#print("user",user);
	user_name = frappe.db.sql("""select td.link_name from `tabContact` tc, `tabDynamic Link` td where td.link_doctype="Customer" and td.parent=tc.name and tc.user='"""+user+"""' """)
	#print("user_name",user_name);
	if(len(user_name)==1):
		for user_list in user_name:
			customer_list=user_list[0];
			delivery_note_list = frappe.db.sql("""select sn.item_name,sn.serial_no,sn.pch_coc,sn.pch_pressure_test,sn.pch_build_sheet,sn.pch1_combined_pdf,sn.pch_dnv_gl_product_certificate,sn.pch_eu_declaration,dn.po_no,sn.delivery_document_no,
	DATE_FORMAT(sn.delivery_date, '%d-%m-%Y') as delivery_date from `tabSerial No` sn ,`tabDelivery Note` dn where sn.delivery_document_type!="Null" and sn.delivery_document_type="Delivery Note"  and sn.delivery_document_no=dn.name and sn.serial_no  LIKE '"""+serial_no+"%""' and sn.customer='"""+customer_list+"""' order by  sn.item_name desc""" ,  as_dict = 1)
		#print("delivery_note_list",delivery_note_list)
		return delivery_note_list

@frappe.whitelist()
def delivery_item_name_delivery_no_desc(delivery_document_no):
	user=frappe.db.get_value("User",{"name":frappe.session.user},"name")
	#print("user",user);
	user_name = frappe.db.sql("""select td.link_name from `tabContact` tc, `tabDynamic Link` td where td.link_doctype="Customer" and td.parent=tc.name and tc.user='"""+user+"""' """)
	#print("user_name",user_name);
	if(len(user_name)==1):
		for user_list in user_name:
			customer_list=user_list[0];
			delivery_note_list = frappe.db.sql("""select sn.item_name,sn.serial_no,sn.pch_coc,sn.pch_pressure_test,sn.pch_build_sheet,sn.pch1_combined_pdf,sn.pch_dnv_gl_product_certificate,sn.pch_eu_declaration,dn.po_no,sn.delivery_document_no,
	DATE_FORMAT(sn.delivery_date, '%d-%m-%Y') as delivery_date from `tabSerial No` sn ,`tabDelivery Note` dn where sn.delivery_document_type!="Null" and sn.delivery_document_type="Delivery Note"  and sn.delivery_document_no=dn.name and sn.delivery_document_no  LIKE '"""+delivery_document_no+"%""' and sn.customer='"""+customer_list+"""' order by  sn.item_name desc""" ,  as_dict = 1)
		#print("delivery_note_list",delivery_note_list)
		return delivery_note_list

@frappe.whitelist()
def delivery_serial_item_name_desc(delivery_document_no,serial_no):
	user=frappe.db.get_value("User",{"name":frappe.session.user},"name")
	#print("user",user);
	user_name = frappe.db.sql("""select td.link_name from `tabContact` tc, `tabDynamic Link` td where td.link_doctype="Customer" and td.parent=tc.name and tc.user='"""+user+"""' """)
	#print("user_name",user_name);
	if(len(user_name)==1):
		for user_list in user_name:
			customer_list=user_list[0];
			delivery_note_list = frappe.db.sql("""select sn.item_name,sn.serial_no,sn.pch_coc,sn.pch_pressure_test,sn.pch_build_sheet,sn.pch1_combined_pdf,sn.pch_dnv_gl_product_certificate,sn.pch_eu_declaration,dn.po_no,sn.delivery_document_no,
	DATE_FORMAT(sn.delivery_date, '%d-%m-%Y') as delivery_date from `tabSerial No` sn ,`tabDelivery Note` dn where sn.delivery_document_type!="Null" and sn.delivery_document_type="Delivery Note"  and sn.delivery_document_no=dn.name and sn.serial_no  LIKE '"""+serial_no+"%""' and  sn.delivery_document_no  LIKE '"""+delivery_document_no+"%""' and sn.customer='"""+customer_list+"""' order by  sn.item_name desc""" ,  as_dict = 1)
		#print("delivery_note_list",delivery_note_list)
		return delivery_note_list

@frappe.whitelist()
def po_serial_item_name_desc(po_no,serial_no):
	user=frappe.db.get_value("User",{"name":frappe.session.user},"name")
	#print("user",user);
	user_name = frappe.db.sql("""select td.link_name from `tabContact` tc, `tabDynamic Link` td where td.link_doctype="Customer" and td.parent=tc.name and tc.user='"""+user+"""' """)
	#print("user_name",user_name);
	if(len(user_name)==1):
		for user_list in user_name:
			customer_list=user_list[0];
			delivery_note_list = frappe.db.sql("""select sn.item_name,sn.serial_no,sn.pch_coc,sn.pch_pressure_test,sn.pch_build_sheet,sn.pch1_combined_pdf,sn.pch_dnv_gl_product_certificate,sn.pch_eu_declaration,dn.po_no,sn.delivery_document_no,
	DATE_FORMAT(sn.delivery_date, '%d-%m-%Y') as delivery_date from `tabSerial No` sn ,`tabDelivery Note` dn where sn.delivery_document_type!="Null" and sn.delivery_document_type="Delivery Note"  and sn.delivery_document_no=dn.name and dn.po_no  LIKE '"""+po_no+"%""' and  sn.serial_no  LIKE '"""+serial_no+"%""' and sn.customer='"""+customer_list+"""' order by  sn.item_name desc""" ,  as_dict = 1)
		#print("delivery_note_list",delivery_note_list)
		return delivery_note_list

@frappe.whitelist()
def po_delivery_item_name_desc(po_no,delivery_document_no):
	user=frappe.db.get_value("User",{"name":frappe.session.user},"name")
	#print("user",user);
	user_name = frappe.db.sql("""select td.link_name from `tabContact` tc, `tabDynamic Link` td where td.link_doctype="Customer" and td.parent=tc.name and tc.user='"""+user+"""' """)
	#print("user_name",user_name);
	if(len(user_name)==1):
		for user_list in user_name:
			customer_list=user_list[0];
			delivery_note_list = frappe.db.sql("""select sn.item_name,sn.serial_no,sn.pch_coc,sn.pch_pressure_test,sn.pch_build_sheet,sn.pch1_combined_pdf,sn.pch_dnv_gl_product_certificate,sn.pch_eu_declaration,dn.po_no,sn.delivery_document_no,
	DATE_FORMAT(sn.delivery_date, '%d-%m-%Y') as delivery_date from `tabSerial No` sn ,`tabDelivery Note` dn where sn.delivery_document_type!="Null" and sn.delivery_document_type="Delivery Note"  and sn.delivery_document_no=dn.name and dn.po_no  LIKE '"""+po_no+"%""' and  sn.delivery_document_no  LIKE '"""+delivery_document_no+"%""' and sn.customer='"""+customer_list+"""' order by  sn.item_name desc""" ,  as_dict = 1)
		#print("delivery_note_list",delivery_note_list)
		return delivery_note_list

@frappe.whitelist()
def all_filters_applied_item_name_desc(po_no,delivery_document_no,serial_no):
	user=frappe.db.get_value("User",{"name":frappe.session.user},"name")
	#print("user",user);
	user_name = frappe.db.sql("""select td.link_name from `tabContact` tc, `tabDynamic Link` td where td.link_doctype="Customer" and td.parent=tc.name and tc.user='"""+user+"""' """)
	#print("user_name",user_name);
	if(len(user_name)==1):
		for user_list in user_name:
			customer_list=user_list[0];
			delivery_note_list = frappe.db.sql("""select sn.item_name,sn.serial_no,sn.pch_coc,sn.pch_pressure_test,sn.pch_build_sheet,sn.pch1_combined_pdf,sn.pch_dnv_gl_product_certificate,sn.pch_eu_declaration,dn.po_no,sn.delivery_document_no,
	DATE_FORMAT(sn.delivery_date, '%d-%m-%Y') as delivery_date from `tabSerial No` sn ,`tabDelivery Note` dn where sn.delivery_document_type!="Null" and sn.delivery_document_type="Delivery Note"  and sn.delivery_document_no=dn.name and dn.po_no  LIKE '"""+po_no+"%""' and sn.serial_no  LIKE '"""+serial_no+"%""' and  sn.delivery_document_no  LIKE '"""+delivery_document_no+"%""' and sn.customer='"""+customer_list+"""' order by  sn.item_name desc""" ,  as_dict = 1)
		#print("delivery_note_list",delivery_note_list)
		return delivery_note_list

@frappe.whitelist()
def item_name_desc():
	user=frappe.db.get_value("User",{"name":frappe.session.user},"name")
	#print("user",user);
	user_name = frappe.db.sql("""select td.link_name from `tabContact` tc, `tabDynamic Link` td where td.link_doctype="Customer" and td.parent=tc.name and tc.user='"""+user+"""' """)
	#print("user_name",user_name);
	if(len(user_name)==1):
		for user_list in user_name:
			customer_list=user_list[0];
			delivery_note_list = frappe.db.sql("""select sn.item_name,sn.serial_no,sn.pch_coc,sn.pch_pressure_test,sn.pch_build_sheet,sn.pch1_combined_pdf,sn.pch_dnv_gl_product_certificate,sn.pch_eu_declaration,dn.po_no,sn.delivery_document_no,
	DATE_FORMAT(sn.delivery_date, '%d-%m-%Y') as delivery_date from `tabSerial No` sn ,`tabDelivery Note` dn where sn.delivery_document_type!="Null" and sn.delivery_document_type="Delivery Note"  and sn.delivery_document_no=dn.name and sn.customer='"""+customer_list+"""' order by  sn.item_name desc""" ,  as_dict = 1)
		#print("delivery_note_list",delivery_note_list)
		return delivery_note_list


#asending item name
@frappe.whitelist()
def po_no_item_name_asc(po_no):
	user=frappe.db.get_value("User",{"name":frappe.session.user},"name")
	#print("user",user);
	user_name = frappe.db.sql("""select td.link_name from `tabContact` tc, `tabDynamic Link` td where td.link_doctype="Customer" and td.parent=tc.name and tc.user='"""+user+"""' """)
	#print("user_name",user_name);
	if(len(user_name)==1):
		for user_list in user_name:
			customer_list=user_list[0];
			delivery_note_list = frappe.db.sql("""select sn.item_name,sn.serial_no,sn.pch_coc,sn.pch_pressure_test,sn.pch_build_sheet,sn.pch1_combined_pdf,sn.pch_dnv_gl_product_certificate,sn.pch_eu_declaration,dn.po_no,sn.delivery_document_no,
	DATE_FORMAT(sn.delivery_date, '%d-%m-%Y') as delivery_date from `tabSerial No` sn ,`tabDelivery Note` dn where sn.delivery_document_type!="Null" and sn.delivery_document_type="Delivery Note"  and sn.delivery_document_no=dn.name and dn.po_no  LIKE '"""+po_no+"%""' and sn.customer='"""+customer_list+"""' order by  sn.item_name asc""" ,  as_dict = 1)
		#print("delivery_note_list",delivery_note_list)
		return delivery_note_list

@frappe.whitelist()
def serial_no_item_name_asc(serial_no):
	user=frappe.db.get_value("User",{"name":frappe.session.user},"name")
	#print("user",user);
	user_name = frappe.db.sql("""select td.link_name from `tabContact` tc, `tabDynamic Link` td where td.link_doctype="Customer" and td.parent=tc.name and tc.user='"""+user+"""' """)
	#print("user_name",user_name);
	if(len(user_name)==1):
		for user_list in user_name:
			customer_list=user_list[0];
			delivery_note_list = frappe.db.sql("""select sn.item_name,sn.serial_no,sn.pch_coc,sn.pch_pressure_test,sn.pch_build_sheet,sn.pch1_combined_pdf,sn.pch_dnv_gl_product_certificate,sn.pch_eu_declaration,dn.po_no,sn.delivery_document_no,
	DATE_FORMAT(sn.delivery_date, '%d-%m-%Y') as delivery_date from `tabSerial No` sn ,`tabDelivery Note` dn where sn.delivery_document_type!="Null" and sn.delivery_document_type="Delivery Note"  and sn.delivery_document_no=dn.name and sn.serial_no  LIKE '"""+serial_no+"%""' and sn.customer='"""+customer_list+"""' order by  sn.item_name asc""" ,  as_dict = 1)
		#print("delivery_note_list",delivery_note_list)
		return delivery_note_list

@frappe.whitelist()
def delivery_item_name_delivery_no_asc(delivery_document_no):
	user=frappe.db.get_value("User",{"name":frappe.session.user},"name")
	#print("user",user);
	user_name = frappe.db.sql("""select td.link_name from `tabContact` tc, `tabDynamic Link` td where td.link_doctype="Customer" and td.parent=tc.name and tc.user='"""+user+"""' """)
	#print("user_name",user_name);
	if(len(user_name)==1):
		for user_list in user_name:
			customer_list=user_list[0];
			delivery_note_list = frappe.db.sql("""select sn.item_name,sn.serial_no,sn.pch_coc,sn.pch_pressure_test,sn.pch_build_sheet,sn.pch1_combined_pdf,sn.pch_dnv_gl_product_certificate,sn.pch_eu_declaration,dn.po_no,sn.delivery_document_no,
	DATE_FORMAT(sn.delivery_date, '%d-%m-%Y') as delivery_date from `tabSerial No` sn ,`tabDelivery Note` dn where sn.delivery_document_type!="Null" and sn.delivery_document_type="Delivery Note"  and sn.delivery_document_no=dn.name and sn.delivery_document_no  LIKE '"""+delivery_document_no+"%""' and sn.customer='"""+customer_list+"""' order by  sn.item_name asc""" ,  as_dict = 1)
		#print("delivery_note_list",delivery_note_list)
		return delivery_note_list

@frappe.whitelist()
def delivery_serial_item_name_asc(delivery_document_no,serial_no):
	user=frappe.db.get_value("User",{"name":frappe.session.user},"name")
	#print("user",user);
	user_name = frappe.db.sql("""select td.link_name from `tabContact` tc, `tabDynamic Link` td where td.link_doctype="Customer" and td.parent=tc.name and tc.user='"""+user+"""' """)
	#print("user_name",user_name);
	if(len(user_name)==1):
		for user_list in user_name:
			customer_list=user_list[0];
			delivery_note_list = frappe.db.sql("""select sn.item_name,sn.serial_no,sn.pch_coc,sn.pch_pressure_test,sn.pch_build_sheet,sn.pch1_combined_pdf,sn.pch_dnv_gl_product_certificate,sn.pch_eu_declaration,dn.po_no,sn.delivery_document_no,
	DATE_FORMAT(sn.delivery_date, '%d-%m-%Y') as delivery_date from `tabSerial No` sn ,`tabDelivery Note` dn where sn.delivery_document_type!="Null" and sn.delivery_document_type="Delivery Note"  and sn.delivery_document_no=dn.name and sn.serial_no  LIKE '"""+serial_no+"%""' and  sn.delivery_document_no  LIKE '"""+delivery_document_no+"%""' and sn.customer='"""+customer_list+"""' order by  sn.item_name asc""" ,  as_dict = 1)
		#print("delivery_note_list",delivery_note_list)
		return delivery_note_list

@frappe.whitelist()
def po_serial_item_name_asc(po_no,serial_no):
	user=frappe.db.get_value("User",{"name":frappe.session.user},"name")
	#print("user",user);
	user_name = frappe.db.sql("""select td.link_name from `tabContact` tc, `tabDynamic Link` td where td.link_doctype="Customer" and td.parent=tc.name and tc.user='"""+user+"""' """)
	#print("user_name",user_name);
	if(len(user_name)==1):
		for user_list in user_name:
			customer_list=user_list[0];
			delivery_note_list = frappe.db.sql("""select sn.item_name,sn.serial_no,sn.pch_coc,sn.pch_pressure_test,sn.pch_build_sheet,sn.pch1_combined_pdf,sn.pch_dnv_gl_product_certificate,sn.pch_eu_declaration,dn.po_no,sn.delivery_document_no,
	DATE_FORMAT(sn.delivery_date, '%d-%m-%Y') as delivery_date from `tabSerial No` sn ,`tabDelivery Note` dn where sn.delivery_document_type!="Null" and sn.delivery_document_type="Delivery Note"  and sn.delivery_document_no=dn.name and dn.po_no  LIKE '"""+po_no+"%""' and  sn.serial_no  LIKE '"""+serial_no+"%""' and sn.customer='"""+customer_list+"""' order by  sn.item_name asc""" ,  as_dict = 1)
		#print("delivery_note_list",delivery_note_list)
		return delivery_note_list

@frappe.whitelist()
def po_delivery_item_name_asc(po_no,delivery_document_no):
	user=frappe.db.get_value("User",{"name":frappe.session.user},"name")
	#print("user",user);
	user_name = frappe.db.sql("""select td.link_name from `tabContact` tc, `tabDynamic Link` td where td.link_doctype="Customer" and td.parent=tc.name and tc.user='"""+user+"""' """)
	#print("user_name",user_name);
	if(len(user_name)==1):
		for user_list in user_name:
			customer_list=user_list[0];
			delivery_note_list = frappe.db.sql("""select sn.item_name,sn.serial_no,sn.pch_coc,sn.pch_pressure_test,sn.pch_build_sheet,sn.pch1_combined_pdf,sn.pch_dnv_gl_product_certificate,sn.pch_eu_declaration,dn.po_no,sn.delivery_document_no,
	DATE_FORMAT(sn.delivery_date, '%d-%m-%Y') as delivery_date from `tabSerial No` sn ,`tabDelivery Note` dn where sn.delivery_document_type!="Null" and sn.delivery_document_type="Delivery Note"  and sn.delivery_document_no=dn.name and dn.po_no  LIKE '"""+po_no+"%""' and  sn.delivery_document_no  LIKE '"""+delivery_document_no+"%""' and sn.customer='"""+customer_list+"""' order by  sn.item_name asc""" ,  as_dict = 1)
		#print("delivery_note_list",delivery_note_list)
		return delivery_note_list

@frappe.whitelist()
def all_filters_applied_item_name_asc(po_no,delivery_document_no,serial_no):
	user=frappe.db.get_value("User",{"name":frappe.session.user},"name")
	#print("user",user);
	user_name = frappe.db.sql("""select td.link_name from `tabContact` tc, `tabDynamic Link` td where td.link_doctype="Customer" and td.parent=tc.name and tc.user='"""+user+"""' """)
	#print("user_name",user_name);
	if(len(user_name)==1):
		for user_list in user_name:
			customer_list=user_list[0];
			delivery_note_list = frappe.db.sql("""select sn.item_name,sn.serial_no,sn.pch_coc,sn.pch_pressure_test,sn.pch_build_sheet,sn.pch1_combined_pdf,sn.pch_dnv_gl_product_certificate,sn.pch_eu_declaration,dn.po_no,sn.delivery_document_no,
	DATE_FORMAT(sn.delivery_date, '%d-%m-%Y') as delivery_date from `tabSerial No` sn ,`tabDelivery Note` dn where sn.delivery_document_type!="Null" and sn.delivery_document_type="Delivery Note"  and sn.delivery_document_no=dn.name and dn.po_no  LIKE '"""+po_no+"%""' and sn.serial_no  LIKE '"""+serial_no+"%""' and  sn.delivery_document_no  LIKE '"""+delivery_document_no+"%""' and sn.customer='"""+customer_list+"""' order by  sn.item_name asc""" ,  as_dict = 1)
		#print("delivery_note_list",delivery_note_list)
		return delivery_note_list

@frappe.whitelist()
def item_name_asc():
	user=frappe.db.get_value("User",{"name":frappe.session.user},"name")
	#print("user",user);
	user_name = frappe.db.sql("""select td.link_name from `tabContact` tc, `tabDynamic Link` td where td.link_doctype="Customer" and td.parent=tc.name and tc.user='"""+user+"""' """)
	#print("user_name",user_name);
	if(len(user_name)==1):
		for user_list in user_name:
			customer_list=user_list[0];
			delivery_note_list = frappe.db.sql("""select sn.item_name,sn.serial_no,sn.pch_coc,sn.pch_pressure_test,sn.pch_build_sheet,sn.pch1_combined_pdf,sn.pch_dnv_gl_product_certificate,sn.pch_eu_declaration,dn.po_no,sn.delivery_document_no,
	DATE_FORMAT(sn.delivery_date, '%d-%m-%Y') as delivery_date from `tabSerial No` sn ,`tabDelivery Note` dn where sn.delivery_document_type!="Null" and sn.delivery_document_type="Delivery Note"  and sn.delivery_document_no=dn.name and sn.customer='"""+customer_list+"""' order by  sn.item_name asc""" ,  as_dict = 1)
		#print("delivery_note_list",delivery_note_list)
		return delivery_note_list







