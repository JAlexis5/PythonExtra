import os

filename = "demobestand.txt"

current_dir = os.getcwd()

full_path = os.path.join(current_dir, filename)
print("Renaming file to " + full_path)

new_name = input("New file name: ")

if len(new_name) > 0:
    new_full_path = os.path.join(current_dir, new_name)
    print("Renaming file to: " + new_full_path)



    os.rename(full_path, new_full_path)
    print("Renamed file.")
else:
    print("Invalid input, ending program...")
