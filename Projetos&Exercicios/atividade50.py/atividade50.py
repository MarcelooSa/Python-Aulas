# Leia o nome do aluno e três notas (0–10). Calcule a média aritmética e mostre:
# “Aprovado” (média ≥ 7.0), “Recuperação” (5.0–6.9) ou “Reprovado” (< 5.0).
# Exiba: Nome: <nome> | Média: X.Y | Situação: <...>.

nome = str(input("Digite o nome do aluno: "))
nota1 = float(input("Digite a 1ª nota: "))
nota2 = float(input("Digite a 2ª nota: "))
nota3 = float(input("Digite a 3ª nota: "))
media = (nota1+nota2+nota3) / 3
if media >= 7:
    print(f"Nome: {nome} | Média: {media:.2f} | Situação: Aprovado")
elif media >= 5 and media < 7:
    print(f"Nome: {nome} | Média: {media:.2f} | Situação: Em Recuperação")
elif media < 5:
    print(f"Nome: {nome} | Média: {media:.2f} | Situação: Reprovado")