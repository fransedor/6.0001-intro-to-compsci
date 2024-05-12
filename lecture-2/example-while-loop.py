##############################
## CODE EXAMPLE FOR WHILE LOOP
## TAKEN FROM THE ZELDA EXAMPLE IN THE LECTURE VIDEO
##############################

def print_question_happy():	
	print("You are in the Lost Forest")
	print(("*")*20)
	print(("*")*20)
	print((" ")*5 ,":)")
	print(("*")*20)
	print(("*")*20)

def print_question_sad():
	print("You are in the Lost Forest")
	print(("*")*20)
	print(("*")*20)
	print((" ")*5 ,":((")
	print(("*")*20)
	print(("*")*20)

def print_flip_table():
	print("You are in the Lost Forest")
	print(("*")*20)
	print(("*")*20)
	print("Flipping table emoji")
	print(("*")*20)
	print(("*")*20)

print_question_happy()
direction = input("Go left or right? ")
print("\n")

right_count = 0
while direction == "right" or direction == "Right":
	right_count += 1
	if right_count > 2:
		print_flip_table()
	elif right_count == 2:
		print_question_sad()
	else:
		print_question_happy()
	direction = input("Go left or right? ")
	print("\n")

print("You got out of the forest! \n \\o/")

