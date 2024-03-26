
# importing the random module
import random
numere=[random.randint(1,49) for nr in range(6)]
numere_jucate=[int(input("ghiciti numarul, introduce numar \n  ")) for nr in range(6)]
numere_comune=[nr for nr in numere_jucate if nr in numere]
print("numerele random", numere)
print("numrele jucate", numere_jucate)
print("numerele comune", numere_comune)

