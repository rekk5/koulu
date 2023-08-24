import aasimaaritelmat as am

def nayta_tila(aasidata):
    """
    Tulostaa aasin tilan.
    """
    if aasidata["ELÄKE"] is True:
        print(f"Aasi on {aasidata['IKÄ']} vuotta vanha ja rahaa on {aasidata['RAHA']} mk.")
        print(f"Kylläisyys: {aasidata['KYLLÄISYYS']}")
        print(f"Onnellisuus: {aasidata['ONNELLISUUS']}")
        print(f"Jaksaminen: {aasidata['JAKSAMINEN']}")
        print("Aasi on jääny eläkeelle.")
    elif aasidata["ELÄKE"] is False:
        print(f"Aasi on {aasidata['IKÄ']} vuotta vanha ja rahaa on {aasidata['RAHA']} mk.")
        print(f"Kylläisyys: {aasidata['KYLLÄISYYS']}")
        print(f"Onnellisuus: {aasidata['ONNELLISUUS']}")
        print(f"Jaksaminen: {aasidata['JAKSAMINEN']}")
def pyyda_syote(aasidata):
    """
    Näyttää käyttäjälle aasin tilaa vastaavat mahdolliset syötteet ja kysyy uutta
    syötettä kunnes käyttäjä antaa laillisen syötteen. Saatu syöte palautetaan.
    """
    if aasidata["ELÄKE"] is False:
        print(f"Valinnat: {am.LOPETA}, {am.RUOKI}, {am.KUTITA}, {am.TYOSKENTELE}")
    elif aasidata["ELÄKE"] is True:
        print(f"Valinnat: {am.LOPETA}, {am.ALUSTA}")
    while True:        
        valinta = input("Anna seuraava valinta: ")
        try:
            if aasidata["ELÄKE"] is False:
                if valinta is am.LOPETA:
                    syote = valinta
                    break
                if valinta is am.RUOKI:
                    syote = valinta
                    break
                if valinta is am.KUTITA:
                    syote = valinta
                    break
                if valinta is am.TYOSKENTELE:
                    syote = valinta
                    break
            elif aasidata["ELÄKE"] is True:
                if valinta == am.LOPETA:
                    syote = valinta
                    break
                if valinta is am.ALUSTA:
                    syote = valinta
                    break
        except ValueError:
            print("Virheellinen syöte!")
        else:
            print("Virheellinen syöte!")
    return syote
