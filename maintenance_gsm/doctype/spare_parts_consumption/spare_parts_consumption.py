import frappe
from frappe.model.document import Document

class SparePartsConsumption(Document):
	def on_submit(self):
		self.create_stock_entry()

	def create_stock_entry(self):
		# Create ERPNext Stock Entry (Material Issue)
		stock_entry = frappe.new_doc("Stock Entry")
		stock_entry.stock_entry_type = "Material Issue"
		stock_entry.append("items", {
			"item_code": self.item,
			"qty": self.quantity,
			"s_warehouse": frappe.db.get_single_value("Stock Settings", "default_warehouse") or "Stores - MGSM"
		})
		stock_entry.insert()
		stock_entry.submit()
		frappe.msgprint(f"Stock Entry {stock_entry.name} created and submitted.")
