# future_age_calculator.py
# Ask user for current age and compute age in 2050 (assuming current year 2023).
age_str = input("How old are you? ")
age = int(age_str)  # assumption: user inputs a valid integer
age_in_2050 = age + 27

print(f"In 2050, you will be {age_in_2050} years old.")
