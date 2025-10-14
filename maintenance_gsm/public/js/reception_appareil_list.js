frappe.listview_settings['Reception Appareil'] = {
    get_indicator: function(doc) {
        if (doc.statut === 'En attente') {
            return [__("En attente"), "orange", "statut,=,En attente"];
        } else if (doc.statut === 'En diagnostic') {
            return [__("En diagnostic"), "yellow", "statut,=,En diagnostic"];
        } else if (doc.statut === 'En réparation') {
            return [__("En réparation"), "blue", "statut,=,En réparation"];
        } else if (doc.statut === 'Terminé') {
            return [__("Terminé"), "green", "statut,=,Terminé"];
        } else if (doc.statut === 'Livré') {
            return [__("Livré"), "grey", "statut,=,Livré"];
        }
    }
};