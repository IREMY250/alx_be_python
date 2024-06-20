monthly_income = float(input("Enter your monthly income:"))
monthly_expenses = float(input("Enter your total monthly expenses:"))
monthly_savings = monthly_income - monthly_expenses
annual_savings = monthly_savings * 12
Projected_Savings = (monthly_savings * 12) + ( monthly_savings * 12 * 0.05)
print(f"the monthly savings is:{monthly_savings}")
print (f"the projected savings is :{Projected_Savings}")
