frappe.ui.form.on('Ordre Reparation', {
    refresh: function(frm) {
        // Display computed repair total
        if (frm.doc.pieces_utilisees || frm.doc.cout_main_oeuvre) {
            let total = frm.doc.cout_main_oeuvre || 0;
            (frm.doc.pieces_utilisees || []).forEach(piece => {
                total += (piece.qty || 0) * (piece.unit_cost || 0);
            });
            frm.dashboard.add_section(`
                <div class="repair-total">
                    <h4>Total réparation estimé: ${total} DT</h4>
                </div>
            `, __("Résumé"));
        }

        // Add button to create invoice manually if not created
        if (frm.doc.statut === 'Terminé' && !frm.doc.sales_invoice) {
            frm.add_custom_button(__('Créer Facture'), function() {
                frappe.confirm('Créer une facture de vente pour cette réparation?',
                    function() {
                        frm.call('create_sales_invoice');
                    }
                );
            });
        }
    },

    statut: function(frm) {
        if (frm.doc.statut === 'Terminé') {
            frappe.confirm('Marquer cette réparation comme terminée créera automatiquement une facture.',
                function() {
                    // Confirmed
                },
                function() {
                    // Cancelled
                    frm.set_value('statut', 'En cours');
                }
            );
        }
    }
});