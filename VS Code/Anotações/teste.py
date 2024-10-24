import arrow

# Obter a data atual
data_atual = arrow.now()

# Formatar a data no formato dia/mês/ano
data_formatada = data_atual.format("DD/MM/YYYY")

print("Data formatada:", data_formatada)

# Configurações de data usando arrow
hoje = arrow.now()
NUM_MES = hoje.month  # Número do mês (1-12)
MES = hoje.format('MMMM')  # Nome do mês completo
DIA = hoje.day  # Dia do mês
ANO_YYYY = hoje.year  # Ano completo (2024)
ANO_YY = hoje.format('YY')  # Ano abreviado (24)

print(f"dia {hoje} \n mes {MES}")