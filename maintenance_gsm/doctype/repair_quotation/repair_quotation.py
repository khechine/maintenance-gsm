import frappe
from frappe.model.document import Document

class RepairQuotation(Document):
	def validate(self):
		self.calculate_totals()

	def calculate_totals(self):
		total_parts = 0
		for item in self.spare_parts:
			item.amount = item.qty * item.rate
			total_parts += item.amount
		self.total_estimated_cost = (self.labor_cost or 0) + total_parts

	def on_update(self):
		# Update Repair Order status if approved
		ro = frappe.get_doc("Repair Order", self.repair_order)
		if self.customer_approval and ro.status == "Diagnostic":
			ro.status = "Devis"
			ro.save()
