import random
import time
import sys
import haravasto as ha

tila = {
    "kentta": [],
    "nakyvakentta": [],
    "leveys": 0,
    "korkeus": 0,
    "miinojen_maara": 0,
    "klikkaukset": 0,
    "kulunutaika": 0,
    "lopputulos": 0,
    "liput": 0,
    "kulunutaikatiedostoon": 0,
    "avaamattomat": 0,
}

def valikko():
    '''
    Tulostaa alkuvalikon ja sitten funktion, joka kutsuu loppu peliä.
    Valinan perusteella sitten joko sijoittaa valmiit arvot sanakirjaan
    tai kutsuu tiedonhankitafunktiota/tulostusfunktiota
    '''
    print(
          "|   1. Uusi peli(helppo)     |\n"
          "|   2. Uusi peli(normaali)   |\n"
          "|   3. Uusi peli(vaikea)     |\n"
          "|   4. Uusi peli(oma)        |\n"
          "|   5. Aijemmat pelit        |\n"
          "|   6. Ohjeet                |\n"
          "|   7. Sulje ohjelma         |\n")
    try:
        valinta = int(input("Anna valinta: "))
        if valinta == 1:
            tila["leveys"] = 9
            tila["korkeus"] = 9
            tila["miinojen_maara"] = 10
            main()
        if valinta == 2:
            tila["leveys"] = 16
            tila["korkeus"] = 16
            tila["miinojen_maara"] = 40
            main()
        if valinta == 3:
            tila["leveys"] = 30
            tila["korkeus"] = 16
            tila["miinojen_maara"] = 99
            main()
        if valinta == 4:
            hanki_tiedot()
        if valinta == 5:
            tulostin()
        if valinta == 6:
            ohjeet()
        if valinta == 7:
            sys.exit(1)
        if valinta < 1 or valinta > 7:
            print("Valintaa ei ole olemassa!")
            valikko()
    except ValueError:
        print("Valintaa ei ole olemassa!")
        valikko()

def kysy_kokonaisluku(viesti, min_arvo, max_arvo=None):
    '''
    Käsittelee kysytyn kokonaisluvun ja varmistaa, että se on täsmäävä luku,
    käyttäen loputonta silmukkaa, ja testaa onko anettu luku kelvollinen,
    try: expect rakenteella.
    '''
    while True:
        try:
            arvo = int(input(viesti))
            if arvo < min_arvo or (max_arvo is not None and arvo > max_arvo):
                print(f"Anna luku väliltä {min_arvo} - {max_arvo}")
                continue
            return arvo
        except ValueError:
            print("Anna kelvollinen kokonaisluku.")

def hanki_tiedot():
    '''
    Kysyy miinojen määrän ja laskee maksimi miinojen määrän käyttäen 
    kysy_kokonaisluku apufuntiona ja laskee maksimaalisten miinojen määrän
    kentänkoko miinus yksi
    , jonka jälkeen kun on saatu oikeat luvut niin kutsuu main() funktiota.
    '''
    maksimi_koko = 100
    tila["leveys"] = kysy_kokonaisluku("Anna kentän leveys: ", 1, maksimi_koko)
    tila["korkeus"] = kysy_kokonaisluku("Anna kentän korkeus: ", 1, maksimi_koko)
    maksimi_miinat = tila["korkeus"] * tila["leveys"] - 1
    tila["miinojen_maara"] = kysy_kokonaisluku("Anna miinojen määrä: ", 1, maksimi_miinat)
    main()

def piirra_kentta():
    '''
    Piirtää pelikentän ja siihen muutokset. E
    nsin tyhjentää pelikentän kutsulla ha.tyhjaa_ikkuna().
    Piirtää taustan pelikentälle käyttäen ha.piirra_tausta().
    ha.aloita_ruutujen_piirto() valmistaa peli-ikkunan uusien 
    graafisten elementtien, kuten ruutujen, piirtämiseen.
    Tämän jälkeen funtio käy läpi kaikki tila["kentta"]
    ruudun ja piirtää ne peli ikkunaan tämä. Sen jälkeen
    lisätään ruudut piirrettäväksi ikkunaksi tila["nakyvakentta"]
    ja sijoitetaan ne kuhunkin ruutuun ja kerrotaan ne 40 pikselillä
    ja viimeiseksi viimeistellään ruutujen piirtämisen ja näyttää
    peli-ikkunan.
    '''
    ha.tyhjaa_ikkuna()
    ha.piirra_tausta()
    ha.aloita_ruutujen_piirto()
    for y in range(len(tila["kentta"][0])):
        for x in range(len(tila["kentta"])):
            ha.lisaa_piirrettava_ruutu(tila["nakyvakentta"][x][y], y * 40, x * 40)
    ha.piirra_ruudut()

