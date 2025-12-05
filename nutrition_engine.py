# nutrition_engine.py
import re
from general_dietary_guide import NUTRIENT_THRESHOLDS

class NutritionEngine:

    # ------------------------------------------------------------
    # Fix OCR text: restore missing line breaks
    # ------------------------------------------------------------
    def clean_text(self, text: str) -> str:
        text = text.replace("\x0c", "")

        # Insert newline before capitalized nutrient names (Energy, Total, Saturated...)
        text = re.sub(r"(?<!\n)([A-Z][a-z]+[^0-9])", r"\n\1", text)

        # Insert newline when a number is followed by a letter (650Vitamin)
        text = re.sub(r"(\d)([A-Za-z])", r"\1\n\2", text)

        # Normalize whitespace
        text = re.sub(r"\n+", "\n", text)
        text = re.sub(r"[ ]+", " ", text)

        return text.strip()

    # ------------------------------------------------------------
    # Extract nutrient-value pairs using OCR-test regex
    # ------------------------------------------------------------
    def extract_pairs(self, text: str):
        nutrient = {}
        lines = text.split("\n")

        for line in lines:
            line = line.strip()
            # original working regex from ocr_test.py
            m = re.search(r"(.+?)\s[-:]?\s?(\d+\.?\d*)$", line)
            if m:
                key = m.group(1).strip()
                value = float(m.group(2))
                nutrient[key] = value

        return nutrient

    # ------------------------------------------------------------
    # Fuzzy match key to dietary guide
    # ------------------------------------------------------------
    def match_key(self, raw_key):
        norm = re.sub(r"[^a-z0-9]", "", raw_key.lower())
        for k in NUTRIENT_THRESHOLDS:
            knorm = re.sub(r"[^a-z0-9]", "", k.lower())
            if norm == knorm or norm in knorm or knorm in norm:
                return k
        return None

    # ------------------------------------------------------------
    # Main analysis function
    # ------------------------------------------------------------
    def analyze(self, raw_text: str):

        text = self.clean_text(raw_text)
        nutrients = self.extract_pairs(text)

        result = {}

        for raw_key, val in nutrients.items():
            match = self.match_key(raw_key)

            if match is None:
                result[raw_key] = {
                    "value": val,
                    "limit": None,
                    "flag": None,
                    "note": None,
                    "verdict": "No rule found"
                }
                continue

            limit, flag, note = NUTRIENT_THRESHOLDS[match]

            # same logic as your ocr_test.py
            if flag == "high" and val > limit:
                verdict = f"High - {note}"
            elif flag == "low" and val < limit:
                verdict = f"low - {note}"
            elif flag == "caution" and val > limit:
                verdict = f"Carefull - {note}"
            elif flag == "harmful" and val > limit:
                verdict = f"Avoid Immidiately - {note}"
            else:
                verdict = "OK"

            result[match] = {
                "value": val,
                "limit": limit,
                "flag": flag,
                "note": note,
                "verdict": verdict
            }

        return result
