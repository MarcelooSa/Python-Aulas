# Peça a quantidade q (q>0). Leia q inteiros e armazene em uma lista.
# Exiba: maior, menor, média com 2 casas, quantos pares e quantos ímpares.
# Ex.: [5, 2, 9, 2] → maior=9, menor=2, média=4.50, pares=2, ímpares=2.
# Peça a quantidade q (q>0). Leia q inteiros e armazene em uma lista.
# Exiba: maior, menor, média com 2 casas, quantos pares e quantos ímpares.
inteiro = []
pares = []
impares = []
quantidade = 0
while quantidade <= 0:
    quantidade = int(input("Digite quantos números inteiros serão lidos: "))
    if quantidade <=0:
        print(f"{quantidade} não é um número válido. Digite um valor igual ou maior que 1.")
if quantidade > 0:
    for i in range(quantidade):
        inteiros = int(input(f"Digite o {i+1}º inteiro: "))
        inteiro.append(inteiros)
        if inteiros % 2 == 0 or inteiros == 0:
            pares.append(inteiros)
        else:
            impares.append(inteiros)
    print(f"{inteiro} -> Maior: {max(inteiro)}, Menor: {min(inteiro)}, Pares = {len(pares)}, Ímpares = {len(impares)}, Média = {(sum(inteiro))/quantidade:.1f}.")