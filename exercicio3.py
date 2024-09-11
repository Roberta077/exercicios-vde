import json

faturamento_diario = json.loads('{"dias": [0, 1500, 2500, 1600, 0, 3500, 2000]}')

valores = faturamento_diario["dias"]
valores_validos = [v for v in valores if v > 0]
media_mensal = sum(valores_validos) / len(valores_validos)
menor_valor = min(valores_validos)
maior_valor = max(valores_validos)
dias_acima_media = sum(1 for v in valores_validos if v > media_mensal)

print(f"Menor valor: {menor_valor}")
print(f"Maior valor: {maior_valor}")
print(f"Número de dias acima da média: {dias_acima_media}")
