# Atividade 10 – Conversão de Unidades
# Peça ao usuário um valor em metros.
# Converta e mostre o resultado em centímetros e milímetros.

print("Conversor de Metros para Centímetros e Milímetros")
metros = float(input("Digite o valor em metros: "))
centimetros = metros * 100
milimetros = metros * 1000
print(f"{metros} metros são {centimetros} centímetros e {milimetros} milímetros!")