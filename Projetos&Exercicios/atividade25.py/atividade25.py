# Crie um programa que pergunte a quantidade de um produto em estoque. Se for igual a 0, exiba “Produto esgotado.” Se for até 5, exiba “Estoque baixo.” Caso contrário, exiba “Estoque normal.”

quantidade = int(input("Digite a quantidade de livros disponíveis: "))
if (quantidade == 0):
    print("Produto esgotado!")
elif (quantidade > 0) and (quantidade <= 5):
    print("Estoque baixo.")
else:
    print("Estoque normal.")