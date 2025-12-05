# ingredient_engine.py
import re
import os
import pandas as pd
from difflib import get_close_matches


# ------------------------------------------------------------
# OCR CLEANING (fix common OCR distortions)
# ------------------------------------------------------------
OCR_CORRECTIONS = {
    r'\bMea\b': 'Meal',
    r'\bEaible\b': 'Edible',
    r'\bPalmelein\b': 'Palmolein',
    r'\bCom\b': 'Corn',
    r'\bOrion\b': 'Onion',
    r'\btng\b': 'Ginger',
    r'ﬁ': 'fi',
}

def apply_ocr_corrections(text: str) -> str:
    """Fix common OCR mistakes before parsing."""
    s = text
    for patt, repl in OCR_CORRECTIONS.items():
        s = re.sub(patt, repl, s, flags=re.IGNORECASE)

    s = re.sub(r'\s+', ' ', s).strip()
    s = s.replace('\x0c', '')

    return s


# ------------------------------------------------------------
# SPLITTING ON TOP-LEVEL COMMAS (NOT inside parentheses)
# ------------------------------------------------------------
def split_top_level_commas(s: str):
    items = []
    buf = []
    depth = 0

    for ch in s:
        if ch == '(':
            depth += 1
            buf.append(ch)

        elif ch == ')':
            if depth > 0:
                depth -= 1
            buf.append(ch)

        elif ch == ',' and depth == 0:
            token = ''.join(buf).strip()
            if token:
                items.append(token)
            buf = []

        else:
            buf.append(ch)

    # final leftover
    token = ''.join(buf).strip()
    if token:
        items.append(token)

    # clean punctuation
    clean = [re.sub(r'^[\W_]+|[\W_]+$', '', it).strip() for it in items if it.strip()]
    return clean


# ------------------------------------------------------------
# PARSE INGREDIENT LIST FROM OCR TEXT
# ------------------------------------------------------------
def extract_ingredient_list_improved(raw_text: str):
    text = apply_ocr_corrections(raw_text)

    # Extract part after "INGREDIENTS:"
    m = re.search(r'ingredients[:\- ]*(.*)', text, re.IGNORECASE)
    if m:
        text = m.group(1)
    else:
        # fallback: take text after the first *
        m2 = re.search(r'\*(.*)', text, re.IGNORECASE)
        if m2:
            text = m2.group(1)

    # remove "CONTAINS ..." block
    text = re.split(r'\bcontains\b', text, flags=re.IGNORECASE)[0]

    # now safely split on top-level commas
    parts = split_top_level_commas(text)

    # cleanup each part
    final = []
    for it in parts:
        it = re.sub(r'\b\d+(\.\d+)?\s*%', '', it)
        it = it.strip(' .;')
        if it:
            final.append(it)

    return final


# ------------------------------------------------------------
# INGREDIENT ENGINE
# ------------------------------------------------------------
class IngredientEngine:

    def __init__(self, dataset_path=None):
        # autodetect dataset path next to this script
        if dataset_path is None:
            base = os.path.dirname(os.path.abspath(__file__))
            dataset_path = os.path.join(base, "custom_ingredient_dataset.csv")

        self.db = {}
        self._load_dataset(dataset_path)

    def _normalize(self, s):
        return re.sub(r'[^a-z0-9]', '', s.lower())

    def _load_dataset(self, path):
        df = pd.read_csv(path).fillna("")
        name_col = df.columns[0]

        for _, row in df.iterrows():
            name = str(row[name_col]).strip()
            key = self._normalize(name)
            self.db[key] = row.to_dict()

        self.keys = list(self.db.keys())

    def _find_match(self, ing):
        norm = self._normalize(ing)

        # exact match
        if norm in self.db:
            return self.db[norm]

        # fuzzy match
        matches = get_close_matches(norm, self.keys, n=1, cutoff=0.75)
        if matches:
            return self.db[matches[0]]

        return None

    # ------------------------------------------------------------
    # MAIN PUBLIC FUNCTION
    # ------------------------------------------------------------
    def analyze(self, raw_text: str):
        ingredient_list = extract_ingredient_list_improved(raw_text)
        result = {}

        for ing in ingredient_list:
            data = self._find_match(ing)

            if not data:
                result[ing] = {
                    "matched": None,
                    "verdict": "Unknown",
                    "note": "Not found in dataset"
                }
                continue

            sev = (data.get("severity", "")).lower()

            if sev in ["bad", "harmful", "high"]:
                verdict = "Bad"
            elif sev in ["moderate", "medium", "caution"]:
                verdict = "Moderate"
            elif sev in ["good", "safe", "low"]:
                verdict = "Good"
            else:
                verdict = "Unknown"

            result[ing] = {
                "matched": data.get("ingredient", ""),
                "severity": data.get("severity", ""),
                "category": data.get("category", ""),
                "note": data.get("note", ""),
                "score": data.get("score", ""),
                "verdict": verdict
            }

        return result
