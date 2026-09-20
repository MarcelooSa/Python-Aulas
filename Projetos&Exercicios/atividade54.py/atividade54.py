# Leia 10 números inteiros e armazene-os em uma lista.
# Mostre a soma dos pares e a soma dos ímpares separadamente.
# Exemplo: [2, 3, 4, 5] → pares = 6, ímpares = 8.
lista = []
pares = []
impares = []
for i in range(10):
    numero = int(input(f"Digite o {i+1}º número inteiro: "))
    lista.append(numero)
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)
soma_pares = sum(pares)
soma_impares = sum(impares)
print(f"{lista} -> Soma dos pares: {soma_pares} | Soma dos ímpares: {soma_impares}")