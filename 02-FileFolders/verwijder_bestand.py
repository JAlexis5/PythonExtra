import os

bestand = input("Welk bestand wil je verwijderen?: ")

if len(bestand) > 0:
    if os.path.exists(bestand):
        os.remove(bestand)
        print("Bestand" , bestand , "verwijderd.")
    else:
        print("Error: Niet-bestaand bestand.")
else:
    print("Geen invoer. Programma zal sluiten")
