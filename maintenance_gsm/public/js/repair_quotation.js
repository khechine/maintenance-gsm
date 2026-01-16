frappe.ui.form.on('Repair Quotation', {
    labor_cost: function (frm) {
        calculate_total(frm);
    }
});

frappe.ui.form.on('Quotation Spare Part', {
    qty: function (frm, cdt, cdn) {
        let item = locals[cdt][cdn];
        frappe.model.set_value(cdt, cdn, 'amount', item.qty * item.rate);
        calculate_total(frm);
    },
    rate: function (frm, cdt, cdn) {
        let item = locals[cdt][cdn];
        frappe.model.set_value(cdt, cdn, 'amount', item.qty * item.rate);
        calculate_total(frm);
    },
    spare_parts_remove: function (frm) {
        calculate_total(frm);
    }
});

var calculate_total = function (frm) {
    let total_parts = 0;
    (frm.doc.spare_parts || []).forEach(item => {
        total_parts += item.amount;
    });
    frm.set_value('total_estimated_cost', (frm.doc.labor_cost || 0) + total_parts);
}
