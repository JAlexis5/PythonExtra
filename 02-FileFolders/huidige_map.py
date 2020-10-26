import os

werkmap = os.getcwd()
print("De huidige map is: " + werkmap)

lengte_mapnaam = 0

while lengte_mapnaam == 0:

    mapnaam = input("Voer de naam van de nieuwe map in: ")
    lengte_mapnaam = len(mapnaam)
    
    if lengte_mapnaam > 0:
            os.mkdir(mapnaam)
            print("Nieuwe map", mapnaam, "aangemaakt.")
    else:
            print("Je hebt geen naam ingevoerd.")
