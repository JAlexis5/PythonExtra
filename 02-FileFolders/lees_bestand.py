import io

file2 = open("test.txt", "r")

# Alle tekst lezen met read() en opslaan in de variabele: inhoud
contents = file2.read()

# De inhoud op het scherm zetten:
print("De inhoud van het bestand is:")
print(contents)
