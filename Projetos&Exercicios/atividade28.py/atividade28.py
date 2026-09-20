# Um sistema de monitoramento deve ler a temperatura de um servidor e classificar assim: até 60°C → “Normal”; entre 61°C e 80°C → “Atenção”; acima de 80°C → “Crítico — risco de superaquecimento!”.
temperatura = float(input("Digite a temperatura atual (em C°): "))
if (temperatura <= 60):
    print("Estado normal - A temperatura está dentro do esperado.")
elif (temperatura < 80): 
    print("Estado moderado -  A temperatura exige monitoramento.")
else:
    print("Estado crítico - risco de superaquecimento.")