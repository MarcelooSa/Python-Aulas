# Peça ao usuário uma palavra e exiba-a invertida, sem usar [::-1].
# Dica: utilize um for percorrendo de trás para frente ou reversed().

palavra = str(input("Digite uma palavra: "))
palavra_invertida = ""
for caractere in reversed(palavra):
    palavra_invertida += caractere
print(f'A palavra "{palavra}" invertida fica: {palavra_invertida}.')