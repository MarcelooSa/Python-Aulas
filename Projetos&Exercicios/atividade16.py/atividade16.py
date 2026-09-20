# Converta a tupla (5, 8, 12) em uma lista, adicione o número 20 e converta de volta em tupla.

tupla_ = (5, 8, 12)
lista = list(tupla_)
lista.append(20)
tupla_vinte = tuple(lista)
print(type(tupla_vinte))