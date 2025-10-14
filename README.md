# Maintenance GSM

A complete ERPNext app for managing mobile phone repair workshops.

## Features

- **Reception Management**: Handle customer device intake with QR code generation
- **Diagnostic Tracking**: Record technical issues and estimated costs
- **Repair Orders**: Manage repair workflows and parts consumption
- **Spare Parts Inventory**: Track spare parts and suppliers
- **Delivery Management**: Handle device return with customer signatures
- **Workflow Automation**: Automated status transitions and invoice creation
- **Dashboard**: Overview of repair statistics and KPIs
- **API Integration**: REST API for IMEI-based status queries

## Installation

### Prerequisites
- ERPNext v15
- Frappe Framework v15

### Install Steps

1. **Get the app**:
   ```bash
   bench get-app maintenance_gsm https://github.com/khechine/maintenance-gsm.git
   ```

2. **Install on site**:
   ```bash
   bench --site your-site-name install-app maintenance_gsm
   ```

3. **Migrate**:
   ```bash
   bench --site your-site-name migrate
   ```

## Setup

### Roles and Permissions

The app uses these roles:
- **Receptionniste**: Front desk operations
- **Technicien**: Technical repair work
- **Chef Atelier**: Workshop management
- **Comptable**: Financial operations

Assign roles via ERPNext Role Permissions Manager or via code.

### Sample Data

Create sample customer and test the workflow:

```bash
# Create customer
curl -X POST http://your-site:8000/api/resource/Customer \
  -H "Authorization: token your-api-key:your-api-secret" \
  -H "Content-Type: application/json" \
  -d '{
    "customer_name": "Client Test",
    "customer_type": "Individual"
  }'

# Create reception
curl -X POST http://your-site:8000/api/resource/Reception%20Appareil \
  -H "Authorization: token your-api-key:your-api-secret" \
  -H "Content-Type: application/json" \
  -d '{
    "client": "Client Test",
    "marque": "Apple",
    "modele": "iPhone 12",
    "imei": "123456789012345",
    "probleme_declare": "Écran cassé",
    "accessoires_fournis": "Chargeur"
  }'
```

### Test Workflow

1. Create Reception Appareil → Status: "En attente"
2. Create Diagnostic Technique and set `validation_client: true` → Creates Ordre Reparation automatically
3. Mark Ordre Reparation as "Terminé" → Creates Sales Invoice, sets Reception status to "Terminé"
4. Create Livraison Atelier → Sets Reception status to "Livrée"

### API Usage

Get status by IMEI:
```bash
curl http://your-site:8000/api/method/maintenance_gsm.api.get_status_by_imei?imei=123456789012345
```

## Doctypes

- **Reception Appareil**: Device intake and tracking
- **Diagnostic Technique**: Technical diagnosis with issues and estimates
- **Ordre Reparation**: Repair orders with parts and labor
- **Piece Detachee**: Spare parts inventory
- **Livraison Atelier**: Delivery and handover
- **Panne**: Issue tracking (child table)
- **Piece Usage**: Parts used in repairs (child table)

## Automation

- QR code and barcode generation for each reception
- Automatic invoice creation on repair completion
- Status workflow enforcement
- Email notifications on status changes
- Stock updates for parts consumption

## Print Formats

- **Bon de Réparation**: Printable receipt with QR code

## Dashboards

- **Atelier Overview**: Repair statistics and KPIs

## Notes

- Stock integration requires additional setup for full ERPNext stock ledger
- Notifications use ERPNext email templates
- Workflows can be customized via Workflow Builder