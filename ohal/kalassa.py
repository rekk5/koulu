def kysy_salasana():
    while True:
        sala = input("Kirjoita salasana: ")
        if len(sala) <= 8:
            print("Salasanan tulee olla vähintään 8 merkkiä pitkä")
        if len(sala) >= 8:            
            break
    return sala
print(kysy_salasana())
