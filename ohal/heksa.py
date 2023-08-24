def muotoile_heksaluvuksi(luku, bitti):
    luku_1 = hex(luku)[2:]
    luku_2 = luku_1
    nollat = int(bitti / 4)
    vastaus = luku_2.zfill(nollat)
    return vastaus
    
try:
    luku_3 = int(input("Anna kokonaisluku: "))
    bitti_3 = int(input("Anna heksaluvun pituus (bittien lukumäärä): "))
except ValueError:
    print("Kokonaisluku kiitos")
else:
    laskettu_vastaus = muotoile_heksaluvuksi(luku_3, bitti_3)
    print(f"{laskettu_vastaus}")
