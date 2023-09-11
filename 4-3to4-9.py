#4.3
print("Lista da 1 a 20: ", list(range(1,21)))
#4.4
boolOneMillion = False
oneMillion = list(range(1, 1000001)) 
print(oneMillion) if boolOneMillion else []
#4.5
boolMinMaxSum = False
min = min(oneMillion)
max = max(oneMillion)
sum = sum(oneMillion)
print("Minimo: %d, Massimo: %d, Somma: %d" % (min, max, sum)) if boolMinMaxSum else []
#4.6
print("Lista pari da 1 a 20: ", list(range(2,21, 2)))
#4.7
print("Lista multipli di 3: ", list(range(3,31, 3)))
#4.8, 4.9
cubeValues = [num**3 for num in range(1, 11)]
for number in cubeValues:
    print("Cubo: ", number)
