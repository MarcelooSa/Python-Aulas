print("Sistema de Cálculo Média Bimestral")
nome = input("Digite seu nome:")
min = float(input("Qual a nota necessária para passar?"))
nota_ap = float(input("Digite a sua nota na avaliação parcial:"))
nota_ag = float(input("Digite a sua nota na avaliação global:"))
nota_c = float(input("Digite a sua nota na construída:"))
media = ((nota_ap+nota_ag+nota_c)/3)
if media >= min:
    print("Sua média é", media, "! Parabéns, aprovado!")
else:
    print("Sua média é", media, "! Você não passou, reprovado! ;(.")

