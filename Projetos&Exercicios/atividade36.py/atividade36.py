# Sistema de Avaliação de Software
# Peça três notas (usabilidade, desempenho e segurança).
# O sistema será Aprovado se todas as notas forem ≥ 7.
# Se pelo menos uma for menor que 5, exiba “Reprovado”.
# Caso contrário, exiba “Necessita melhorias”.

usabilidade = float(input("Digite a nota de usubilidade do software: "))
desempenho = float(input("Digite a nota de desempenho do software: "))
segurança = float(input("Digite a nota de segurança do software: "))
if (usabilidade >= 7 and desempenho >= 7 and segurança >= 7):
    print("Sistema aprovado.")
elif (usabilidade < 5 or desempenho < 5 or segurança < 5):
    print("Sistema reprovado.")
else:
    print("O Sistema necessita de melhorias.")