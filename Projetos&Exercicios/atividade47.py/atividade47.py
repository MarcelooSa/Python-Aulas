# Contagem Regressiva para Inicialização do Sistema
# Use for para exibir uma contagem regressiva de 10 até 0 e, ao final, mostre “Sistema inicializado com sucesso!”

import time
for i in range (10, -1, -1):
    print(i)
    time.sleep(1)
print("Sistema inicializado com sucesso!")