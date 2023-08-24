def nayta_tulokset(tiedosto):
    "nayttää tulokset"
    try:
        with open(tiedosto) as lahde:
            for rivi in lahde.readlines():
                nimi1, nimi2, piste1, piste2 = rivi.split(",")
                lista = {
                     'n1': nimi1.strip(),
                     'n2': nimi2.strip(),
                     'p1': piste1.strip(),
                     'p2': piste2.strip()
                }
                print(f"{lista['n1']} {lista['p1']} - {lista['p2']} {lista['n2']}")
    except IOError:
        print("Tiedoston avaaminen ei onnistunut. Aloitetaan tyhjällä kokoelmalla")

nayta_tulokset("hemulicup.csv")
