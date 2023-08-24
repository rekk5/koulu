import piiristo
import ikkunasto

tila = {
    "syote": None,
    "laatikko": None,
    "piiri": None,
    "komponentit": [],
    "jannite": 0,
    "taajuus": 0,
}

def aseta_jannite():
    "asettaa jannitteen"
    try:
        luku = float(ikkunasto.lue_kentan_sisalto(tila["syote"]))
        tila["jannite"] = luku
        ikkunasto.kirjoita_tekstilaatikkoon(tila["laatikko"],
        (f"Jännite {luku:.1f} V"))
        ikkunasto.tyhjaa_kentan_sisalto(tila["syote"])
    except ValueError:
        ikkunasto.avaa_viesti_ikkuna("Virhe",
        "Syote ei ollut kelvollinen liukuluku",
        virhe=True
        )
        ikkunasto.tyhjaa_kentan_sisalto(tila["syote"])

def aseta_taajuus():
    "asettaa taajuuden"
    try:
        luku1 = float(ikkunasto.lue_kentan_sisalto(tila["syote"]))
        tila["taajuus"] = luku1
        ikkunasto.kirjoita_tekstilaatikkoon(tila["laatikko"],
        (f"Taajuus {luku1:.1f} HZ"))
        ikkunasto.tyhjaa_kentan_sisalto(tila["syote"])
    except ValueError:
        ikkunasto.avaa_viesti_ikkuna("Virhe",
        "Syote ei ollut kelvollinen liukuluku",
        virhe=True
        )
        ikkunasto.tyhjaa_kentan_sisalto(tila["syote"])

def lisaa_vastus():
    "lisää vastuksen"
    try:
        luku2 = float(ikkunasto.lue_kentan_sisalto(tila["syote"]))
        tila["komponentit"].append(("r", luku2))
        piiristo.piirra_jannitelahde(tila["piiri"],
        tila["jannite"],
        tila["taajuus"],
        v_asetteluvali=2
        )
        piiristo.piirra_haara(tila["piiri"],
        tila["komponentit"],
        h_asetteluvali=2,
        v_asetteluvali=2,
        viimeinen=True
        )
        piiristo.piirra_piiri(tila["piiri"])
    except ValueError:
        ikkunasto.avaa_viesti_ikkuna("Virhe",
        "Syote ei ollut kelvollinen liukuluku",
        virhe=True
        )
        ikkunasto.tyhjaa_kentan_sisalto(tila["syote"])

def main():
    "pääohjelma"
    ikkuna = ikkunasto.luo_ikkuna("hemuli")
    vasenkehys = ikkunasto.luo_kehys(ikkuna, ikkunasto.VASEN)
    ikkunasto.luo_tekstirivi(vasenkehys, "arvo:")
    tila["syote"] = ikkunasto.luo_tekstikentta(vasenkehys)
    ikkunasto.luo_nappi(vasenkehys, "aseta jännite", aseta_jannite)
    ikkunasto.luo_nappi(vasenkehys, "aseta taajuus", aseta_taajuus)
    ikkunasto.luo_nappi(vasenkehys, "lisää vastus", lisaa_vastus)
    ikkunasto.luo_nappi(vasenkehys, "lopeta", ikkunasto.lopeta)
    tila["laatikko"] = ikkunasto.luo_tekstilaatikko(vasenkehys, 40, 20)
    oikeakehys = ikkunasto.luo_kehys(ikkuna, ikkunasto.VASEN)
    tila["piiri"] = piiristo.luo_piiri(oikeakehys, 600, 600, 16)
    ikkunasto.kaynnista()
    
if __name__=="__main__":
    main()
    