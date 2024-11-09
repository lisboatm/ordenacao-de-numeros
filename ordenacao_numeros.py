# Número de elementos
N = int(input())

# Listas para pares e ímpares
pares = []
impares = []

# Separando pares e ímpares
for _ in range(N):
    valor = int(input())
    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)

# Ordenação conforme critérios
pares.sort()
impares.sort(reverse=True)

# Exibindo a saída conforme o esperado
for numero in pares:
    print(numero)
for numero in impares:
    print(numero)
