import random
#Generate 5 random numbers between 10 and 30
randomlist_int = random.sample(range(10, 40), 5)
print(randomlist_int)
for floatlist in randomlist_int:
    print(float(floatlist), end=' ')