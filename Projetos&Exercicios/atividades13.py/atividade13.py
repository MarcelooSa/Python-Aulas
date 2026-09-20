# Peça ao usuário para digitar 3 notas e armazene em uma lista. Depois, calcule a média dessas notas.

print("Calcule sua média!")
lista = [float(input("Digite a sua 1ª nota: ")), float(input("Digite a sua 2ª nota: ")), float(input("Digite a sua 3ª nota: "))]
media = (lista[0]+lista[1]+lista[2]) / 3
print(f"A média das notas é: {media:.1f}.")

