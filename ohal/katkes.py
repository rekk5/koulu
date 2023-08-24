def kysy_arvot():
    "kysyy arvon ja lisääsen listaan"
    mittaukset = []
    while True:
        syote = input("Anna vastusarvo: ")
        try:
            arvo = float(syote)
            if syote == " ":
                break
            if arvo == 0:
                break
        except ValueError:
            if not syote:
                return mittaukset
            print("Komponentin arvon on oltava nollaa suurempi luku.")
        else:
            mittaukset.append(arvo)   
    return mittaukset
    
def laske_sarja(mittaukset3):
    "laskee sarjan"
    sarjaresistanssi4 = float(sum(mittaukset3))
    return sarjaresistanssi4

def laske_rinnan(mittaukset2):
    "laskee rinnan"
    jakaja = 1
    jakajat = [jakaja/i for i in mittaukset2]
    rinnanresistanssi2 = float(1 / sum(jakajat))
    return rinnanresistanssi2

x1 = kysy_arvot()
if sum(x1) == 0:
    print(" ")
else:
    sarjaresistanssi = laske_sarja(x1)
    rinnanresistanssi = laske_rinnan(x1)
    print(sarjaresistanssi)
    print(rinnanresistanssi)
