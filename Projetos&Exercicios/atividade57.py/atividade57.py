# Leia idades de várias pessoas até que o usuário digite -1.
# Calcule a média das idades somente dos maiores de 18 anos.
# Se não houver maiores de idade, exiba mensagem apropriada.
idades = []
maior = []
media = 0
idade = 0
while idade != -1:
    idade = int(input("Digite a idade: "))
    idades.append(idade)
    if idade >= 18:
        maior.append(idade)
if idade > 0: 
    media = (sum(maior))/(len(maior))
if media >= 18:
    print(f"Idades maioridade: {maior}\nMédia das idades: {media}")
else:
    print("Não há nenhum maior de idade para a média.")