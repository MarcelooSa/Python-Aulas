# Peça ao usuário que informe sua idade. Caso tenha menos de 18 anos, exiba “Acesso permitido apenas para maiores de idade.” Se tiver 60 anos ou mais, exiba “Acesso preferencial.” Caso contrário, exiba “Acesso liberado.”

idade = int(input("Digite a sua idade: "))
if (idade < 18):
    print("Acesso permitido apenas para maiores de idade.")
elif (idade >= 60):
    print("Acesso preferencial.")
else:
    print("Acesso liberado.")