# Em um sistema de gestão, apenas usuários com o perfil "Administrador" podem acessar o painel de configurações. Peça ao usuário para digitar seu perfil e exiba se ele tem permissão ou não para acessar.
print("Seja bem vindo(a) ao sistema de gestão!")
perfil = str(input("Digite o seu perfil: "))
if (perfil == "Administrador"):
    print("Acesso permitido.")
else:
    print("Acesso negado. Você não tem permissão para isso.")
