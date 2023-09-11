bool = False
ingredienti = []
while bool == False:
    ingrediente = input("Inserisci una serie di ingredienti oppure (ESC) per uscire: ")
    ingrediente = str(ingrediente)
    if (ingrediente == "ESC"): 
        bool = True
        print(f"Lista di ingredienti: {ingredienti}")
    else: 
        ingredienti.append(ingrediente)
        print(f"{ingrediente.title()} sarà aggiunto/a alla pizza.")