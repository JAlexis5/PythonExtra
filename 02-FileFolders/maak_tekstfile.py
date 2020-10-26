import io

file = open("test.txt", "w")
file.write("Test 123!");
file.close()

file2 = open("test.txt", "r")
file2.write("Lekker alles overschrijven")
