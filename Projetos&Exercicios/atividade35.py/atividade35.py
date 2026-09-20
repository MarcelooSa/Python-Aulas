# O usuário informa sua categoria de cliente (bronze, prata, ouro, diamante) e o valor da compra.

# Bronze: sem desconto

# Prata: 5%

# Ouro: 10%

# Diamante: 15%
# Calcule e mostre o valor final com desconto.

categoria = str(input("Digite a sua categoria de cliente: "))
valor_compra = float(input("Digite o valor da compra: "))
if (categoria == "Bronze"): 
    desconto = 0*valor_compra
elif (categoria == "Prata"):
    desconto = 0.05*valor_compra
elif (categoria == "Ouro"):
    desconto = 0.1*valor_compra
elif (categoria == "Diamante"):
    desconto = 0.15*valor_compra
else:
    desconto = 0
print(f"Você pagará R${valor_compra - desconto} e seu desconto foi de R${desconto}!")