def laske_miinat(x, y, lista):
    """
    Ensinnä alustetaan miina_count, joka pitää kirjaa siitä
    , kuinka monta miinaa annetun ruudun ympärillä. Sitten käydään
    läpi annetun ruudun ympärillä olevat ruudut käyttäen kaksiulotteista
    silmukkaa, jokaisen rundin jälkeen lasketaan uudet koordinaatit, jotka
    edustavat tarkasteltavaa ruutua suhteessa alkuperäisiin ruutuihin. Sitten
    tarkistetaan, että nämä uudet koordinaatit ovat pelikentän sisällä. Jos
    siinä on miina lisätään yksi miinacount muutujaan. Sitten jos miina
    count on yli 0 niin se tarkoittaa, että kyseisen ruudun ympärillä on
    miina tai miinoja niin päivitetään tila["kentta"] taulukon kyseistä ruutua.
    Sitten viela tarkistetaan onko "nakyvakentt" listassa ruudussa lippua
    , jos ei niin myös tämä ruutu näyttää miinojen määrää.
    """
    miina_count = 0
    for annettux in range(-1, 2):
        for annettuy in range(-1, 2):
            uusix, uusy = x + annettux, y + annettuy
            if 0 <= uusix < len(lista[0]) and 0 <= uusy < len(lista) and lista[uusy][uusix] == 'x':
                miina_count += 1
    if miina_count > 0:
        tila["kentta"][y][x] = f"{miina_count}"
        if tila["nakyvakentta"][y][x] != "f":
            tila["nakyvakentta"][y][x] = f"{miina_count}"

def miinoita(kentta, miinat):
    """
    Lasketaan ensin peli kentän korkeus ja leveys. Tämän jälkeen tehdään
    apu lista, jossa on jokaisen miinan mahdollinen sijainti. Tämän jälkeen
    arvotaan, jokainen miinan paikka listalla ja ne ei voi olla samalla paikalla
    , koska random.sample(). Tämän jälkeen käydään läpi, jokaisen arvotun miinan
    sijainti ja merkitaan ne "x":si taustajärjestelmän listaan.
    """
    korkeus = len(kentta)
    leveys = len(kentta[0])
    kaikki_sijainnit = [(x, y) for x in range(korkeus) for y in range(leveys)]
    miinojen_sijainnit = random.sample(kaikki_sijainnit, miinat)

    for x, y in miinojen_sijainnit:
        kentta[x][y] = "x"

def sekuntikello(sekuntti):
    '''
    Laskee sekuntteja sanakirjan muuttujaan
    '''
    tila["kulunutaika"] += 1

def lopetustoiminta():
    '''
    Lopetus toiminta, joka tallentaa pelin tilatstot .txt tiedostoon ja
    samalla laskee ajan ja muuttaa sen oikeaksi yksiköksi. Ja sitten 
    vielä näytetään pelin lopputulos kun päivitetään "näkyväkentta"
    tausta listalla "kentta"
    '''
    minuutit = tila["kulunutaika"] // 60
    sekunnit = tila["kulunutaika"] % 60
    aika_merkkijonona = f"{minuutit}min {sekunnit}s" if minuutit > 0 else f"{sekunnit}s"
    try:
        with open("tilasto.txt", "a", encoding="utf-8") as tiedosto:
            tiedosto.write(
                f"{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}: "
                f"Pelin kesto: {aika_merkkijonona}, Siirtoja: {tila['klikkaukset']}, "
                f"Lopputulos: {tila['lopputulos']} "
                f"(kentän mitat olivat {tila['leveys']}x{tila['korkeus']} ja "
                f"miinoja oli {tila['miinojen_maara']}).\n")
    except IOError:
        print("Tiedoston kirjoittaminen epäonnistui")
    tila["nakyvakentta"] = tila["kentta"]

