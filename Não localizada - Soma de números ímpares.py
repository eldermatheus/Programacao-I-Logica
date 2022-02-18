count = 0
numeros = []

while count < 1000:

    numeros.append(int(input()))
    if numeros[count] == -1:
        break
    count += 1

# retira o -1 da lista
numeros.pop()
soma = 0

for n in numeros:
    while n > 0:
        resto = n % 10
        if resto % 2 != 0:
            soma += resto
        n = n // 10

    print(soma)
    soma = 0
