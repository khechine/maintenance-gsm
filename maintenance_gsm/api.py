import frappe
from frappe import _

@frappe.whitelist()
def get_status_by_imei(imei):
    """
    Get reception status by IMEI
    Returns reception record, last ordre_reparation status, last diagnostic summary
    """
    if not imei:
        frappe.throw(_("IMEI is required"))

    reception = frappe.db.get_value("Reception Appareil", {"imei": imei}, "*")
    if not reception:
        frappe.throw(_("No reception found for IMEI: {0}").format(imei))

    reception_doc = frappe.get_doc("Reception Appareil", reception.name)

    # Get last diagnostic
    diagnostic = frappe.get_all("Diagnostic Technique",
        filters={"reception": reception.name},
        fields=["name", "validation_client", "rapport_technique", "estimation_cout", "date_diagnostic"],
        order_by="creation desc",
        limit=1
    )

    # Get last ordre_reparation
    ordre = frappe.get_all("Ordre Reparation",
        filters={"diagnostic": ["in", [d.name for d in diagnostic]] if diagnostic else None},
        fields=["name", "statut", "sales_invoice", "date_fin"],
        order_by="creation desc",
        limit=1
    )

    result = {
        "reception": reception_doc.as_dict(),
        "last_diagnostic": diagnostic[0] if diagnostic else None,
        "last_ordre_reparation": ordre[0] if ordre else None
    }

    return result