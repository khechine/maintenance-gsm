import frappe
from frappe.model.document import Document

class RepairOrder(Document):
	def after_insert(self):
		# Auto-create Technical Diagnostic
		self.create_diagnostic()

	def create_diagnostic(self):
		if not frappe.db.exists("Technical Diagnostic", {"repair_order": self.name}):
			diagnostic = frappe.new_doc("Technical Diagnostic")
			diagnostic.repair_order = self.name
			diagnostic.insert()

	def validate(self):
		if self.status == "En cours":
			# Block repair progress if quotation not approved
			quotation = frappe.get_all("Repair Quotation", filters={"repair_order": self.name}, fields=["customer_approval"])
			if not quotation or not quotation[0].customer_approval:
				frappe.throw("La r\u00e9paration ne peut pas commencer sans l'approbation du devis.")
