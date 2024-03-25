
# importing the random module
import random
numere=[random.randint(1,49) for i in range(6)]
print(numere)
numar_jucat=int(input("ghiciti numarul, introduce numar \n  "))
for nr in numere:   
    if numar_jucat == nr:
        print("Numarul extras se afla in numerele jucate")
        break
else:
       print("Numarul extras NU se afla in numerele jucate") 
print(any ([numar_jucat == nr for nr in numere]))
