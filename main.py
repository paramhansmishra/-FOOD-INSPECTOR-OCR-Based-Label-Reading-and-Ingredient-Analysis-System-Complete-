# main.py (INTERACTIVE CLI VERSION)

import cv2
import pytesseract
import numpy as np
from PIL import Image

from ingredient_engine import IngredientEngine
from nutrition_engine import NutritionEngine
from ocr_test import nutrients


# ------------------------------------------------------------
# OCR Preprocessing (from your ocr_test.py)
# ------------------------------------------------------------
def preprocess_for_ocr(image_path):
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    denoised = cv2.bilateralFilter(gray, 7, 75, 75)
    thresh = cv2.adaptiveThreshold(
        denoised, 255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,15, 6)
    kernel = np.ones((1, 1), np.uint8)
    dilated = cv2.dilate(thresh, kernel, iterations=1)
    sharp = cv2.addWeighted(dilated, 1.5, gray, -0.5, 0)
    cv2.imshow('gray',gray)
    # cv2.imshow('denoised',denoised)
    cv2.imshow('thresh',thresh)
    cv2.imshow('dilated',dilated)
    cv2.imshow('sharp',sharp)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return sharp


def run_ocr(image_path):
    processed = preprocess_for_ocr(image_path)
    pil = Image.fromarray(processed)
    return pytesseract.image_to_string(pil)


# ------------------------------------------------------------
# Overall rating generator (simple scoring system)
# ------------------------------------------------------------
def get_overall_ingredient_rating(result_dict):
    score = 0

    for item, data in result_dict.items():
        verdict = data.get("verdict", "Unknown")

        if verdict == "Good":
            score += 1
        elif verdict == "Moderate":
            score += 0
        elif verdict == "Bad":
            score -= 1

    if score > 2:
        return "Healthy / Safe"
    elif score >= -1:
        return "Moderate"
    return "Unhealthy"


def get_overall_nutrition_rating(result_dict):
    issues = 0

    for item, data in result_dict.items():
        verdict = data.get("verdict", "").lower()

        if "high" in verdict or "harmful" in verdict:
            issues += 1

    if issues == 0:
        return "Nutrition Good"
    elif issues <= 2:
        return "Mixed / Moderate"
    return "Poor Nutrition"


# ------------------------------------------------------------
# SWITCH-LIKE COMMAND DISPATCHING
# ------------------------------------------------------------
def ingredient_handler():
    path = input("\nEnter the IMAGE PATH for Ingredient Analysis: ").strip()
    print("\nRunning OCR...")
    text = run_ocr(path)

    engine = IngredientEngine()
    result = engine.analyze(text)

    print("\n===== INGREDIENT ANALYSIS RESULTS =====")
    for ing, data in result.items():
        print(f"\n• {ing}")
        for k, v in data.items():
            print(f"   {k}: {v}")

    overall = get_overall_ingredient_rating(result)
    print("\n>>> OVERALL PRODUCT RATING:", overall)
    return 0


def nutrition_handler():
    path = input("\nEnter the IMAGE PATH for Nutrition Table: ").strip()
    print("\nRunning OCR...")
    raw_text = run_ocr(path)

    engine = NutritionEngine()
    result = engine.analyze(raw_text)

    print("\n===== NUTRITION ANALYSIS RESULTS =====")
    # show extracted nutrients and their values
    for k, v in result.items():
        # v is a dict now
        print(f"\n• {k}")
        print(f"   value: {v.get('value')}")
        if v.get('limit') is not None:
            print(f"   limit: {v.get('limit')}")
            print(f"   flag: {v.get('flag')}")
        print(f"   verdict: {v.get('verdict')}")
        if v.get('note'):
            print(f"   note: {v.get('note')}")

    overall = get_overall_nutrition_rating(result)
    print("\n>>> OVERALL NUTRITION RATING:", overall)
    return 0


switch = {
    "1": ingredient_handler,
    "2": nutrition_handler
}


# ------------------------------------------------------------
# MAIN PROGRAM LOOP
# ------------------------------------------------------------
def main():
    print("\n====== FOOD ANALYSIS CLI ======")
    print("1. Ingredient Analysis")
    print("2. Nutrition Analysis")

    choice = input("\nEnter your choice: ").strip()

    if choice in switch:
        switch[choice]()   # dispatch
    else:
        print("Invalid choice! Exiting.")


if __name__ == "__main__":
    main()
