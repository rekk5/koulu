import ikkunasto

elementit = {
    "tekstilaatikko": None
}

def tulosta_testirivi():
    "testirivi"
    ikkunasto.kirjoita_tekstilaatikkoon(elementit["tekstilaatikko"], "aasisvengaa")

def main():
    "tekee ikkunan"
    ikkuna = ikkunasto.luo_ikkuna("hemuli")
    vasenkehys = ikkunasto.luo_kehys(ikkuna, ikkunasto.VASEN)
    ikkunasto.luo_nappi(vasenkehys, "test", tulosta_testirivi)
    ikkunasto.luo_nappi(vasenkehys, "lopeta", ikkunasto.lopeta)
    oikeakehys = ikkunasto.luo_kehys(ikkuna, ikkunasto.VASEN)
    elementit["tekstilaatikko"] = ikkunasto.luo_tekstilaatikko(oikeakehys, 80, 20)
    ikkunasto.kaynnista()

if __name__ == "__main__":
    main()
