# Simule um sistema que solicita uma senha e, em seguida, um código de verificação. O login só deve ser autorizado se ambos estiverem corretos. Caso contrário, exiba uma mensagem de erro.
senha = str(input("Digite a sua senha: "))
codigo = int(input("Digite o código de verificação de seis dígitos: "))
if (senha == "python") and (codigo == 199530):
    print("Acesso autorizado.")
else:
    print("A senha ou o código de verificação estão incorretos.")