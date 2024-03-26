
# importing the random module
import random
numere=[random.randint(1,49) for nr in range(6)]
numere_jucate=[int(input("ghiciti numarul, introduce numar \n  ")) for nr in range(6)]
numere_comune=[nr for nr in numere_jucate if nr in numere]
print("numerele random", numere)
print("numrele jucate", numere_jucate)
print("numerele comune", numere_comune)
categorii={6:1, 5:2, 4:3, 3:4}
print("categoria : ", categorii.get (len(numere_comune), 0))
##sau varianta 2
print("categoria : ", categorii[len(numere_comune)] if len(numere_comune) in categorii else  0)
