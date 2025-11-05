def determine_insurance_plan():
    print("Welcome to the Insurance Plan Selector!")

    # Inputs
    age = int(input("Enter your age: "))
    income = float(input("Enter your annual income: "))
    marital_status = input("Are you single or married? (Enter 'single' or 'married'): ").strip().lower()
    has_children = input("Do you have children? (yes/no): ").strip().lower()
    health_level = input("Do you visit the doctor a lot or have any chronic illness? (yes/no): ").strip().lower()

    # eligibility
    if age <= 18:
        print("Sorry, you do not qualify for any plans.")
        return


    util_low = (health_level == "no")
    married = (marital_status == "married")
    family = married and (has_children == "yes")
    scope = "Family" if family else "Individual"

    if not married:
        low_income = income < 35000
        segment = "single_individual"
    elif family:
        low_income = income < 65000
        segment = "married_family"
    else:
        low_income = False
        segment = "married_individual"

    income_high = income > 50000

    plans = {
        "High-Deductible A": {"deductible": "3500/person, 7500/family", "coverage": "80% after deductible", "cost": "1100/month individual, 2300/month family"},
        "High-Deductible B": {"deductible": "4500/person, 9500/family", "coverage": "80% after deductible", "cost": "800/month individual, 1800/month family"},
        "Regular Plan A":    {"deductible": "1500/person, 3500/family", "coverage": "80% after deductible", "cost": "2800/month individual, 3800/month family"},
        "Regular Plan B":    {"deductible": "1500/person, 3500/family", "coverage": "90% after deductible", "cost": "3500/month individual, 4800/month family"},
        "Low Income Plan":   {"deductible": "No deductible",             "coverage": "90% coverage",          "cost": "1000/month individual, 2000/month family"},
    }

    def print_plan_details(plan_name):
        print(f"\nPlan: {plan_name}")
        print(f"  Deductible: {plans[plan_name]['deductible']}")
        print(f"  Coverage:   {plans[plan_name]['coverage']}")
        print(f"  Cost:       {plans[plan_name]['cost']}")

    def recommend(primary, alternate):
        print(f"\nRecommended Plan: {primary} ({scope})")
        print_plan_details(primary)
        print(f"\nAlternate Plan: {alternate} ({scope})")
        print_plan_details(alternate)

    # (segment, low_income, income_high, util_low)
    rules = {
        # Single (Individual)
        ("single_individual", True,  None, True):  ("Low Income Plan", "High-Deductible B"),  # income < 35k, low util
        ("single_individual", True,  None, False): ("Low Income Plan", "Regular Plan A"),     # income < 35k, high util

        ("single_individual", False, True,  True):  ("High-Deductible B", "High-Deductible A"),  # >50k, low util
        ("single_individual", False, False, True):  ("High-Deductible A", "Regular Plan A"),     # <=50k, low util
        ("single_individual", False, True,  False): ("Regular Plan A", "Regular Plan B"),        # >50k, high util
        ("single_individual", False, False, False): ("Regular Plan B", "High-Deductible A"),     # <=50k, high util

        # married + children (Family)
        ("married_family", True,  None, True):  ("Low Income Plan", "High-Deductible A"),  # income < 65k, low util
        ("married_family", True,  None, False): ("Low Income Plan", "Regular Plan A"),     # income < 65k, high util

        ("married_family", False, True,  True):  ("High-Deductible A", "High-Deductible B"),  # >50k, low util
        ("married_family", False, False, True):  ("High-Deductible B", "Regular Plan A"),     # <=50k, low util
        ("married_family", False, True,  False): ("Regular Plan A", "Regular Plan B"),        # >50k, high util
        ("married_family", False, False, False): ("Regular Plan B", "High-Deductible A"),     # <=50k, high util

        # married no children (Individual)
        ("married_individual", False, True,  True):  ("High-Deductible A", "High-Deductible B"),  # >50k, low util
        ("married_individual", False, True,  False): ("Regular Plan B", "Regular Plan A"),        # >50k, high util
        ("married_individual", False, False, True):  ("High-Deductible B", "High-Deductible A"),  # <=50k, low util
        ("married_individual", False, False, False): ("Regular Plan A", "Regular Plan B"),        # <=50k, high util
    }

    key = (
        segment,
        low_income,
        (None if low_income else income_high),
        util_low
    )

    primary, alternate = rules[key]
    recommend(primary, alternate)


# Run the program
if __name__ == "__main__":
    determine_insurance_plan()