def kasittele_hiiri(hiirix, hiiriy, nappi, muoknap):
    """
    Ensin käsitellään vasenta hiirennapin klikkausta, ensin päivitetään
    laskuria tila["klikkaukset"]. Tämän jälkeen lasketaan klikatun ruudun
    koordinaatit, jos klikattu on jo näkymässä niin piirretään kenttä uudestaan.
    Jos klikattu ruutu on miina eli "x" peli päättyy häviöön ja päivitetään lopputulos
    ja kutsutaan lopetustoiminta funktiota. Jos klikattu ruutu ei sisällä miinaa
    , niin lasketaan lähellä olevat miinat ja tulvataan näyttö eli näytetään
    lisää ruutuja. Oikeassa hiiressä on myös klikkaus muuttuja. Jos klikattu
    ruudussa ei ole lippua asetetaan tähän lippu ja pidetään huolta siitä ettei
    kaikki lippuja ole käytetty ja päivitetään lippu nakyvakenttä listaan.
    Lopuksi vielä tarkistetaan voitto.
    """
    if tila["lopputulos"] in ["Voitto!", "Häviö"]:
        return
    if nappi == ha.HIIRI_VASEN:
        tila["klikkaukset"] += 1
        vasenx = int(hiirix/40)
        vaseny = int(hiiriy/40)
        if tila["kentta"] == tila["nakyvakentta"]:
            piirra_kentta()
        elif tila["kentta"][vaseny][vasenx] == "x":
            tila["lopputulos"] = "Häviö"
            print("Hävisit pelin")
            lopetustoiminta()
        elif tila["kentta"][vaseny][vasenx] != "x":
            laske_miinat(vasenx, vaseny, tila["kentta"])
            tulvataytto(tila["kentta"], vasenx, vaseny)
    if nappi == ha.HIIRI_OIKEA:
        tila["klikkaukset"] += 1
        oikeax = int(hiirix/40)
        oikeay = int(hiiriy/40)
        if tila["nakyvakentta"][oikeay][oikeax] == "f":
            tila["nakyvakentta"][oikeay][oikeax] = " "
            tila["liput"] -= 1
        elif tila["kentta"][oikeay][oikeax] != "f":
            tila["nakyvakentta"][oikeay][oikeax] = "f"
            tila["liput"] += 1
    tarkista_voitto()

def tarkista_voitto():
    """
    Ensinnä lasketaan, onko miinoja ja lippuja, kuinka paljon käytetty eri
    kentta listoista. Jos nämä ovat yhtä suuret pelaaja voittaa pelin. 
    Tämän jälkeen tarkistetaan, onko pelaaja käyttänyt kaikki liput, mutta kaikkia
    miinoja ei ole liputettu. Tämän jälkeen lasketaan, kuinka monta ruutua on vielä avaamatta
    tai liputettu. Jos avaamattomien ja liputettujen ruutujen määrä vastaa miinojen määrää
    pelaaja on voittanut pelin. Avaamalla kaikki ei miinoitetut ruudut.
    """
    yhtalaisyydet = sum(1 for i in range(tila["korkeus"]) for j in range(tila["leveys"])
                        if tila["kentta"][i][j] == "x" and tila["nakyvakentta"][i][j] == "f")
    if yhtalaisyydet == tila["miinojen_maara"]:
        print("Onneksi olkoon, voitit pelin (kaikki miinalliset ruudut liputettu)")
        tila["lopputulos"] = "Voitto!"
        lopetustoiminta()
        return
    if tila["liput"] == tila["miinojen_maara"] and yhtalaisyydet < tila["miinojen_maara"]:
        print("Hävisit pelin (kaikki liput käytetty, mutta miinoja vielä liputtamatta)")
        tila["lopputulos"] = "Häviö"
        lopetustoiminta()
        return
    avaamattomat = sum(1 for i in range(tila["korkeus"]) for j in range(tila["leveys"])
                       if tila["nakyvakentta"][i][j] in [" ", "f"])
    if avaamattomat == tila["miinojen_maara"]:
        print("Onneksi olkoon, voitit pelin (kaikki miinattomat ruudut aukaistu)!")
        tila["lopputulos"] = "Voitto!"
        lopetustoiminta()

def tulostin():
    '''
    Lukee tiedot tiedostosta tilasto.txt, joka luodaan ensimmäisen pelin kanssa
    '''
    try:
        with open('tilasto.txt', 'r', encoding="utf-8") as tiedosto:
            tilastot = tiedosto.read()
            print(tilastot)
    except FileNotFoundError:
        print("Tilastotiedostoa ei ole olemassa (oletko pelannut yhtään peliä?)")
    print("Palataan alkuvalikkoon...")
    valikko()

def ohjeet():
    '''
    Lukee pelin ohjeet, jos se on valittu alussa painamalla 6.
    '''
    print("\nSÄÄNNÖT:\r\nKlikkaamalla haluamaasi ruutua hiiren vasemmalla näppäimellä\n"
          "\nTyhjä laatta - Avaa muut laata tämän ympäriltä ja paljasta lähimmät numerolaatat\n"
          "Numerolaatta - Kertoo kuinka montaa miinaa tämän laatan ympärillä on .\n"
          "Miinalaatta - Klikkaamalla ruutua, jossa on miina, häviät pelin.\n"
          "Voit asettaa hiiren oikeaa näppäimellä lipun, jos luulet että se on miina\n"
          "\nKun olet löytänyt kaikki miinat peli ilmoittaa että voitit pelin\n"
          "\nOnnea matkaan!\n")
    valikko()

