import random

lo = int(input("Enter the down range number :"))
hi = int(input("Enter the up range number :"))

randomNumber = random.randrange(lo, hi, 1)
print("The random Number between the provided range is :", randomNumber)
