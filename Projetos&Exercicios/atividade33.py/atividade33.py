# Peça o valor que o usuário deseja sacar. O sistema só deve permitir saques múltiplos de 10. Caso contrário, exiba “Valor inválido para saque.” Se o valor for válido, exiba “Saque autorizado.”
saque = float(input("Digite o valor que você deseja sacar: "))
if (saque % 10 == 0):
    print("Saque autorizado!")
else: 
    print("Valor inválido para saque.")