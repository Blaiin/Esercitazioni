while True:
    age = input("Inserisci età (o '0' per uscire): ")
    age = int(age)
    if age == 0: break
    elif age <= 3: print("Il biglietto è gratuito.")
    elif (age > 3 and age <= 12): print("Il biglietto costa 12$.")
    else: print("Il biglietto costa 15$.")
    