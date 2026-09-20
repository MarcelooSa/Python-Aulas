# Peça ao usuário um ano e verifique se ele é bissexto. (Um ano é bissexto se for divisível por 4 e não for por 100, ou se for divisível por 400.)
ano = int(input("Digite o ano: "))
if (ano % 4 == 0 and ano % 400 != 0) or (ano % 400 == 0):
    print(f"{ano} é um ano bissexto.")
else:
    print(f"{ano} não é um ano bissexto")