frappe.ui.form.on('Reception Appareil', {
    refresh: function(frm) {
        // Auto-fill date_reception on refresh if not set
        if (!frm.doc.date_reception) {
            frm.set_value('date_reception', frappe.datetime.now_datetime());
        }

        // Disable IMEI edit after submit
        if (frm.doc.docstatus === 1) {
            frm.set_df_property('imei', 'read_only', 1);
        }

        // Show QR code and barcode preview
        if (frm.doc.reference_qr && frm.doc.code_barre) {
            frm.dashboard.add_section(`
                <div class="codes-preview">
                    <h4>Codes de suivi:</h4>
                    <div style="display: flex; justify-content: center; gap: 20px;">
                        <div>
                            <p><strong>QR Code:</strong></p>
                            <img src="/api/method/maintenance_gsm.api.generate_qr?text=${encodeURIComponent(frm.doc.reference_qr)}" alt="QR Code" style="max-width: 100px;">
                            <p>${frm.doc.reference_qr}</p>
                        </div>
                        <div>
                            <p><strong>Code Barre:</strong></p>
                            <img src="/api/method/maintenance_gsm.api.generate_barcode?text=${encodeURIComponent(frm.doc.code_barre)}" alt="Barcode" style="max-width: 150px; height: 50px;">
                            <p>${frm.doc.code_barre}</p>
                        </div>
                    </div>
                </div>
            `, __("Informations"));
        }
    },

    imei: function(frm) {
        // Validate IMEI uniqueness
        if (frm.doc.imei) {
            frappe.call({
                method: 'frappe.client.get_list',
                args: {
                    doctype: 'Reception Appareil',
                    filters: { imei: frm.doc.imei },
                    fields: ['name']
                },
                callback: function(r) {
                    if (r.message && r.message.length > 0 && r.message[0].name !== frm.doc.name) {
                        frappe.msgprint(__('IMEI déjà utilisé dans une autre réception'));
                        frm.set_value('imei', '');
                    }
                }
            });
        }
    }
});