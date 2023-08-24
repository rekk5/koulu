def suodata_virhearvot(lista, arvo):
    for luku in lista[:]:
        if luku > arvo:
            lista.remove(luku)

mittaukset = [12.2, 54.2, 42345.2, 23534.1, 55.7, 8982.4]
suodata_virhearvot(mittaukset, 8000)
print(mittaukset)
