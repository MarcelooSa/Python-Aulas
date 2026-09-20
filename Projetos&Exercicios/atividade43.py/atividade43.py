# Contador de Cliques em um Botão (Simulado)
# Simule um contador que pergunte quantas vezes o botão foi clicado e mostre mensagens como “Clique 1 registrado”, “Clique 2 registrado” até o número informado.

cliques = int(input("Digite a quantidade de cliques no botão deseja adicionar: "))
for i in range(1 , cliques+1):
    print(f"Clique {i} registrado!")