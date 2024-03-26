
# importing the random module
import random
numere=[random.randint(1,49) for nr in range(6)]
numere_jucate=[int(input("ghiciti numarul, introduce numar \n  ")) for nr in range(6)]
numere_comune=[nr for nr in numere_jucate if nr in numere]
print("numerele random", numere)
print("numrele jucate", numere_jucate)
print("numerele comune", numere_comune)
#varianta 3
print("categoria :", 7- len(numere_comune) if len(numere_comune) >= 3 else 0)

for nr in numere:
    if nr not in range(1,50):
        print(f"nu {nr}se afla in range")
        break
else:
    print("toate numerele se afla inre 1 si 49")
print(all([nr in range(1,50) for nr in numere]))
print(all([nr in range(1,50) for nr in numere_jucate]))
# verificam daca elementele din nr random sunt unice si nu se repeta cu ajutrul set de numere
print(len(numere) == len(set(numere)))
print("aici am printat setul de numere random", set(numere))

# verificam daca nr sunt unice din nr input
print(len(numere_jucate) == len(set(numere_jucate)))
print("aici am printat setul de numere random", set(numere_jucate))