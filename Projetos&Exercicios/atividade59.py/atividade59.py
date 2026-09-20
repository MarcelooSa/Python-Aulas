# Centímetros, milímetros e quilômetros.
# Mostre todos os resultados formatados.
# Exemplo: 1.5m → 150cm | 1500mm | 0.0015km.
valor = float(input("Digite um valor em metros(m): "))
print(f"{valor}m → {valor*100:.0f}cm | {valor*1000:.0f}mm | {valor/1000:.4f}km")