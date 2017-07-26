def validate(doc, method):
	remove_spaces(doc)
	create_supplier(doc)
	validate_email(doc)
	if doc.tax_id:
		tax_id = doc.tax_id.replace(".", "").replace(" ", "")
		if doc.type_document == "":
			pass
		elif doc.type_document == "Pasaporte":
			pass
		elif doc.type_document == "RUC":
			compute_check_digit(doc, tax_id)
		elif doc.type_document == "Cedula":
			compute_check_digit(doc, tax_id)
		elif doc.type_document == "Consumidor Final":
			doc.tax_id = "9999999999999"

def create_supplier(doc):
	import frappe
	is_supplier = doc.is_supplier
	if is_supplier == 1:
		supplier = frappe.db.sql("""select supplier_name, type_document, country,
			address, email, phone, province, tax_id from `tabSupplier`
			where tax_id = %s""",
			doc.tax_id, as_dict = 1)
		if supplier:
			supplier = frappe.get_doc("Supplier", doc.tax_id)
			if supplier:
				supplier.supplier_name = doc.customer_name
				supplier.comercial_name = doc.comercial_name
				supplier.type_document = doc.type_document
				supplier.country = doc.territory
				supplier.address = doc.street
				supplier.email = doc.email
				supplier.phone = doc.phone
				supplier.province = doc.province
				supplier.tax_id = doc.tax_id
				supplier.fecha_de_nacimiento = doc.fecha_de_nacimiento
				supplier.fecha_de_registro = doc.fecha_de_registro
				supplier.nombre_de_contacto = doc.nombre_de_contacto
				supplier.mobile = doc.mobile
				supplier.save()

		if not supplier:
			supplier = frappe.db.sql("""select supplier_name, type_document, country,
				address, email, phone, province, tax_id from `tabSupplier`
				where supplier_name = %s""",
				doc.customer_name, as_dict = 1)
			if supplier:
				supplier = frappe.get_doc("Supplier", doc.customer_name)
				supplier.supplier_name = doc.customer_name
				supplier.comercial_name = doc.comercial_name
				supplier.type_document = doc.type_document
				supplier.country = doc.territory
				supplier.address = doc.street
				supplier.email = doc.email
				supplier.phone = doc.phone
				supplier.province = doc.province
				supplier.tax_id = doc.tax_id
				supplier.fecha_de_nacimiento = doc.fecha_de_nacimiento
				supplier.fecha_de_registro = doc.fecha_de_registro
				supplier.nombre_de_contacto = doc.nombre_de_contacto
				supplier.mobile = doc.mobile
				supplier.save()

		if not supplier:
			supplier = frappe.get_doc({
			    "doctype":"Supplier",
			    "supplier_name": doc.customer_name,
				"comercial_name": doc.comercial_name,
				"type_document": doc.type_document,
				"country": doc.territory,
				"address": doc.street,
				"email" : doc.email,
				"phone" : doc.phone,
				"province" : doc.province,
				"tax_id":doc.tax_id,
				"nombre_de_contacto": doc.nombre_de_contacto,
				"fecha_de_nacimiento": doc.fecha_de_nacimiento,
				"fecha_de_registro":doc.fecha_de_registro,
				"mobile":doc.mobile
			})
			supplier.save()

def validate_email(doc):
	import re
	import frappe
	email = doc.email
	if email:
		if re.match("[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,3})", email):
			pass
		else:
			frappe.throw("Correo electronico no cumple con la estructura: ejemplo@mail.com")

def remove_spaces(doc):
	if doc.customer_name:
		doc.customer_name = doc.customer_name.strip()
	if doc.comercial_name:
		doc.comercial_name = doc.comercial_name.strip()
	if doc.tax_id:
		doc.tax_id = doc.tax_id.strip()
	if doc.street:
		doc.street = doc.street.strip()
	if doc.province:
		doc.province = doc.province.strip()
	if doc.phone:
		doc.phone = doc.phone.strip()
	if doc.email:
		doc.email = doc.email.strip()
	if doc.mobile:
		doc.mobile = doc.mobile.strip()
	if doc.nombre_de_contacto:
		doc.nombre_de_contacto = doc.nombre_de_contacto.strip()


def compute_check_digit(doc, raw_number):
	import frappe
	factor = 2
	x = 0
	set_check_digit = None
	if doc.type_document == 'RUC':
		if int(raw_number[2]) < 6:
			type_party='persona_natural'
		if int(raw_number[2]) == 6:
			type_party='entidad_publica'
		if int(raw_number[2]) == 9:
			type_party='persona_juridica'

		if type_party == 'persona_natural':
			if len(raw_number) != 13 or int(raw_number[2]) > 5 or raw_number[-3:] != '001':
				frappe.throw("Numero RUC no valido")
			number = raw_number[:9]
			set_check_digit = raw_number[9]
			for n in number:
				y = int(n) * factor
				if y >= 10:
					y = int(str(y)[0]) + int(str(y)[1])
				x += y
				if factor == 2:
					factor = 1
				else:
					factor = 2
			res = (x % 10)

			if res ==  0:
				value = 0
			else:
				value = 10 - (x % 10)

			if set_check_digit == str(value):
				pass
			else:
				frappe.throw("Numero RUC no valido")

		elif type_party == 'entidad_publica':
			if not len(raw_number) == 13 or raw_number[2] != '6' \
				or raw_number[-3:] != '001':
				frappe.throw("Numero RUC no valido")
			number = raw_number[:8]
			set_check_digit = raw_number[8]
			for n in reversed(number):
				x += int(n) * factor
				factor += 1
				if factor == 8:
					factor = 2
			value = 11 - (x % 11)
			if value == 11:
				value = 0
			if set_check_digit == str(value):
				pass
			else:
				frappe.throw("Numero RUC no valido")

		else:
			if len(raw_number) != 13 or \
				(type_party in ['persona_juridica'] \
				and int(raw_number[2]) != 9) or raw_number[-3:] != '001':
				frappe.throw("Numero RUC no valido")
			number = raw_number[:9]
			set_check_digit = raw_number[9]
			for n in reversed(number):
				x += int(n) * factor
				factor += 1
				if factor == 8:
					factor = 2
			value = 11 - (x % 11)

			if value == 11:
				value = 0
			if set_check_digit == str(value):
				pass
			else:
				frappe.throw("Numero RUC no valido")
	else:
		if len(raw_number) != 10:
			frappe.throw("Numero C.I. no valido")
		number = raw_number[:9]
		set_check_digit = raw_number[9]
		for n in number:
			y = int(n) * factor
			if y >= 10:
				y = int(str(y)[0]) + int(str(y)[1])
			x += y
			if factor == 2:
				factor = 1
			else:
				factor = 2
		res = (x % 10)
		if res ==  0:
			value = 0
		else:
			value = 10 - (x % 10)
		if set_check_digit == str(value):
			pass
		else:
			frappe.throw("Numero C.I. no valido")
