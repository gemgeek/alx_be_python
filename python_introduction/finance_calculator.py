income = float(input("Enter your monthly income: "))
expenses = float(input("Enter your monthly expenses: "))
monthly_savings = income - expenses
annual_savings = monthly_savings * 12
interest = annual_savings * 0.05
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)
print(f"Your monthly savings are ${monthly_savings:.0f}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings:.0f}.")
