sandwich_orders = ["Grilled cheese", "Pastrami", "Grilled chicken", "Turkey", "Pastrami", "Roast beef", "Ham", "BLT", "Club", "Bacon", "Pastrami"]
finished_orders = []
for sandwich in sandwich_orders:
    finished_orders.append(sandwich)
print(f"Ordini completati pre filtro: {finished_orders}")
while True:
    for x in finished_orders:
        if x == "Pastrami": finished_orders.remove(x)
    break
print(f"Ordini completati post filtro: {finished_orders}")