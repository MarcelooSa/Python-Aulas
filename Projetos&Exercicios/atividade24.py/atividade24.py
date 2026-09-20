# Validação de Acesso a um Sistema Interno
# Peça o cargo e o turno do funcionário.
# Apenas administradores que trabalham no turno da manhã podem acessar o painel de controle.
# Use operadores lógicos para validar.
# Use operadores lógicos para validar.

cargo = str(input("Qual o seu cargo?"))
turno = str(input("Qual o seu turno?"))
if (cargo == "Administrador") and (turno == "Manhã"):
    print("Acesso permitido.")
else:
    print("Acesso negado. Apenas administradores podem acessar.")