from math import sqrt

def laske_sivun_pituus(hypotenuusa):
    sivu = hypotenuusa / sqrt(2)
    return sivu

x = float(input("nna tasakylkisen kolmion hypotenuusan pituus:"))
y = round(laske_sivun_pituus(x), 4)
print("Kylkien pituus:", y)
