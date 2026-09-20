# Validação de CPF Simples
# Peça ao usuário para digitar um CPF (apenas números). Se ele tiver exatamente 11 dígitos, exiba “CPF válido.” Caso contrário, exiba “CPF inválido.”

cpf = int(input("Digite o seu CPF sem os caracteres: "))
if len(str(cpf)) == 11:
    print("CPF válido.")
else:
    print("CPF inválido.")