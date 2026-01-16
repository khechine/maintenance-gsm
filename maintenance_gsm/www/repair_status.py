import frappe

def get_context(context):
	imei = frappe.form_dict.get('imei')
	if imei:
		device = frappe.db.get_value("Appareil", {"imei": imei}, ["name", "status"], as_dict=True)
		if device:
			context.device_found = True
			context.imei = imei
			context.status = device.status
			
			# Get latest repair order
			ro = frappe.get_all("Repair Order", 
				filters={"device": device.name}, 
				fields=["status", "priority", "opened_on"],
				order_by="opened_on desc",
				limit=1
			)
			if ro:
				context.ro_status = ro[0].status
				context.priority = ro[0].priority
		else:
			context.device_found = False
			context.error = "Appareil non trouv\u00e9."
	return context
