from math import sqrt, pi

def laske_nelio_ala(sivun_pituus):
    nelio = sivun_pituus * sivun_pituus
    return nelio

def laske_sektorin_ala(sade, sisakulma):
    ala = (sisakulma * pi * sade ** 2) / 360
    return ala

def laske_sivun_pituus(hypotenuusa):
    sivu = hypotenuusa / sqrt(2)
    return sivu

def laske_kuvion_ala(x):
    nelio1 = laske_nelio_ala(x)
    sivu1 = laske_sivun_pituus(x)
    kolmio = (sivu1 * sivu1) / 2
    laita = sivu1 + sivu1
    nelio2 = laske_nelio_ala(laita)
    kulma1 = 45
    kulma2 = 270
    ympyra1 = laske_sektorin_ala(sivu1, kulma1)
    ympyra2 = laske_sektorin_ala(laita, kulma2)
    x = nelio1 + kolmio + nelio2 + ympyra1 + ympyra2
    return x

x = float(input("Anna x: "))
ala = round(laske_kuvion_ala(x), 4)
print("Kuvion ala:", (ala))
