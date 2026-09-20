# Crie um programa que permita até 3 tentativas de login. Se o usuário errar o nome ou senha três vezes, o acesso deve ser bloqueado e o programa exibirá “Usuário bloqueado por excesso de tentativas.”
usuario_valido = "Marcelo"
senha_correta = "python2009"
usuario = str(input("Digite o seu nome: "))
senha = str(input("Digite sua senha: "))
if (usuario == usuario_valido) and (senha == senha_correta):
    print("Login autorizado.")
else:
    print("Usuário ou senha incorretos. Tente novamente!")
    usuario = str(input("Digite o seu nome: "))
    senha = str(input("Digite sua senha: "))
    if (usuario == usuario_valido) and (senha == senha_correta):
        print("Login autorizado.")
    else:
        print("Usuário ou senha incorretos. Tente novamente!")
        usuario = str(input("Digite o seu nome: "))
        senha = str(input("Digite sua senha: "))
        if (usuario == usuario_valido) and (senha == senha_correta):
            print("Login autorizado.")
        else:
            print("Usuário bloqueado por excesso de tentativas.")

