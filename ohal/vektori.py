def laske_pituus(v):
    nelio = 0
    for komponentti in v:
        nelio += komponentti ** 2
    return nelio ** 0.5

def yksikkovektoriksi(v): 
    u = []
    pituus = laske_pituus(v)
    # silmukan määrittely
    # silmukan sisältö (1 rivi)
    return u

print(yksikkovektoriksi([2.0, 2.0, 2.0, 2.0]))