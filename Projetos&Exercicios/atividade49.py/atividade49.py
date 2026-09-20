# Controle de Tarefas de Desenvolvimento
# Peça ao usuário quantas tarefas ele precisa realizar hoje.
# Com um for, exiba “Tarefa X concluída” até todas estarem finalizadas.

tarefas = int(input("Quantas tarefas você precisa realizar hoje?: "))
for i in range(1, tarefas+1, 1):
    print(f"Tarefa {i} concluída.")
print(f"Todas as {tarefas} tarefas foram concluídas!")