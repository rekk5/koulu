def laske_nelion_ala(sivu):
    sivun_pituus = sivu * sivu
    return sivun_pituus

x = float(input("Anna neliön sivun pituus:"))
y = round(laske_nelion_ala(x), 4)
print("Neliön pinta-ala:", y)
