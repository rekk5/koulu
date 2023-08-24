def pituus():
    print("Valittiin pituus")
    
def paino():
    print("Valittiin paino")
    
def tilavuus():
    print("Valittiin tilavuus")

def lampotila():
    print("Valittiin lämpötila")

print("Tämä ohjelma muuntaa yhdysvaltalaisia yksiköitä SI-yksiköiksi")
print("Mahdolliset toiminnot:")
print("pituus")
print("paino")
print("tilavuus")
print("lämpötila")
print()
valinta = input("Tee valintasi: ")
if valinta == "pituus":
    pituus()
elif valinta == "paino":
    paino()
elif valinta == "tilavuus":
    tilavuus()
elif valinta == "lämpötila":
    lampotila()
else:
    print("Valitsemaasi toimintoa ei ole olemassa")