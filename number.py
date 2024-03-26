
# importing the random module
import random
numere=[random.randint(1,49) for i in range(6)]
numere_jucate=[]

for nr in range(6):   
    numar_jucat=int(input("ghiciti numarul, introduce numar \n  "))
    numere_jucate.append(numar_jucat)
numere_comune=[]
for nr in numere_jucate:
    if nr in numere:
       numere_comune.append(nr)
print("numerele random", numere)
print("numrele jucate", numere_jucate)
print("numerele comune", numere_comune)
# for nr in numere_jucate:
