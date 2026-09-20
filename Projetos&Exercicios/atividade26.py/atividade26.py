# Peça a média final de um aluno e exiba o resultado conforme as regras: média ≥ 7 → “Aprovado”, média entre 5 e 6.9 → “Recuperação”, média < 5 → “Reprovado.”

mediafinal = float(input("Digite a sua média final: "))
if (mediafinal >= 7):
    print("Aprovado.")
elif (mediafinal >= 5) and (mediafinal < 7):
    print("Recuperação.")
else:
    print("Reprovado.")
