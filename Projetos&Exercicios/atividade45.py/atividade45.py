# Controle de Temperatura de Servidores
# Leia 5 temperaturas e mostre a média delas.
# Use um laço para fazer as leituras e cálculos.
temperatura_soma = 0.0
temperaturas_todas = []

for i in range(5):
    temperaturas = float(input(f"Digite a temperatura {i+1}: "))
    temperaturas_todas.append(temperaturas)

temperaturas_soma = sum(temperaturas_todas)
media = temperaturas_soma / 5
print(f"A média de temperaturas é: {media}C°.")

    
