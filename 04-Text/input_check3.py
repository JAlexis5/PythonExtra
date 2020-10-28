import re

while True:
	
	licplate = input ("What's on your car's license plate?: ")
	
	licplatepattern ='^[a-zA-Z]{2}-?[0-9]{3}-?[a-zA-Z]{3}$'
	matches3 = re.findall(licplatepattern, licplate)
	
	if(len(matches3) > 0):
		break

matches3str = str(matches3).strip('[]')

print("Plate in correct format:", matches3str)