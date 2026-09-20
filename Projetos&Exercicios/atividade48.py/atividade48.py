# Verificação de Senhas Fortes
# Permita que o usuário insira senhas até digitar uma com pelo menos 8 caracteres.
# Quando isso ocorrer, exiba “Senha válida, cadastro permitido.”

senha = ""
while len(senha) < 8:
    senha = input("Digite a senha correta: ")
print("Senha válida, cadastro permitido.")  