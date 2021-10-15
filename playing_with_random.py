import random
lst = [1, 3, 5, 7, 9, 11, 13, 15]

for x in range(1000):
    i, j, k = random.randint(
        lst[0], lst[-1]), random.randint(lst[0], lst[-1]), random.randint(lst[0], lst[-1])
    if i + j + k == 30:
        print(i, j, k)
