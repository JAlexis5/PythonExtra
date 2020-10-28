import re

while True:
	
	zipcode = input ("What's your ZIP code?: ")
	
	zippattern ='^[0-9]{4}\s?[a-zA-Z]{2}$'
	matches2 = re.findall(zippattern, zipcode)
    
	if(len(matches2)>0):
		break

matches2str = str(matches2).strip('[]')

print("ZIP code in correct format:", matches2str)