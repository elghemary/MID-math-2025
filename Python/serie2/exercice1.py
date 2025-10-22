nombre = int(input('entrer un nombre'))
fibonacci0 = 0
fibonacci1 = 1
fibonacci = 0
i = 1

for i in range(0, nombre):
    print(fibonacci0)
    fibonacci = fibonacci1 + fibonacci0
    fibonacci0 = fibonacci1
    fibonacci1 = fibonacci
