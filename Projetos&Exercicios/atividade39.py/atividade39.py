# Sistema de Pedidos Online
# Peça o valor total do pedido e o método de entrega: "retirada" ou "entrega".

# Se for entrega e o valor for menor que R$ 50, cobre taxa de R$ 10.

# Caso contrário, o frete é grátis.
# Mostre o valor final a pagar.

valort = float(input("Digite o valor total (EM R$): "))
metodo = int(input("Método de entrega: digite 0 se for retirada; digite 1 se for entrega: "))
if (metodo == 1 and valort < 50):
    print(f"Será cobrado uma taxa de R$10,00 pela entrega. O valor total do pedido é: R${valort + 10}.")
else:
    print(f"O frete é grátis. O valor total do pedido é: R${valort}")
