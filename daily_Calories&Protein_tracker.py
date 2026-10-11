# Standard data per 100g
FOOD_TABLE = {
    "rice (cooked)": (130, 2.7),
    "chicken breast (cooked)": (165, 31.0),
    "chicken (cooked)": (175, 25.0),
    "soya chunks": (345, 52.0),
    "egg (2-whole)": (143, 12.6),
    "banana": (89, 1.1),
    "whole wheat bread": (247, 13.0),
    "milk (whole)": (61, 3.2),
    "salmon / fish (cooked)": (206, 22.0),
    "potato (boiled)": (87, 1.9),
    "apple": (52, 0.3),
    "lean beef (cooked)": (250, 26.0)
}


def get_float_input(prompt: str, min_val: float = 0.0) -> float:
    """Helper function to safely handle numeric user inputs."""
    while True:
        try:
            val = float(input(prompt))
            if val < min_val:
                print(f"Please enter a value greater than or equal to {min_val}.")
                continue
            return val
        except ValueError:
            print("Invalid entry. Please enter a valid number.")


def get_choice_input(prompt: str, valid_choices: list[str]) -> str:
    """Helper function to enforce selection from valid options."""
    while True:
        choice = input(prompt).strip().upper()
        if choice in valid_choices:
            return choice
        print(f"Invalid choice. Please select from: {', '.join(valid_choices)}")


# User Profile
print("--- Daily Calories & Protein Tracker ---")
name = input("Enter your name: ").strip() or "User"
age = int(get_float_input("Enter your age: ", min_val=1))
weight = get_float_input("Enter your weight in kg: ", min_val=1.0)
height = get_float_input("Enter your height in cm: ", min_val=1.0)

print("\nGender:\nA. Male\nB. Female")
gender = get_choice_input("Choose your gender (A/B): ", ["A", "B"])

print("\nActivity Levels:")
print("A. Low (little or no exercise)")
print("B. Light (light exercise 1-3 days/week)")
print("C. Moderate (moderate exercise 3-5 days/week)")
print("D. High (hard exercise 6-7 days/week)")
activity = get_choice_input("Choose your activity level (A/B/C/D): ", ["A", "B", "C", "D"])

# BMR Calculation
if gender == "A":
    bmr = (10 * weight) + (6.25 * height) - (5 * age) + 5
else:
    bmr = (10 * weight) + (6.25 * height) - (5 * age) - 161

# Activity 
activity_multipliers = {"A": 1.2, "B": 1.375, "C": 1.55, "D": 1.725}
target_calories = bmr * activity_multipliers[activity]
target_protein = weight * 1.2

# User Summary
print("\n" + "=" * 45)
print(f" Hello, {name}!")
print(f" Estimated BMR:          {round(bmr)} kcal/day")
print(f" Daily Calorie Target:   {round(target_calories)} kcal/day")
print(f" Daily Protein Target:   {round(target_protein - 10)} - {round(target_protein)} grams/day")
print("=" * 45)

# Display Food Reference Table
print("\nFood Reference Table (per 100g)")
print("-" * 48)
print(f"{'Food Item':<25} {'Calories (kcal)':<15} {'Protein (g)':<10}")
print("-" * 48)
for food, (cal, pro) in FOOD_TABLE.items():
    print(f"{food.title():<25} {cal:<15} {pro:<10}")
print("-" * 48)

# Log Consumed Food
food_calories = 0.0
food_protein = 0.0

n = int(get_float_input("\nHow many food items did you eat today? ", min_val=0))

for i in range(n):
    print(f"\nItem #{i + 1}:")
    fname = input("Enter food name: ").strip().lower()

    # Search for matching item key in reference table
    matched_key = next((key for key in FOOD_TABLE if fname in key), None)

    if matched_key:
        amount = get_float_input(f"How many grams of '{matched_key.title()}' did you eat? ", min_val=0.0)
        cal_per_100g, pro_per_100g = FOOD_TABLE[matched_key]
    else:
        print(f"'{fname.title()}' is not in the table. Let's enter custom nutrition details.")
        add_custom = get_choice_input("Would you like to enter values manually? (Y/N): ", ["Y", "N"])
        
        if add_custom == "Y":
            cal_per_100g = get_float_input("Enter calories per 100g (kcal): ", min_val=0.0)
            pro_per_100g = get_float_input("Enter protein per 100g (grams): ", min_val=0.0)
            amount = get_float_input("How many grams did you eat? ", min_val=0.0)
        else:
            print("Skipped item.")
            continue

    item_calories = (cal_per_100g * amount) / 100
    item_protein = (pro_per_100g * amount) / 100

    food_calories += item_calories
    food_protein += item_protein
    print(f" Added: {round(item_calories, 1)} kcal, {round(item_protein, 1)}g protein")

# Daily Summary Results
print("\n" + "=" * 45)
print(" DAILY INTAKE SUMMARY")
print("=" * 45)
print(f" Total Calories Consumed: {round(food_calories, 1)} / {round(target_calories)} kcal")
print(f" Total Protein Consumed:  {round(food_protein, 1)} / {round(target_protein)} g")
print("-" * 45)

# Calorie Status
cal_diff = food_calories - target_calories
if abs(cal_diff) <= 100:
    print(" Calories: You hit your daily energy target almost exactly!")
elif cal_diff > 100:
    print(f" Calories: You are OVER your maintenance target by {round(cal_diff)} kcal.")
else:
    print(f" Calories: You are UNDER your target by {round(abs(cal_diff))} kcal.")

# Protein Status
pro_diff = target_protein - food_protein
if pro_diff <= 10:
    print(" Protein:  Great job! You reached your daily protein goal.")
else:
    print(f" Protein:  You need approximately {round(target_protein-10, 1)}g more protein today.")
print("=" * 45)
