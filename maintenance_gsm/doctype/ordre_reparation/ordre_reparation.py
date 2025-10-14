import frappe
from frappe import _
from frappe.utils import now

class OrdreReparation(frappe.Document):
	def on_update(self):
		if self.statut == "Terminé":
			self.create_sales_invoice()
			self.update_reception_status()

	def create_sales_invoice(self):
		if not self.sales_invoice:
			invoice = frappe.new_doc("Sales Invoice")
			invoice.customer = frappe.db.get_value("Reception Appareil", self.reception, "client")
			total_cost = self.cout_main_oeuvre or 0
			for piece in self.pieces_utilisees:
				total_cost += piece.unit_cost * piece.qty
			invoice.append("items", {
				"item_name": f"Réparation {self.diagnostic}",
				"description": f"Réparation pour diagnostic {self.diagnostic}",
				"qty": 1,
				"rate": total_cost
			})
			invoice.insert()
			self.sales_invoice = invoice.name
			self.statut = "Facturé"
			frappe.msgprint(_("Facture de vente créée"))

	def update_reception_status(self):
		if self.diagnostic:
			diagnostic = frappe.get_doc("Diagnostic Technique", self.diagnostic)
			if diagnostic.reception:
				reception = frappe.get_doc("Reception Appareil", diagnostic.reception)
				reception.statut = "Terminé"
				reception.save()

	def before_submit(self):
		for piece in self.pieces_utilisees:
			if piece.piece:
				piece_doc = frappe.get_doc("Piece Detachee", piece.piece)
				piece_doc.stock_interne -= piece.qty
				piece_doc.save()
				if piece_doc.linked_item_code:
					# TODO: Integrate with ERPNext stock ledger
					pass