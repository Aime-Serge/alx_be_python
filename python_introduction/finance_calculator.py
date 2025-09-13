# finance_calculator.py
# Calculates monthly savings and projects one-year savings with 5% interest.
monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))

monthly_savings = monthly_income - monthly_expenses
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

# Use the general format specifier 'g' to avoid unnecessary trailing .0 without using conditionals
print(f"Your monthly savings are ${monthly_savings:g}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings:g}.")
