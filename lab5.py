import random

results = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
i = 1
while i <= 10000:
    diceRoll1 = random.randint(1,6)
    diceRoll2 = random.randint(1,6)
    result = diceRoll1 + diceRoll2
    results[result - 2] += 1
    i += 1
print(results)
