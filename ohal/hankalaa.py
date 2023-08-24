def pyyda_syote(yksi, kaksi):
    "esim"
    while True:
        try: 
            numer = int(input(yksi))
            if numer <= 1:
                print(kaksi)
            else:
                break
        except ValueError:
            print(kaksi)
    return numer

def tarkista_alkuluku(numero):
    "testi"
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True

num = pyyda_syote(
    "Anna kokonaisluku, joka on suurempi kuin 1:",
    "Pieleen meni :'(.")
    
tulos = tarkista_alkuluku(num)

if tarkista_alkuluku(num) is False: 
    print("Kyseessä ei ole alkuluku.")
elif tarkista_alkuluku(num) is True:
    print("Kyseessä on alkuluku.")
