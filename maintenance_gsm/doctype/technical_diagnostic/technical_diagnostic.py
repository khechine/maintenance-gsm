import frappe
from frappe.model.document import Document

class TechnicalDiagnostic(Document):
	def on_update(self):
		# Update Repair Order status if not already moved past Diagnostic
		ro = frappe.get_doc("Repair Order", self.repair_order)
		if ro.status == "Re\u00e7u":
			ro.status = "Diagnostic"
			ro.save()
