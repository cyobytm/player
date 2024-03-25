
# importing the random module
import random
numere=[random.randint(0,100)]
userx=int(input("ghiciti numarul, introduce numar \n  "))
print("numarul random este ", numere)
if userx == numere:
    print("Ai ghicit")
else:
  print("Nu ai ghicit")