# Faça um dicionário com 3 frutas e seus respectivos preços. Depois, peça ao usuário para digitar o nome de uma fruta e exiba o preço correspondente.

frutas = {"Abacaxi": 3.99, "Goiaba": 2.99, "Melancia": 4.99}
fruta = str(input("Digite o nome da fruta: "))
if fruta in frutas: 
    print(f"O preço da {fruta} é: R${frutas[fruta]:.2f}")
else:
    print("Não temos essa fruta disponível. Desculpe!")