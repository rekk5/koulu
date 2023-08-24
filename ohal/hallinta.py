from math import cos, radians, sin

hahmo_1 = {
    "x": 0,
    "y": 0,
    "suunta": 0,
    "nopeus": 0
}

hahmo_2 = {
    "x": 50,
    "y": 50,
    "suunta": 0,
    "nopeus": 0
}

def kysy_liike(pelaaja):
    x_1 = pelaaja["x"]
    y_1 = pelaaja["y"]
    print(f"Hahmo on sijanissa ({x_1}, {y_1})")
    pelaaja["suunta"] = float(input("Anna liikkumissuunta asteina: "))    
    pelaaja["nopeus"] = float(input("Anna liikenopeus: "))

def paivita_sijainti(pelaaj):
    pelaaj["x"] = pelaaj["x"] + int(round(pelaaj["nopeus"] * cos(radians(pelaaj["suunta"])), 0))
    pelaaj["y"] = pelaaj["y"] + int(round(pelaaj["nopeus"] * sin(radians(pelaaj["suunta"])), 0))
        
print("Pelaajan 1 vuoro")
kysy_liike(hahmo_1)
paivita_sijainti(hahmo_1)
print(f"Uusi sijainti: ({hahmo_1['x']}, {hahmo_1['y']})")
print("Pelaajan 2 vuoro")
kysy_liike(hahmo_2)
paivita_sijainti(hahmo_2)
print(f"Uusi sijainti: ({hahmo_2['x']}, {hahmo_2['y']})")