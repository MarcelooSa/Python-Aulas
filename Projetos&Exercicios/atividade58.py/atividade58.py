# Leia uma frase e mostre:
# A palavra mais longa e a mais curta.
# A quantidade total de palavras digitadas.
# Dica: use split().
texto = str(input("Digite uma frase: ")).split()
print(f"A menor palavra é: {min(texto,key=len)} e a maior palavra é: {max(texto,key=len)}.")