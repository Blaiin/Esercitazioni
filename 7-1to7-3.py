#7.1 Rental car
rentalCar = input("Che macchina vorresti noleggiare? ")
rentalCar = str(rentalCar)
print(f"Vedrò se posso trovare una {rentalCar.title()} per te")
#7.2
seating = input("Per quante persone è il tavolo? ")
seating = int(seating)
if seating > 8:
    print("Dovrete aspettare per un tavolo.")
else:
    print("Il vostro tavolo è pronto.")
#7.3
number = input("Inserisci un numero: ")
number = int(number)
if number % 10 == 0:
    print("Il numero è multiplo di 10.")
else: 
    print("Il numero non è multiplo di 10.")