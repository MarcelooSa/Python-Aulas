# Em um sistema de vendas, o cliente deve receber 10% de desconto se for cadastrado como “VIP”. Caso contrário, se o valor da compra for maior que R$ 500, receba 5% de desconto. Em outros casos, não há desconto.

cadastro = str(input("Possui cadastro VIP? (s/n): "))
produto = float(input("Digite o valor da compra: "))
if (cadastro == "s") and (produto < 500):
    desconto =produto*0.10
elif (cadastro == "s") and (produto >= 500):
    desconto = produto*0.05
else:
    desconto = 0
print(f"O valor final será de {produto - desconto:.2f}, com desconto de R${desconto:.2f}!")