import frappe
from frappe import _

class LivraisonAtelier(frappe.Document):
	def on_submit(self):
		self.update_reception_status()

	def update_reception_status(self):
		if self.ordre_reparation:
			ordre = frappe.get_doc("Ordre Reparation", self.ordre_reparation)
			if ordre.diagnostic:
				diagnostic = frappe.get_doc("Diagnostic Technique", ordre.diagnostic)
				if diagnostic.reception:
					reception = frappe.get_doc("Reception Appareil", diagnostic.reception)
					reception.statut = "Livré"
					reception.save()