🍽️ FOOD INSPECTOR -- OCR-Based Ingredient & Nutrition Analysis
==============================================================

A computer-vision powered system that automatically extracts **ingredient lists** and **nutrition tables** from food package images using OCR, and evaluates them using domain-specific rules.

This project simplifies food label understanding by detecting harmful ingredients, unhealthy nutrient levels, and giving an easy-to-read "Product Rating".

* * * * *

🧠 Project Motivation
---------------------

Food labels are confusing. Ingredients are hidden under marketing terms, and nutrition tables are difficult to interpret at a glance.

This project solves that by providing:

✔ Automated OCR extraction\
✔ Ingredient danger assessment\
✔ Nutrition threshold analysis\
✔ Clean CLI workflow\
✔ Extendable datasets for ingredients & nutrition

* * * * *

🚀 Features
===========

### 🔍 **1\. OCR-Powered Ingredient Detection**

-   Parses unstructured ingredient images

-   Fixes OCR mistakes intelligently

-   Splits ingredients correctly using **top-level comma detection**

-   Keeps parentheses groups intact

-   Matches against a curated CSV dataset

-   Assigns verdicts: **Good / Moderate / Bad / Unknown**

* * * * *

### 📊 **2\. Nutrition Table Extraction**

-   Reads nutrition tables from images using OpenCV preprocessing + Tesseract

-   Automatically reconstructs missing line breaks

-   Extracts nutrient → value pairs

-   Fuzzy matches to dietary threshold rules

-   Generates verdicts:

    -   **High**

    -   **Low**

    -   **Caution**

    -   **Harmful**

    -   **OK**

* * * * *

### 🤖 **3\. Interactive CLI**

When you run the project, you get:

`====== FOOD ANALYSIS CLI ======
1. Ingredient Analysis
2. Nutrition Analysis`

You simply choose an option, provide a cropped image, and the system prints structured results + an overall rating.

* * * * *

### 📁 **4\. Clean Modular Architecture**

`Food Inspector/
│── main.py                     ← CLI + OCR control
│── ingredient_engine.py        ← Ingredient parsing + verdict logic
│── nutrition_engine.py         ← Nutrition table analyzer
│── general_dietary_guide.py    ← Nutrient thresholds
│── custom_ingredient_dataset.csv← Ingredient danger levels
│── test_images/                ← Sample images
│── requirements.txt
│── README.md`

* * * * *

### 📦 **5\. Extendable Datasets**

-   Ingredient dataset (CSV): can add any number of ingredients, additives, oils, etc.

-   Nutrition thresholds: fully editable via `general_dietary_guide.py`

-   Clean pipeline for adding future ML models / RDA tables

* * * * *

📸 How it Works
===============

### **1\. OCR Preprocessing (OpenCV)**

-   grayscale

-   bilateral filtering

-   adaptive threshold

-   dilation

-   sharpening

Produces high-contrast text for Tesseract.

* * * * *

### **2\. Text Extraction**

Performed using:

`pytesseract.image_to_string(...)`

* * * * *

### **3\. Ingredient Parsing**

-   Cleans OCR noise

-   Identifies ingredient section

-   Splits at commas **only at top-level**

-   Keeps content inside `(...)` together

-   Applies fuzzy matching to dataset

* * * * *

### **4\. Nutrition Parsing**

-   Fixes missing line breaks in OCR output

-   Uses regex to find `"name value"` patterns

-   Fuzzy matches to known nutrient keys

-   Applies thresholds (high/low/caution/harmful/ok)

-   Returns structured JSON-like result

* * * * *

📈 Example Outputs
==================

### **Ingredient Analysis Example**

`- Palmolein Oil
   severity: Bad
   note: Increases inflammation
   verdict: Bad

- Sugar
   severity: Moderate
   note: Added sugar risk
   verdict: Moderate

Overall Product Rating: Moderate`

* * * * *

### **Nutrition Analysis Example**

`- Total Fat, g
   value: 80.0
   limit: 17
   verdict: High - Too much fat per 100g

- Sodium, mg
   value: 836
   verdict: High - Excess sodium linked to high BP

Overall Nutrition Rating: Poor Nutrition`

* * * * *

🛠️ Installation
================

### 1\. Clone the repository

`git clone https://github.com/<your-username>/Food-Inspector-OCR.git
cd Food-Inspector-OCR`

### 2\. Install dependencies

`pip install -r requirements.txt`

### 3\. Install Tesseract OCR

**Windows:**\
Download from: https://github.com/UB-Mannheim/tesseract/wiki\
Add to PATH:

`C:\Program Files\Tesseract-OCR\`

* * * * *

🎮 Usage
========

Run the CLI:

`python main.py`

Upload a **cropped image** of either:

-   ingredient list

-   nutrition table

The system will automatically analyze and print your results.

* * * * *

⚠️ Known Limitations
====================

-   OCR quality depends heavily on image clarity and cropping

-   Some rare ingredients may not exist in dataset → verdict = Unknown

-   Complex nutrition tables with multiple columns (e.g., per 100g & per serving) are not yet fully supported

-   Regional language labels are not supported yet (English only)

* * * * *

🔮 Future Work (Planned)
========================

### ⭐ 1. **ICMR RDA Integration**

Implement full comparison of nutrition table values vs.\
ICMR Recommended Dietary Allowances (for age, gender, pregnancy, lactation).

### ⭐ 2. Multi-language OCR

Support for Hindi, Tamil, Bengali, etc.

### ⭐ 3. Web UI / Mobile App

Using Streamlit or Flutter.

### ⭐ 4. Product Health Score

Combined rating from:

-   ingredient safety

-   nutrient thresholds

-   RDA contribution

### ⭐ 5. Neural OCR for curved packages

Using deep-learning text detectors.

* * * * *

❤️ Credits
==========

Developed by **Param**\
M.Tech -- Computer Science Engineering\
Delhi Technological University (DTU)

* * * * *

🎯 Conclusion
=============

Food Inspector turns **raw food labels** into **clear, actionable insights** using OCR + rule engines.\
Perfect for academic projects, consumer health tools, and real-world applications.
