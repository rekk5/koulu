import cmath
import math
import piiristo
import ikkunasto
import re


tila = {
    "syote": None,
    "laatikko": None,
    "piiri": None,
    "komponentit": [],
    "jannite": 0,
    "taajuus": 0,
    "jannite1": [],
    "taajuus1": [],
    "impedanssi": 0,
    "impedanssirinnan": [],
    "impedanssirinnan1": 0,
    "impedanssisarjassa": [],
    "tulos": [],
    "virta": 0
}

YKSIKOT = {
    "Y": 1000000000000000000000000,
    "Z": 1000000000000000000000,
    "E": 1000000000000000000,
    "P": 1000000000000000,
    "T": 1000000000000,
    "G": 1000000000,
    "M": 1000000,
    "k": 1000,
    "h": 100,
    "d": 0.1,
    "c": 0.01,
    "m": 0.001,
    "u": 0.000001,
    "n": 0.000000001,
    "p": 0.000000000001,
    "f": 0.000000000000001,
    "a": 0.000000000000000001,
    "z": 0.000000000000000000001,
    "y": 0.000000000000000000000001
}


def aseta_jannite():
    try:
        luku_1 = ikkunasto.lue_kentan_sisalto(tila["syote"]).strip()
        luku_1 = muuta_kerrannaisyksikko(luku_1)
        tila["jannite"] = luku_1
        tila["jannite1"].append(luku_1)
        ikkunasto.kirjoita_tekstilaatikkoon(tila["laatikko"],
                                             f"Jännite {luku_1:.1f} V")
        ikkunasto.tyhjaa_kentan_sisalto(tila["syote"])
    except ValueError:
        ikkunasto.avaa_viesti_ikkuna("Virhe", "Syote ei ollut kelvollinen liukuluku", virhe=True)
        ikkunasto.tyhjaa_kentan_sisalto(tila["syote"])


def aseta_taajuus():
    try:
        luku1 = ikkunasto.lue_kentan_sisalto(tila["syote"])
        luku1 = muuta_kerrannaisyksikko(luku1)
        tila["taajuus"] = luku1
        tila["taajuus1"].append(luku1)
        ikkunasto.kirjoita_tekstilaatikkoon(tila["laatikko"],
                                             f"Taajuus {luku1:.5f} HZ")
        piiristo.piirra_jannitelahde(tila["piiri"], tila["jannite"],
                                      tila["taajuus"], v_asetteluvali=1)
        piiristo.piirra_piiri(tila["piiri"])
        ikkunasto.tyhjaa_kentan_sisalto(tila["syote"])
    except ValueError:
        ikkunasto.avaa_viesti_ikkuna("Virhe", "Syote ei ollut kelvollinen liukuluku", virhe=True)
        ikkunasto.tyhjaa_kentan_sisalto(tila["syote"])


def lisaa_vastus():
    try:
        luku2 = ikkunasto.lue_kentan_sisalto(tila["syote"])
        luku2 = muuta_kerrannaisyksikko(luku2)
        tila["komponentit"].append(("r", luku2))
        ikkunasto.kirjoita_tekstilaatikkoon(tila["laatikko"],
                                             f"Resistanssi {luku2:.5f} Ω")
        piiristo.piirra_haara(tila["piiri"], tila["komponentit"],
                               h_asetteluvali=3, v_asetteluvali=1,
                               viimeinen=False)
        piiristo.piirra_piiri(tila["piiri"])
        r_1, theta = cmath.polar(luku2)
        tila["impedanssi"] = tila["impedanssi"] + r_1
        tila["impedanssisarjassa"].append(r_1)
        ikkunasto.tyhjaa_kentan_sisalto(tila["syote"])
    except ValueError:
        ikkunasto.avaa_viesti_ikkuna("Virhe", "Syote ei ollut kelvollinen liukuluku", virhe=True)
        ikkunasto.tyhjaa_kentan_sisalto(tila["syote"])


