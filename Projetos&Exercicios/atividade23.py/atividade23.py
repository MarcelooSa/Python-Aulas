# Solicite ao usuário que escolha um método de pagamento: "pix", "cartão" ou "dinheiro". 
# Mostre uma mensagem diferente para cada opção, como “Pagamento instantâneo via Pix” ou “Pagamento processado no cartão.”

metodo = int(input("Escolha um método de pagamento: Digite 1 para pagamentos em pix, 2 para pagamentos no cartão e 3 para pagamento em dinheiro: "))
if (metodo == 1):
    print("Aguarde o QR Code.")
elif (metodo == 2):
    print("O pagamento será processado no cartão")
elif (metodo == 3):
    print("Entregue o dinheiro ao caixa.")
else:
    print("Insira uma opção válida!")
