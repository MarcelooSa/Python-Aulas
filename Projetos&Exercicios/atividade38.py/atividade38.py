# Classificação de Temperatura de CPU com Risco
# Receba a temperatura da CPU e mostre o status:

# Até 50°C → “Normal”

# De 51°C a 70°C → “Atenção”

# Acima de 70°C → “Crítico”
# E se o valor for negativo ou acima de 150°C, exiba “Erro: leitura inválida.”

temperatura = float(input("Digite a temperatura da CPU em C°: "))
if (temperatura <= 50):
    print("Normal.")
elif (temperatura <= 51 and temperatura <= 70):
    print("Atenção.")
elif (temperatura > 70 and temperatura <= 150):
    print("Crítico.")
elif (temperatura < 0 or temperatura > 150):
    print("Erro: leitura inválida.")