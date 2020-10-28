import re

while True:

	phone = input("What's your phone number?: ")

	phonepattern = '^06-?\d{8}$'
	matches1 = re.findall(phonepattern, phone)
	
	if(len(matches1) > 0):
		break

print("Number in correct format:", matches1[0])