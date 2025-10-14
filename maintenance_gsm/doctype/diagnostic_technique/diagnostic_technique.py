import frappe
from frappe import _

class DiagnosticTechnique(frappe.Document):
	def on_update(self):
		if self.validation_client:
			self.update_reception_status()
			self.create_ordre_reparation_if_not_exists()

	def update_reception_status(self):
		if self.reception:
			reception = frappe.get_doc("Reception Appareil", self.reception)
			reception.statut = "En diagnostic"
			reception.save()

	def create_ordre_reparation_if_not_exists(self):
		existing = frappe.db.exists("Ordre Reparation", {"diagnostic": self.name})
		if not existing:
			ordre = frappe.new_doc("Ordre Reparation")
			ordre.diagnostic = self.name
			ordre.reception = self.reception
			ordre.insert()
			frappe.msgprint(_("Ordre de Réparation créé automatiquement"))