def lisaa_vastusrinnan():
    try:
        luku_3 = ikkunasto.lue_kentan_sisalto(tila["syote"])
        luku_3 = muuta_kerrannaisyksikko(luku_3)
        ikkunasto.kirjoita_tekstilaatikkoon(tila["laatikko"],
                                             f"Resistanssi rinnan{luku_3:.5f} Ω")
        tila["tulos"].append(("r", luku_3))
        i = float(luku_3)
        r_2, theta = cmath.polar(i)
        piiristo.piirra_haara(tila["piiri"], tila["komponentit"],
                               h_asetteluvali=3, v_asetteluvali=1,
                               viimeinen=False)
        piiristo.piirra_piiri(tila["piiri"])
        tila["impedanssirinnan"].append(r_2)
        ikkunasto.tyhjaa_kentan_sisalto(tila["syote"])
    except ValueError:
        ikkunasto.avaa_viesti_ikkuna("Virhe", "Syote ei ollut kelvollinen liukuluku", virhe=True)
        ikkunasto.tyhjaa_kentan_sisalto(tila["syote"])


def lisaa_kondensaattori():
    try:
        luku3 = ikkunasto.lue_kentan_sisalto(tila["syote"])
        luku3 = muuta_kerrannaisyksikko(luku3)
        tila["komponentit"].append(("c", luku3))
        ikkunasto.kirjoita_tekstilaatikkoon(tila["laatikko"],
                                             f"Kapasitanssi {luku3:.5f} F")
        piiristo.piirra_haara(tila["piiri"], tila["komponentit"],
                               h_asetteluvali=3, v_asetteluvali=1,
                               viimeinen=False)
        piiristo.piirra_piiri(tila["piiri"])
        k_1 = float(tila["taajuus"])
        r_3, theta = cmath.polar(1 / (2 * math.pi * k_1 * luku3 * 1j))
        tila["impedanssi"] = r_3 + tila["impedanssi"]
        tila["impedanssisarjassa"].append(r_3)
        ikkunasto.tyhjaa_kentan_sisalto(tila["syote"])
    except ValueError:
        ikkunasto.avaa_viesti_ikkuna("Virhe", "Syote ei ollut kelvollinen liukuluku", virhe=True)
        ikkunasto.tyhjaa_kentan_sisalto(tila["syote"])


def lisaa_kondesaattoririnnan():
    try:
        luku5 = ikkunasto.lue_kentan_sisalto(tila["syote"])
        luku5 = muuta_kerrannaisyksikko(luku5)
        ikkunasto.kirjoita_tekstilaatikkoon(tila["laatikko"],
                                             f"Kapasitanssi rinnan {luku5:.5f} F")
        k = float(tila["taajuus"])
        tila["tulos"].append(("c", luku5))
        piiristo.piirra_haara(tila["piiri"], tila["komponentit"],
                               h_asetteluvali=3, v_asetteluvali=1,
                               viimeinen=False)
        piiristo.piirra_piiri(tila["piiri"])
        i_1 = float(luku5)
        r_4, theta = cmath.polar(1 / (2 * math.pi * k * i_1 * 1j))
        tila["impedanssirinnan"].append(r_4)
        ikkunasto.tyhjaa_kentan_sisalto(tila["syote"])
    except ValueError:
        ikkunasto.avaa_viesti_ikkuna("Virhe",
                                      "Syote ei ollut kelvollinen liukuluku",
                                      virhe=True
                                      )
        ikkunasto.tyhjaa_kentan_sisalto(tila["syote"])


def lisaa_kela():
    try:
        luku4 = ikkunasto.lue_kentan_sisalto(tila["syote"])
        luku4 = muuta_kerrannaisyksikko(luku4)
        tila["komponentit"].append(("l", luku4))
        ikkunasto.kirjoita_tekstilaatikkoon(tila["laatikko"],
                                             f"Induktanssi {luku4:.5f} H")
        piiristo.piirra_haara(tila["piiri"], tila["komponentit"],
                               h_asetteluvali=3, v_asetteluvali=1,
                               viimeinen=False)
        piiristo.piirra_piiri(tila["piiri"])
        k_2 = float(tila["taajuus"])
        r_5, theta = cmath.polar(2 * math.pi * k_2 * luku4 * 1j)
        tila["impedanssi"] = r_5 + tila["impedanssi"]
        tila["impedanssisarjassa"].append(r_5)
        ikkunasto.tyhjaa_kentan_sisalto(tila["syote"])
    except ValueError:
        ikkunasto.avaa_viesti_ikkuna("Virhe", "Syote ei ollut kelvollinen liukuluku", virhe=True)
        ikkunasto.tyhjaa_kentan_sisalto(tila["syote"])


