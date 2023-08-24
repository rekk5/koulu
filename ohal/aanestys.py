verouudistus = {
    "jaa": 0,
    "ei": 0,
    "eos": 0,
    "virhe": 0
}
nalle_puh_presidentiksi = {
    "jaa": 12,
    "ei": 0,
    "eos": 5,
    "virhe": 4
}

def aanesta(verolista):
    aani = input("Anna äänesi, vaihtoehdot ovat: ").lower()
    if aani == "jaa":
        verolista["jaa"] = verolista["jaa"] + 1
    elif aani == "ei":
        verolista["ei"] = verolista["ei"] + 1
    elif aani == "eos":
        verolista["eos"] = verolista["eos"] + 1
    else:
        verolista["virhe"] = verolista["virhe"] + 1

def nayta_tulokset(verolista2):
    print(f"Jaa : {'#'*verolista2['jaa']}")
    print(f"Ei : {'#'*verolista2['ei']}")
    print(f"Eos : {'#'*verolista2['eos']}")
    print(f"Virhe : {'#'*verolista2['virhe']}")

aanesta(verouudistus)
nayta_tulokset(verouudistus)
aanesta(nalle_puh_presidentiksi)
nayta_tulokset(nalle_puh_presidentiksi)