def tulvataytto(lista, klikattux, klikattuy):
    '''
    Ensin luodaan lista, joka sisältää klikatun ruudun sijaintia. Määritellään
    pelikenttä. Ensin, jos klikattu ruutu on tyhjä, eli " " aloitetaan tulvatäyttö
    prosessi otetaan yksi koordinaattipari annetusta listasta asetetaan tämän ruudun arvoksi
    0 jos siinä ei ole lippua. Käydään tämän jälkeen läpi kaikki tarkasteltavan ruudun ympärillä
    olevat ruudut (myös diagonaalit) lasketaan ympäröivän ruutujen miinat, jos viereinen ruutu on
    tyhjä lisätään se ymparillalistaan, joten senkin vieressä olevat ruudut käydään läpi.
    '''
    ymparillalista = [(klikattux, klikattuy)]
    leveys = len(lista[0])
    korkeus = len(lista)
    if lista[klikattux][klikattuy] == " ":
        while ymparillalista:
            y, x = ymparillalista.pop()
            lista[y][x] = "0"
            if tila["nakyvakentta"][y][x] == "f":
                pass
            else:
                tila["nakyvakentta"][int(y)][int(x)] = "0"
            for uusiy in range(min(max(y-1, 0), korkeus), min(max(y+2, 0), korkeus)):
                for uusix in range(min(max(x-1, 0), leveys), min(max(x+2, 0), leveys)):
                    laske_miinat(uusix,uusiy, tila["kentta"])
                    if lista[uusiy][uusix] == " ":
                        ymparillalista.append((uusiy, uusix))

def alusta_kentta(leveys, korkeus, miinojen_maara):
    '''
    Alustaa pelikentän ensin tyhjillä merkeillä kaksiuloitteisen lista argumenteilla leveys
    ja korkeus. Nakyvakentta on se kaksiuloitteinen lista, jonka pelaaja näkee ja aluksi
    kaikki ruudut ovat tyhjiä. Miinoittaa satunnaisesti miinoja kentta listaan. Palauttaa
    sen jälkeen kentätä "kentta" sisältää pelin oikean tiedon, kun taas nakyvakentta
    on se mitä pelaaja näkee.
    '''
    kentta = [[" " for _ in range(leveys)] for _ in range(korkeus)]
    nakyvakentta = [[" " for _ in range(leveys)] for _ in range(korkeus)]
    miinoita(kentta, miinojen_maara)
    return kentta, nakyvakentta

def main():
    '''
    Nollataan tietyt muutujat heti alussa, että tiedostoon tulee oikeat ajat
    ja muutenkin peli toimii.
    Alustaa kentän ensin yllä olevalla funktiolla. Tämän jälkeen lataa kuvat
    spritet tiedostosta. Tämän jälkeen luo ikkunan ja kertoo sen pikselien
    määrällä, että saadaan oikean kokoinen ikkuna. Tämän jälkeen asetetaan
    käsittelijöitä ensin piirretään peli kenttä, kun peli-ikkuna päivitetään.
    Sitten funktio, joka käsittelee hiiren klikkaukset. Sitten funktio, joka 
    päivittää pelin ajastinta, joka minuutti. Tämän jälkeen käynnistetään peli
    ja viimeisenä on siksi aloita, koska täten peli pysyy loopissa koko ajan aina
    kun sulkee pelin se kysyy uutta peliä terminaalissa. Tämän oisi varmaan voinut 
    tehdä paremminkin. Ja jos tulee liian suuri pelikenttä niin mennään memory
    errorilla takaisin päävalikkoon.
    '''
    tila["lopputulos"] = None
    tila["klikkaukset"] = 0
    tila["liput"] = 0
    tila["kulunutaika"] = 0
    try:
        tila["kentta"], tila["nakyvakentta"] = alusta_kentta(tila["leveys"],
        tila["korkeus"], tila["miinojen_maara"])
        ha.lataa_kuvat("spritet")
        ha.luo_ikkuna(tila["leveys"] * 40, tila["korkeus"] * 40)
        ha.aseta_piirto_kasittelija(piirra_kentta)
        ha.aseta_hiiri_kasittelija(kasittele_hiiri)
        ha.aseta_toistuva_kasittelija(sekuntikello, 1)
        ha.aloita()
        valikko()
    except MemoryError:
        print("Kenttä on liian suuri. Yritä pienemmällä kentällä.")
        valikko()

if __name__ == "__main__":
    valikko()