def lisaa_kelarinnan():
    try:
        luku_7 = ikkunasto.lue_kentan_sisalto(tila["syote"])
        luku_7 = muuta_kerrannaisyksikko(luku_7)
        ikkunasto.kirjoita_tekstilaatikkoon(tila["laatikko"],
                                             f"Induktanssi {luku_7:.5f} H")
        k = float(tila["taajuus"])
        tila["tulos"].append(("l", luku_7))
        piiristo.piirra_haara(tila["piiri"], tila["komponentit"],
                               h_asetteluvali=3, v_asetteluvali=1,
                               viimeinen=False)
        piiristo.piirra_piiri(tila["piiri"])
        i_2 = float(luku_7)
        r_6, theta = cmath.polar(2 * math.pi * i_2 * k * 1j)
        tila["impedanssirinnan"].append(r_6)
        ikkunasto.tyhjaa_kentan_sisalto(tila["syote"])
    except ValueError:
        ikkunasto.avaa_viesti_ikkuna("Virhe",
                                      "Syote ei ollut kelvollinen liukuluku",
                                      virhe=True
                                      )
        ikkunasto.tyhjaa_kentan_sisalto(tila["syote"])


def piirra_piiri():
    try:
        if not tila["tulos"]:
            piiristo.piirra_jannitelahde(tila["piiri"], tila["jannite"],
                                          tila["taajuus"], v_asetteluvali=2)
            piiristo.piirra_haara(tila["piiri"], tila["komponentit"],
                                   h_asetteluvali=6, v_asetteluvali=2,
                                   viimeinen=True)
            piiristo.piirra_piiri(tila["piiri"])
            tila["virta"] = tila["jannite"] / tila["impedanssi"]
            laske_jannitesarjan()
            k = tila["impedanssi"]
            ikkunasto.kirjoita_tekstilaatikkoon(tila["laatikko"],
                                                 f"Kapasitanssi {k:.5f} F")
            tila["komponentit"].clear()
        else:
            tila["komponentit"].append(tila["tulos"])
            piiristo.piirra_jannitelahde(tila["piiri"], tila["jannite"],
                                          tila["taajuus"], v_asetteluvali=2)
            piiristo.piirra_haara(tila["piiri"], tila["komponentit"],
                                   h_asetteluvali=6, v_asetteluvali=2,
                                   viimeinen=True)
            piiristo.piirra_piiri(tila["piiri"])
            laske_kokoimpedanssivirta()
            laske_rinnanvirta()
            laske_jannitesarjan()
            tila["komponentit"].clear()
    except IndexError:
        ikkunasto.avaa_viesti_ikkuna("Virhe",
                                      "Muista lisätä komponentteja",
                                      virhe=True
                                      )
        ikkunasto.tyhjaa_kentan_sisalto(tila["syote"])


def laske_kokoimpedanssivirta():
    try:
        for x_4 in tila["impedanssirinnan"]:
            if isdigit(x_4):
                impedanssi = 1 / x_4
                tila["impedanssirinnan1"] = tila["impedanssirinnan1"] + impedanssi
            else:
                continue
        tila["impedanssi"] = tila["impedanssi"] + (1 / tila["impedanssirinnan1"])
        tila["impedanssisarjassa"].append(1 / tila["impedanssirinnan1"])
        tila["virta"] = tila["jannite"] / tila["impedanssi"]
    except IndexError:
        ikkunasto.avaa_viesti_ikkuna("Virhe",
                                      "Muista lisätä komponentteja",
                                      virhe=True
                                      )
        ikkunasto.tyhjaa_kentan_sisalto(tila["syote"])


