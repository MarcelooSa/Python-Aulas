# Atividade 08

# Peça ao usuário:
# Nome
# Ano de nascimento
# Calcule sua idade aproximada e mostre a mensagem:
# ___, você tem ___ anos.

print("Quantos anos eu tenho?")
nome = input("Digite o seu nome: ")
ano_nascimento = int(input("Digite o ano de nascimento: "))
idade_aprox = 2025 - ano_nascimento
print(f"{nome}, você tem {idade_aprox} anos.")