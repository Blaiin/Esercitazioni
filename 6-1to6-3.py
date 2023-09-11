#6.1
persone = {
    'nome': 'Lorenzo',
    'cognome': 'Andreucci',
    'età': 27,
    'città': 'Reggio Calabria'
}
print("Persone:")
for key, value in persone.items():
    print(f'\t{key}: {value}')
#6.2
numeriPref = {
    'Andrea': 10,
    'Lorenzo': 3,
    'Jessica': 27,
    'Ginevra': 9,
    'Matteo': 7
}
print("Numeri preferiti:")
for key, value in numeriPref.items():
    print(f'\t{key}: {value}')
#6.3
glossary = {
    'variable': 'variabile che può assumere qualsiasi valore',
    'for loop': 'ciclo iterativo che può essere usato per stampare, ad esempio, tutti i valori di una lista',
    'dictionary': 'lista di chiave-valore',
    'function': 'funzione o metodo che applica ed/o esegue della logica o operazioni',
    'class': 'blueprint per la creazione di oggetti con attributi, metodi e costruttore/i'
}
print("Dizionario:")
for key, value in glossary.items():
    print(f'\t{key}: \n\t{value}')