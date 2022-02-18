N = int(input()) #Tamanho Array
numbers = list(map(int,input().split())) #Convertemos cada elemento da lista de string em inteiro
min_value = min(numbers) #Pegamos o menor valor da lista
max_value = max(numbers)

position = numbers.index(min_value) #Pegamos o indice do menor valor da lista
print("Menor valor: %i" %min_value)
print("Posicao: %i" %position)

position = numbers.index(max_value) #Pegamos o indice do menor valor da lista
print("Maior valor: %i" %max_value)
print("Posicao: %i" %position)
