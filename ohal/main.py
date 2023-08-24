import aasilogiikka
import aasikaytto
import aasimaaritelmat

def main():
    "määrä aasin toiminnan tietyissä syötteissä"
    aasidata = aasilogiikka.alusta()
    
    while True:
        aasikaytto.nayta_tila(aasidata)
        syote = aasikaytto.pyyda_syote(aasidata)
        
        if syote == aasimaaritelmat.LOPETA:
            break
        if syote == aasimaaritelmat.RUOKI:
            aasilogiikka.ruoki(aasidata)
        elif syote == aasimaaritelmat.KUTITA:
            aasilogiikka.kutita(aasidata)
        elif syote == aasimaaritelmat.TYOSKENTELE:
            aasilogiikka.tyoskentele(aasidata)
        elif syote == aasimaaritelmat.ALUSTA:
            aasidata = aasilogiikka.alusta()

if __name__ == "__main__":
    main()
