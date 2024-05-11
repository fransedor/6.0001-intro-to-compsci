import math

semi_annual_raise = 0.07
r = 0.04
down_payment_ratio = 0.25
house_cost = 1000000
months_to_down_payment = 36
down_payment_needed = down_payment_ratio * house_cost

starting_salary = input("Enter the starting salary: ")

def calc_current_savings(starting_salary, portion_saved):
	current_savings = 0
	monthly_salary = starting_salary/12
	monthly_saved = monthly_salary * portion_saved
	#print(f"Monthly salary: {monthly_salary}, Monthly saved: {monthly_saved}")
	for i in range(months_to_down_payment):
		if i != 0 and i % 6 == 0:
			monthly_salary = monthly_salary * (1 + semi_annual_raise)
			monthly_saved = monthly_salary * portion_saved
		current_savings = current_savings * (1 + r/12)
		#print(f"current savings: {current_savings}")
		current_savings += monthly_saved
		#print(f"current savings: {current_savings}")
	return current_savings

left = 0
right = 10000
mid = 0
count = 0
current_savings = 0
while left < right and left < 9999:
	mid = math.floor((right + left)/2)
	midAsDecimal = mid/10000
	current_savings = calc_current_savings(float(starting_salary), midAsDecimal)
	#print(f"current_savings: {current_savings} {left} {right} {midAsDecimal}")
	if (current_savings > down_payment_needed + 100):
		count += 1
		right = mid
	elif (current_savings < down_payment_needed):
		count += 1
		left = mid
	else:
		break
if left == 9999:
	print("It is not possible to pay the down payment in three years.")
else:
	print(f"Best savings rate: ", mid/10000)
	print(f"Steps in bisection search: ", count)




