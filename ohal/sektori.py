from math import  pi

def laske_sektorin_ala(sade, sisakulma):
    ala = (sisakulma * pi * sade ** 2) / 360
    return ala

x = float(input("Anna ympyrän säde:"))
y = float(input("Anna sektorin sisäkulma asteina:"))
answ = round(laske_sektorin_ala(x,y), 4)
print("Sektorin pinta-ala", answ)
