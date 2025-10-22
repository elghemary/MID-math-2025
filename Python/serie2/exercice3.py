nombre = int(input('entrer un nombre'))
i = 0
pi = 0
while i < nombre:
    pi += ((-1)** i )/(2 * i + 1)
    i += 1
pi *= 4
print(pi)