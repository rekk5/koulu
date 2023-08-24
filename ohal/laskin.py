def plus():
    try:
        luku_1 = float(input("Anna luku 1: "))
        luku_2 = float(input("Anna luku 2: "))
    except ValueError:
        print("Ei tämä ole mikään luku")
    else:
        if luku_1 != 0 and luku_2 != 0:
            print(f"Tulos: {luku_1 + luku_2}")
        elif luku_1 == 0 or luku_2 == 0:
            print("Tällä ohjelmalla ei pääse äärettömyyteen")
def miinus():
    try:
        luku_1 = float(input("Anna luku 1: "))
        luku_2 = float(input("Anna luku 2: "))
    except ValueError:
        print("Ei tämä ole mikään luku")
    else:
        if luku_1 != 0 and luku_2 != 0:
            print(f"Tulos: {luku_1 - luku_2}")
        elif luku_1 == 0 or luku_2 == 0:
            print("Tällä ohjelmalla ei pääse äärettömyyteen")
def kerto():
    try:
        luku_1 = float(input("Anna luku 1: "))
        luku_2 = float(input("Anna luku 2: "))
    except ValueError:
        print("Ei tämä ole mikään luku")
    else:
        if luku_1 != 0 and luku_2 != 0:
            print(f"Tulos: {luku_1 * luku_2}")
        elif luku_1 == 0 or luku_2 == 0:
            print("Tällä ohjelmalla ei pääse äärettömyyteen")        
def jako():
    try:
        luku_1 = float(input("Anna luku 1: "))
        luku_2 = float(input("Anna luku 2: "))
    except ValueError:
        print("Ei tämä ole mikään luku")
    else:
        if luku_1 != 0 and luku_2 != 0:
            print(f"Tulos: {luku_1 / luku_2}")
        elif luku_1 == 0 or luku_2 != 0:
            print(f"Tulos: {luku_1 / luku_2}")
        elif luku_1 == 0 or luku_2 == 0:
            print("Tällä ohjelmalla ei pääse äärettömyyteen")                
valinta = input("Valitse operaatio (+, -, *, /): ")
if valinta == "+":
    plus()
elif valinta == "-":
    miinus()
elif valinta == "*":
    kerto()
elif valinta == "/":
    jako()
else:
    print("Operaatiota ei ole olemassa")
