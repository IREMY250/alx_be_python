monthly_income = float(input("Enter your monthly income:"))
total_monthly_expenses = float(input("Enter your total monthly expenses:"))
monthly_savings = monthly_income - total_monthly_expenses
annual_interest_rate = 0.05
Projected_Savings = (monthly_savings * 12) + ( monthly_savings * 12 * 0.05)
print(f"the monthly savings is:{monthly_savings}")
print (f"the projected savings is :{Projected_Savings}")
