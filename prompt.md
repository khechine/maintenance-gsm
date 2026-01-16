You are a senior ERPNext / Frappe architect.

Design and generate a professional ERPNext application named
**maintenance_gsm**, intended for real-world GSM repair workshops.

Target:
- ERPNext v16
- Frappe v16
- Docker-based deployment
- Production-ready structure

--------------------------------------------------
1. APPLICATION STRUCTURE
--------------------------------------------------
- Framework: frappe
- App name: maintenance_gsm
- Display name: Maintenance GSM
- Module: Maintenance GSM
- Multilingual ready (fr / en)
- Clean separation between ERPNext core and custom logic

--------------------------------------------------
2. CORE BUSINESS OBJECTS (DOCTYPES)
--------------------------------------------------

### A. Appareil
Purpose: Track customer devices across their lifecycle.

Fields:
- imei (Data, unique, required)
- brand (Select)
- model (Data)
- customer (Link → Customer)
- reception_date (Date)
- physical_condition (Text)
- status (Select: Reçu, En réparation, Prêt, Livré)

Enable:
- History of repairs
- List view optimized for reception desk

--------------------------------------------------

### B. Repair Order
Purpose: Operational repair workflow.

Fields:
- device (Link → Appareil)
- technician (Link → Employee)
- priority (Low, Medium, High)
- status (Workflow-based)
- opened_on (Datetime)
- closed_on (Datetime)
- internal_notes (Text)

Workflow:
- Reçu → Diagnostic → Devis → En cours → Terminé → Livré

--------------------------------------------------

### C. Technical Diagnostic
Purpose: Structured technical analysis.

Fields:
- repair_order (Link → Repair Order)
- symptoms (Text)
- root_cause (Text)
- severity (Low, Medium, Critical)
- estimated_time (Duration)
- created_by (Link → User)

Auto-create this document when a Repair Order is opened.

--------------------------------------------------

### D. Repair Quotation
Purpose: Commercial validation before repair.

Fields:
- repair_order (Link → Repair Order)
- labor_cost (Currency)
- spare_parts (Child Table → ERPNext Item + qty)
- total_estimated_cost (Currency)
- customer_approval (Check)

Actions:
- Convert to ERPNext Sales Invoice
- Lock repair until approval

--------------------------------------------------

### E. Spare Parts Consumption
Purpose: Stock integration.

Fields:
- repair_order (Link)
- item (Link → Item)
- quantity (Float)

On submit:
- Create ERPNext Stock Entry (Material Issue)

--------------------------------------------------
3. AUTOMATIONS & HOOKS
--------------------------------------------------
- Auto-create Diagnostic on Repair Order creation
- Block repair progress if quotation not approved
- Notify customer on:
  - Diagnostic completed
  - Repair finished

--------------------------------------------------
4. WEB & CUSTOMER INTERFACE
--------------------------------------------------
- Public page: /repair-status
- Input: IMEI
- Output: repair status, messages
- Secure and read-only

--------------------------------------------------
5. ROLES & PERMISSIONS
--------------------------------------------------
- GSM Receptionist
- GSM Technician
- Workshop Manager

--------------------------------------------------
6. OUTPUT EXPECTATIONS
--------------------------------------------------
- Full folder structure
- Doctype schemas
- hooks.py
- Workflow definitions
- Sample fixtures
- Bench install instructions
