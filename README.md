## 🧾 Payslip XML 2.0 Schema Validation (Pytest)

This project validates Finnish **Verkkopalkka "Payslip XML 2.0"** files against the official XML Schema (XSD) using **pytest** and **lxml**.

The tests ensure:
- ✅ **Valid** XML examples (from TIEKE spec) conform to the schema.
- ❌ **Invalid** samples fail validation, with clear, assertable error messages.

---

## 📁 Project Structure
```
payslip-xsd-validation/
├── ...
│
├── schemas/
│   └── payslipxml-2-0.xsd
├── tests/
│   ├── data/
│   │   ├── valid/
│   │   │   └── valid_payslip.xml
│   │   │   
│   │   └── invalid/
│   │       ├── extra_unexpected_tag.xml
│   │       ├── invalid_currency_code.xml
│   │       ├── malformed_structure.xml
│   │       ├── missing_required_element.xml
│   │       └── wrong_date_format.xml
│   │      
│   └── test_xsd_validation.py
│   
├── pytest.ini
├── requirements.txt
├── ci.yml
└── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone or download this repo

```bash
git clone https://github.com/JayKishoreDuvvuri/payslip-xsd-validation-pytest.git
cd payslip-xsd-validation
```

### 2️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Obtain the official XSD and sample XML
```bash
Download from the TIEKE website:
👉 https://tieke.fi/wp-content/uploads/2025/05/PayslipCommon20.zip

Unzip it, and copy:
PayslipCommon20.xsd → schemas/payslipxml-2-0.xsd
The example payslip XML → tests/data/valid/valid_payslip.xml
```
---

### 🧪 Running the Tests
```bash
pytest -s -v 
pytest -q

Pytest will:
Validate tests/data/valid/valid_payslip.xml → Should pass
Parameterize through tests/data/invalid/*.xml → Each should fail
```
---

### 📄 Notes & Assumptions
```bash
The schema and sample XMLs are property of TIEKE and must be downloaded manually.

The project assumes the PayslipCommon20.xsd schema corresponds to version 2.0 (22.5.2025).

All tests use the lxml library for schema validation.

Invalid test cases include:

 - Extra unexpected tag
 - Invalid currency code
 - Malformed structure
 - Missing required element
 - Wrong date format
```

### CI Run
```bash
https://github.com/JayKishoreDuvvuri/payslip-xsd-validation-pytest/actions
Run 1: https://github.com/JayKishoreDuvvuri/payslip-xsd-validation-pytest/actions/runs/18805583965/job/53659218845
Run 2: https://github.com/JayKishoreDuvvuri/payslip-xsd-validation-pytest/actions/runs/18805667385/job/53659411841
```