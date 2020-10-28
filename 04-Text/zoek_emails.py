import re

emails = []

with open("tekstmetemails.txt", "r") as file:
	line = file.readline()
	
	while line:
		pattern = r"([a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]+)"
		found = re.findall(pattern, line)
		emails.extend(found)
		line = file.readline()

print(emails)