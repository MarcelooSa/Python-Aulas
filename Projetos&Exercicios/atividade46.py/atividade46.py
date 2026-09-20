# Sistema de Avaliação Contínua
# Permita que o usuário digite notas enquanto desejar (perguntando se quer continuar).
# Ao final, exiba a média geral e quantas notas foram informadas.

soma = 0
contador = 0
continuar = "s"
while continuar == "s":
    notas = float(input("Digite sua nota: "))
    contador += 1
    soma += notas
    continuar = str(input("Deseja continuar?(s/n): "))
print(f"Ao todo foram {contador} notas informadas e a média geral foi: {soma/contador:.2f}")   