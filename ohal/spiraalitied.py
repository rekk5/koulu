from turtle import *

def piirra_tiedostosta(tiedosto):
    "käsittele tiedosto"
    try:
        with open(tiedosto) as lahde:
            for rivi in lahde.readlines():
                vari, maara, sade, kasvu, paksuus = rivi.split(",")
                vari1 = vari.strip()
                maara1 = int(maara)
                sade1 = int(sade)
                kasvu1 = float(kasvu)
                paksuus1 = int(paksuus)
                piirra_spiraali(vari1, maara1, sade1, kasvu1, paksuus1)
    except IOError:
        print("Tiedoston avaaminen ei onnistunut. Aloitetaan tyhjällä kokoelmalla")


def piirra_spiraali(vari2, maara2, sade2, kasvu2, paksuus2):
    "piirra spiraali"
    color(vari2)
    pensize(paksuus2)
    for ympyra in range(maara2):
        circle(sade2, 90)
        sade2 = sade2 + kasvu2

piirra_tiedostosta("spiraali.txt")
done()
