import random
import time

flower = ["She loves me.", "She loves me not."]
while True:
    petal = random.choice(flower)
    print(petal)
    time.sleep(2)
