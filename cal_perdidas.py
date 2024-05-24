def calcular_calorias_perdidas(velocidade, peso, constante, tempo):
    # Calcular as calorias perdidas
    calorias_perdidas = velocidade * peso * constante * tempo
    return round(calorias_perdidas, 2)

# Exemplo de uso
velocidade = 10  # km/h
peso = 70       # kg
constante = 0.0175  # Fator de conversão
tempo = 1.5     # horas

# Calcular as calorias perdidas
calorias_perdidas = calcular_calorias_perdidas(velocidade, peso, constante, tempo)

#Exibir apresentação
print("\n### Cálculo para calorias perdidas### \n")
# Imprimir o resultado com duas casas decimais
print("Calorias perdidas:", "{:.2f}".format(calorias_perdidas))
