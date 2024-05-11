import numpy
import math

# Total cost of the house
# total_cost = 1
# Down payment of the house
portion_down_payment = 0.25
# Current money saved
#current_savings = 0
# Annual return rate
r = 0.04
# Annual salary
# annual_salary = 0
# Certain percentage of salary saved for down payment
# portion_saved = 0.01

# At end of month, savings will be increased by return on investment plus percentage of monthly salary

# Write a program to calculate how many months needed to save money for down payment
# The program should ask for
# 1. Annual salary (annual_salary)
# 2. Portion of salary to be saved (portion_saved)
# 3. Cost of home (total_cost)
# 4. The rate of semi annual raise (semi_annual_raise)

#annual_salary = input("Enter your annual salary: ")
#portion_saved = input("Enter the percent of your salary to be saved, as a decimal: ")
#total_cost = input("Enter the cost of your dream home: ")
#semi_annual_raise = input("Enter the semi-annual raise, as decimal: ")

#total_down_payment = portion_down_payment * float(total_cost)
#print(f"Total down payment: {total_down_payment}")
#monthly_salary = float(annual_salary)/12
#monthly_return_rate = r/12
#monthly_saved = monthly_salary * float(portion_saved)
#months = 0
#while current_savings < total_down_payment:
# if months != 0 and months % 6 == 0:
#	 monthly_salary = monthly_salary * (1 + float(semi_annual_raise))
#	 monthly_saved = monthly_salary * float(portion_saved)
#	current_savings += current_savings * monthly_return_rate
#	current_savings += monthly_saved
#	months += 1
#print(f"Total months: {months}")

# The algorithm as a function
def months_to_save(annual_salary, portion_saved, total_cost, semi_annual_raise):
	current_savings = 0
	total_down_payment = portion_down_payment * float(total_cost)
	print(f"Total down payment: {total_down_payment}")
	monthly_salary = float(annual_salary)/12
	monthly_return_rate = r/12
	monthly_saved = monthly_salary * float(portion_saved)
	months = 0
	while current_savings < total_down_payment:
		if months != 0 and months % 6 == 0:
			monthly_salary = monthly_salary * (1 + float(semi_annual_raise))
			monthly_saved = monthly_salary * float(portion_saved)
		current_savings += current_savings * monthly_return_rate
		current_savings += monthly_saved
		months += 1
	print(f"Total months: {months}")

test_cases = [
	{
		"annual_salary": 120000,
		"portion_saved": 0.05,
		"total_cost": 500000,
		"semi_annual_raise": 0.03
	},
	{
		"annual_salary": 80000,
		"portion_saved": 0.1,
		"total_cost": 800000,
		"semi_annual_raise": 0.03
	},
	{
		"annual_salary": 75000,
		"portion_saved": 0.05,
		"total_cost": 1500000,
		"semi_annual_raise": 0.05
	}
]

for test_case in test_cases:
	months_to_save(test_case["annual_salary"], test_case["portion_saved"], test_case["total_cost"], test_case["semi_annual_raise"])





