import frappe
from frappe import _
from frappe.utils import now

class ReceptionAppareil(frappe.Document):
	def before_save(self):
		if not self.reference_qr:
			self.reference_qr = self.generate_unique_reference()
		if not self.code_barre:
			self.code_barre = self.reference_qr  # Use same value for barcode

	def on_submit(self):
		# Send notification to receptionniste
		self.send_notification("Reception Appareil Created", "Receptionniste")

	def generate_unique_reference(self):
		return frappe.generate_hash(length=8).upper()

	def send_notification(self, subject, role):
		users = frappe.get_users_with_role(role)
		if users:
			frappe.sendmail(
				recipients=users,
				subject=subject,
				message=f"New Reception Appareil created: {self.reference_qr}"
			)