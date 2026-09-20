# Crie uma lista de números de 1 a 10 e mostre apenas os números pares.

lista = [1,2,3,4,5,6,7,8,9,10]
for lista in range(1,11):
    if lista % 2 == 0:
        print(lista)