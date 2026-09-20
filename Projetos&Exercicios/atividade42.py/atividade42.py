# Cadastro de Produtos
# Peça o nome e preço de 5 produtos usando um laço for.
# Ao final, exiba o nome de todos e a soma total dos preços.

produtos = []
precos = []

for i in range(5):
    nome = input(f"Digite o nome do produto {i+1}: ")
    preco = float(input(f"Digite o preço do produto {i+1}: R$ "))
    produtos.append(nome)
    precos.append(preco)

print("\nLista de produtos cadastrados:")
for nome in produtos:
    print(nome)

soma_precos = sum(precos)
print(f"\nSoma total dos preços: R$ {soma_precos:.2f}")