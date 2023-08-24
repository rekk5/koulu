def paaohjelma():
    try:
        matka = float(input("Anna auton kulkema matka (m) :"))
        aika = float(input("Anna matkaan kulunut aika (s) :"))
    except ValueError:
        print("Vähemmän donitseja, enemmän puhtaita numeroita.")
    else:
        nopeus = matka / aika * 3.6
        tie = matka
        kello = aika
        print(f"{tie:.2f} metriä {kello:.2f} sekunissa kulkeneen auton nopeus on {nopeus:.2f} km/h")
        

paaohjelma()
