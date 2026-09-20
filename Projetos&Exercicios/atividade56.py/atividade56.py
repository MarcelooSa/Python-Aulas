# Receba uma frase e mostre:
# Quantas letras possui (ignorando espaços).
# Quantas vezes a letra “a” aparece (maiúscula ou minúscula).
# Em que posição ocorre a primeira e a última letra “a”.

frase = str(input("Digite uma frase: "))

qtd_letras = len(frase.replace(" ", "")) ## comando len faz a contagem e replace remove os caractereses e adiciona novos no lugar, no caso tirei os espaços com: " ", ""
frase_minuscula = frase.lower() ## o lower faz todo os caracteres da string ficarem minusculas
qtd_a = frase_minuscula.count('a') ## o count faz a contagem de a; nota-se que tem de ser o A maisculo também, mas como a gente deixou todo em minusculo com lower, ja deu certo (count so aceita 1 caractere para contar, por isso usamos lower antes)
primeiro_a = frase_minuscula.find('a') + 1 ## find busca a posição (tem de ser mais um pois o python começa a contar do 0 e não do 1)
ultimo_a = frase_minuscula.rfind('a') + 1 ## rfind busca a ultima posição (e como ele sempre vai contar do 0, vai estar sempre faltando 1, por isso da posição)

print(f"A frase possui {qtd_letras} letras (ignorando espaços).")
print(f"A letra 'a' aparece {qtd_a} vezes.")

if qtd_a > 0:
    print(f"A primeira letra 'a' está na posição {primeiro_a}.")
    print(f"A última letra 'a' está na posição {ultimo_a}.")
else:
    print("A letra 'a' não aparece na frase.")
