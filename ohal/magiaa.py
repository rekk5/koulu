def pyyda_syote(x, y):
    while True:
        try: 
            x = int(input(x))
        except ValueError:
            print(y)
        else:
            return x

luku = pyyda_syote(
    "Anna kokonaisluku: ",
    "Et antanut kokonaislukua"
)

print(f"Annoit kokonaisluvun {luku}! Nohevaa toimintaa!")
hemulit = pyyda_syote(
    "Montako hemulia mahtuu muumitaloon? ",
    "Tämä ei ollut kelvollinen hemulien lukumäärä!"
)
print(f"Muumitaloon mahtuu {(hemulit)} hemulia")
