file = open("klasgenoten.txt","r")

text_line = file.readline()

while text_line:
    text_line = text_line.strip()
    print(text_line)

    text_line = file.readline()
