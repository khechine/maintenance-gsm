frappe.ui.form.on('Diagnostic Technique', {
    validation_client: function(frm) {
        if (frm.doc.validation_client) {
            frappe.confirm('Êtes-vous sûr de valider ce diagnostic? Cela créera automatiquement un Ordre de Réparation.',
                function() {
                    // Confirmed
                },
                function() {
                    // Cancelled
                    frm.set_value('validation_client', 0);
                }
            );
        }
    }
});