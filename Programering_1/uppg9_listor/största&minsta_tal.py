import random

tal = [random.randint (1,1000) for i in range (100)]

minst = min(tal)
störst = max(tal)

print (f"Minsta talet är: {minst}")
print (f"Största telet är: {störst}")