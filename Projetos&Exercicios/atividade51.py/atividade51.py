# Leia um inteiro e informe:
# se é par ou ímpar;
# se é positivo, negativo ou zero;
# se é múltiplo de 5.
# Ex.: -10 → “Par, Negativo, Múltiplo de 5”.

inteiro = int(input("Digite o número inteiro: "))
if inteiro % 2 == 0:
    paridade = "Par"
else:
    paridade = "Ímpar"
if inteiro > 0:
    sinal = "Positivo"
elif inteiro == 0:
    sinal = "0"
else:
    sinal = "Negativo"
if inteiro % 5 == 0:
    multiplo = "Múltiplo de 5"
else:
    multiplo = "Não é múltiplo de 5"
print(f"{inteiro} -> {paridade}, {sinal}, {multiplo}.")
