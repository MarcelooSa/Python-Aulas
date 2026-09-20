# Crie um dicionário chamado notas com as chaves: Matemática, Português, História. Atribua valores (notas) e exiba a média.

notas = {"Matemática": 10.0, "Português": 7.5, "História": 9.5}
media = (notas["Matemática"] + notas["Português"] + notas["História"]) / 3
print(f"A sua média é {media:.2f}.")