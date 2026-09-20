# Cadastre pares nome e nota (0–10) repetidamente até o usuário digitar "fim" no nome.
# Ao final:
# mostre a quantidade de alunos;
# a média da turma;
# o melhor e o pior aluno (nome e nota).
# Desconsidere cadastros vazios e valide notas fora do intervalo.

classe = {}
while True:
    aluno = input("Digite o nome do aluno ou 'fim' para encerrar: ").strip()
    if aluno.lower() == "fim":
        break
    if aluno == "":
        print("Ops! Espaços vazios não são permitidos. Tente novamente.")
        continue
    try:
        nota = float(input(f"Digite a nota do {aluno} (0–10): "))
    except ValueError:
        print(f"{nota} não é um valor válido. Tente novamente.")
        continue
    if nota < 0 or nota > 10:
        print("Nota fora do intervalo permitido (0–10). Tente novamente.")
        continue
    classe[aluno] = nota
if not classe:
    print("\nNenhum aluno cadastrado.")
else:
    qtd_alunos = len(classe)
    media_turma = sum(classe.values()) / qtd_alunos
    melhor_aluno = max(classe, key=classe.get)
    pior_aluno = min(classe, key=classe.get)

    print("\n--- RESULTADOS ---")
    print(f"- Há {qtd_alunos} aluno(s) na sala.")
    print(f"- A média da turma é {media_turma:.2f}.")
    print(f"- Melhor aluno: {melhor_aluno} (nota {classe[melhor_aluno]:.1f})")
    print(f"- Pior aluno: {pior_aluno} (nota {classe[pior_aluno]:.1f})")