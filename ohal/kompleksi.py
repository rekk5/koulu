import cmath
import math
import ikkunasto

elementit = {
    "tekstilaatikko": None,
    "tekstikentta": None
}

def muuta_osoitinmuotoon():
    "muuta osoitin"
    luku = ikkunasto.lue_kentan_sisalto(elementit["tekstikentta"])
    luku = luku.strip()
    try:
        ko1 = complex(luku)
        kom = cmath.polar(ko1)
        if isinstance(ko1, complex):
            ikkunasto.kirjoita_tekstilaatikkoon(elementit["tekstilaatikko"], (f"{ko1:.3f} on osoitinmuodossa: {kom[0]:.3f} < {kom[1]*180/math.pi:.3f}"))
            ikkunasto.tyhjaa_kentan_sisalto(elementit["tekstikentta"])
    except ValueError:
        ikkunasto.avaa_viesti_ikkuna("Virhe",
        "Syöte ei ollut kelvollinen kompleksiluku",
        virhe=True
        )
        ikkunasto.tyhjaa_kentan_sisalto(elementit["tekstikentta"])
    


def main():
    "ikkunan luonti"
    ikkuna = ikkunasto.luo_ikkuna("hemuli")
    vasenkehys = ikkunasto.luo_kehys(ikkuna, ikkunasto.VASEN)
    ikkunasto.luo_tekstirivi(vasenkehys, "kompleksiluku:")
    elementit["tekstikentta"] = ikkunasto.luo_tekstikentta(vasenkehys)
    ikkunasto.luo_nappi(vasenkehys, "muunna", muuta_osoitinmuotoon)
    ikkunasto.luo_nappi(vasenkehys, "lopeta", ikkunasto.lopeta)
    oikeakehys = ikkunasto.luo_kehys(ikkuna, ikkunasto.VASEN)
    elementit["tekstilaatikko"] = ikkunasto.luo_tekstilaatikko(oikeakehys, 80, 20)
    ikkunasto.kaynnista()    
    
if __name__ == "__main__":
    main()
