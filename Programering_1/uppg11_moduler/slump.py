from math import sqrt

import random

antal = int(input("Hur många tal vill du ha? "))

for i in range (antal):
    random_num = random.randint (1,100)
    print (random_num)
    print (sqrt(random_num))