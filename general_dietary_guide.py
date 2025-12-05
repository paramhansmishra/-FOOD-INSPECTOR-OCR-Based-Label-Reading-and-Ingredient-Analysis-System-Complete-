NUTRIENT_THRESHOLDS = {

    # ============================
    # EXISTING CORE NUTRIENTS
    # ============================
    "Total Fat, g": (17, "high", "Too much fat per 100g"),
    "Saturated fat, g": (5, "high", "Raises bad cholesterol"),
    "Trans Fat, g": (0, "harmful", "Even small amounts are harmful"),
    "Cholesterol, mg": (100, "caution", "Heart risk beyond 100mg/day"),
    "Sodium, mg": (600, "high", "Excess sodium linked to high BP"),
    "Added Sugar, g": (5, "high", "Added sugar should be minimal"),
    "Protein, g": (5, "low", "Too little protein per serving"),
    "Vitamin A, mcg": (600, "low", "Below ideal daily value (RDA ~900)"),

    # ============================
    # GENERAL MACROS
    # ============================
    "Calories, kcal": (250, "high", "High calorie density"),
    "Energy, kcal": (250, "high", "High calorie density"),
    "Carbohydrate, g": (30, "caution", "High carb content"),
    "Sugars, g": (10, "high", "High sugar intake is harmful"),
    "Total Carbohydrate, g": (30, "caution", "High carb content"),
    "Dietary Fiber, g": (3, "low", "Low fibre content"),

    # ============================
    # FATS & OILS
    # ============================
    "Omega 3, mg": (250, "low", "Low omega-3 fatty acids"),
    "Omega 6, mg": (5000, "caution", "Excess omega-6 may cause inflammation"),
    "Monounsaturated Fat, g": (10, "ok", "Healthy fat—moderate intake recommended"),
    "Polyunsaturated Fat, g": (10, "ok", "Healthy fat—moderate intake recommended"),

    # ============================
    # MINERALS
    # ============================
    "Calcium, mg": (300, "low", "Calcium below recommended intake"),
    "Iron, mg": (4, "low", "Low iron content"),
    "Magnesium, mg": (80, "low", "Low magnesium value"),
    "Potassium, mg": (300, "low", "Potassium content too low"),
    "Zinc, mg": (2, "low", "Low zinc content"),
    "Phosphorus, mg": (200, "low", "Low phosphorus content"),
    "Copper, mg": (0.3, "low", "Low copper value"),
    "Manganese, mg": (0.3, "low", "Low manganese value"),
    "Selenium, mcg": (20, "low", "Low selenium value"),
    "Iodine, mcg": (70, "low", "Low iodine content"),

    # ============================
    # VITAMINS
    # ============================
    "Vitamin C, mg": (20, "low", "Vitamin C value below RDA"),
    "Vitamin D, mcg": (5, "low", "Low vitamin D content"),
    "Vitamin E, mg": (2, "low", "Low vitamin E content"),
    "Vitamin K, mcg": (20, "low", "Low vitamin K content"),
    "Vitamin B1, mg": (0.5, "low", "Low thiamine (B1) content"),
    "Vitamin B2, mg": (0.5, "low", "Low riboflavin (B2) content"),
    "Vitamin B3, mg": (5, "low", "Low niacin (B3) content"),
    "Vitamin B5, mg": (2, "low", "Low pantothenic acid (B5) content"),
    "Vitamin B6, mg": (0.5, "low", "Low vitamin B6 content"),
    "Vitamin B7, mcg": (20, "low", "Low biotin (B7) value"),
    "Vitamin B9, mcg": (80, "low", "Low folate (B9) content"),
    "Vitamin B12, mcg": (1, "low", "Low vitamin B12 content"),

    # ============================
    # AMINO ACIDS
    # ============================
    "Lysine, mg": (100, "low", "Low lysine content"),
    "Leucine, mg": (150, "low", "Low leucine content"),
    "Valine, mg": (100, "low", "Low valine content"),
    "Isoleucine, mg": (100, "low", "Low isoleucine content"),

    # ============================
    # SUGAR TYPES
    # ============================
    "Sucrose, g": (5, "high", "High sucrose content"),
    "Glucose, g": (5, "high", "High glucose value"),
    "Fructose, g": (5, "high", "High fructose intake is harmful"),
    "Lactose, g": (5, "caution", "May affect lactose-intolerant individuals"),
    "Maltose, g": (5, "high", "High maltose level"),

    # ============================
    # SPECIAL METRICS
    # ============================
    "Glycemic Index": (60, "high", "High GI foods spike blood sugar"),
    "Glycemic Load": (10, "high", "High GL is harmful for diabetics"),

    # ============================
    # OTHER LABEL ITEMS
    # ============================
    "Moisture, g": (5, "ok", "Healthy moisture level"),
    "Ash, g": (2, "ok", "Normal ash content"),
    "Sodium Chloride, g": (1, "caution", "Extra hidden salt content"),
    "Salt Equivalent, g": (2, "high", "Excess salt"),
    "Caffeine, mg": (80, "caution", "High caffeine per serving"),
    "Taurine, mg": (400, "caution", "High taurine level (energy drinks)"),
    "Creatine, mg": (3000, "ok", "Creatine safe threshold"),

    # ============================
    # FORTIFIED FOODS
    # ============================
    "Folic Acid, mcg": (80, "low", "Low folic acid content"),
    "Niacinamide, mg": (5, "low", "Below recommended niacin levels"),
    "Riboflavin, mg": (0.5, "low", "Below recommended riboflavin levels"),
    "Thiamine, mg": (0.5, "low", "Low thiamine content"),

    # ============================
    # OILS / FATTY ACIDS EXTRA
    # ============================
    "Lauric Acid, g": (3, "caution", "High lauric acid content"),
    "Myristic Acid, g": (2, "caution", "Raises LDL cholesterol"),
    "Palmitic Acid, g": (3, "caution", "Unhealthy saturated fat"),
    "Stearic Acid, g": (2, "ok", "Neutral saturated fat"),

}
