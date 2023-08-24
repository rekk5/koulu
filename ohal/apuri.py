import re

YKSIKOT = {
    "Q": 1000000000000000000000000000000,
    "R": 1000000000000000000000000000,
    "Y": 1000000000000000000000000,
    "Z": 1000000000000000000000,
    "E": 1000000000000000000,
    "P": 1000000000000000,
    "T": 1000000000000,
    "G": 1000000000,
    "M": 1000000,
    "k": 1000,
    "h": 100,
    "d": 0.1,
    "c": 0.01,
    "m": 0.001,
    "u": 0.000001,
    "n": 0.000000001,
    "p": 0.000000000001,
    "f": 0.000000000000001,
    "a": 0.000000000000000001,
    "z": 0.000000000000000000001,
    "y": 0.000000000000000000000001,
    "r": 0.000000000000000000000000001,
    "q": 0.000000000000000000000000000001
}    
 
def muuta_kerrannaisyksikko(kokoluku):
    "katsoo onko oikeat luvut"
    kokoluku1 = kokoluku.strip()
    if kokoluku1.isdigit() is True:
        vastaus = float(kokoluku1)
    elif kokoluku1.isalpha() is True:
        vastaus = None
    else:
        luku = kokoluku1[:-1]
        kerroin = "".join(re.findall("[a-zA-Z]+", kokoluku1))
        try:
            vastaus = (float(luku) * YKSIKOT[kerroin])
        except KeyError:
            vastaus = None
    return vastaus

while True:
    try:
        x1 = input("Anna muutettava arvo: ")
        v2 = muuta_kerrannaisyksikko(x1)
        if v2 is None:
            print("Arvo ei ole kelvollinen")
        else:
            print(v2)
            break
    except KeyError:
        print("Arvo ei ole kelvollinen")