def laske_rinnanvirta():
    try:
        for x_5 in tila["impedanssirinnan"]:
            if isdigit(x_5):
                i_4 = tila["jannite"] / x_5
                ikkunasto.kirjoita_tekstilaatikkoon(tila["laatikko"],
                 f"Rinnan kytkettyjen komponenttien virta {i_4:.7f}")
            else:
                continue
    except ValueError:
        ikkunasto.avaa_viesti_ikkuna("Virhe",
                                      "Muista lisätä komponentteja",
                                      virhe=True
                                      )
        ikkunasto.tyhjaa_kentan_sisalto(tila["syote"])


def laske_jannitesarjan():
    try:
        for x_7 in tila["impedanssisarjassa"]:
            if isdigit(x_7):
                u_1 = tila["virta"] * x_7
                ikkunasto.kirjoita_tekstilaatikkoon(tila["laatikko"],
                  f"Sarjaan kytkettyjen komponenttien jännite {u_1:.7f}")
            else:
                continue
    except IndexError:
        ikkunasto.avaa_viesti_ikkuna("Virhe",
                                      "Muista lisätä komponentteja",
                                      virhe=True
                                      )


def tyhjaa_piiri():
    piiristo.tyhjaa_piiri(tila["piiri"])
    tila["komponentit"].clear()
    tila["tulos"].clear()
    tila["jannite1"].clear()
    tila["taajuus1"].clear()


def isdigit(x_8):
    try:
        float(x_8)
        return True
    except ValueError:
        return False


def muuta_kerrannaisyksikko(kokoluku):
    kokoluku1 = kokoluku.strip()
    if kokoluku1.isdigit():
        vastaus = float(kokoluku1)
    elif kokoluku1.isalpha():
        vastaus = None
    else:
        luku = kokoluku1[:-1]
        kerroin = "".join(re.findall("[a-zA-Z]+", kokoluku1))
        try:
            vastaus = (float(luku) * YKSIKOT[kerroin])
        except KeyError:
            vastaus = None
    return vastaus


def main():
    ikkuna = ikkunasto.luo_ikkuna("hemuli")
    vasenkehys = ikkunasto.luo_kehys(ikkuna, ikkunasto.VASEN)
    ikkunasto.luo_tekstirivi(vasenkehys, "arvo:")
    tila["syote"] = ikkunasto.luo_tekstikentta(vasenkehys)
    ikkunasto.luo_nappi(vasenkehys, "aseta jännite", aseta_jannite)
    ikkunasto.luo_nappi(vasenkehys, "aseta taajuus", aseta_taajuus)
    ikkunasto.luo_nappi(vasenkehys, "lisää vastus", lisaa_vastus)
    ikkunasto.luo_nappi(vasenkehys, "lisää vastusrinnan", lisaa_vastusrinnan)
    ikkunasto.luo_nappi(vasenkehys, "lisää kondensaattori", lisaa_kondensaattori)
    ikkunasto.luo_nappi(vasenkehys, "lisää kondensaattoririnnan", lisaa_kondesaattoririnnan)
    ikkunasto.luo_nappi(vasenkehys, "lisää kela", lisaa_kela)
    ikkunasto.luo_nappi(vasenkehys, "lisää kelarinnan", lisaa_kelarinnan)
    ikkunasto.luo_nappi(vasenkehys, "piirra piiri", piirra_piiri)
    ikkunasto.luo_nappi(vasenkehys, "tyhjaa piiri", tyhjaa_piiri)
    ikkunasto.luo_nappi(vasenkehys, "lopeta", ikkunasto.lopeta)
    tila["laatikko"] = ikkunasto.luo_tekstilaatikko(vasenkehys, 50, 40)
    oikeakehys = ikkunasto.luo_kehys(ikkuna, ikkunasto.VASEN)
    tila["piiri"] = piiristo.luo_piiri(oikeakehys, 800, 600, 16)
    ikkunasto.kaynnista()


if __name__ == "__main__":
    main()
