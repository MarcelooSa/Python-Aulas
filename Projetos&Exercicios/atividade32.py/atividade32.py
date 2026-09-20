# O sistema deve ler a média e a frequência do aluno. Ele será aprovado se tiver média ≥ 7 e frequência ≥ 75%. Caso contrário, estará reprovado. Mostre a situação final.
media = float(input("Digite a sua média: "))
frequencia = float(input("Digite a sua frequência: "))
if (media >= 7) and (frequencia >= 75):
    estado = "aprovado"
else:
    estado = "reprovado"
print(f"Com média {media:.1f} e frequência {frequencia:.2f}% você está {estado}!")
