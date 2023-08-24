from math import sin, cos

def muunna_xy_koordinaateiksi (radi,pituus):
    x = round(pituus * cos(radi))
    y = round(pituus * sin(radi))
    kuu = int(x)
    puu = int(y)
    return kuu,puu

kulma = float(input("Anna kulma radiaaneina:"))
osoitin = float(input("Anna osoitinvektorin pituus:"))
eka, toka = (muunna_xy_koordinaateiksi(kulma, osoitin))
print(f"Koordinaatit (x, y): ({eka},{toka} )")
