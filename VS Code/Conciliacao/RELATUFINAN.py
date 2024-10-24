import pandas as pd

# Caminho do arquivo CSV
arquivo_csv = r'C:\Users\rodrigo.oliveira_war\Downloads\RLATUFINANCEIRO - 2024-08-01T172159.885.CSV'

# Abra o arquivo CSV usando pandas
df_recentes = pd.read_csv(arquivo_csv)

# Imprima as colunas do arquivo CSV
print("Colunas do arquivo CSV:")
print(df_recentes.columns.tolist())

# Carregar o arquivo de conciliação
caminho_arquivo_conciliacao = r'G:\Drives compartilhados\#Crossing - Diretoria COO\Distribuição Plataforma\Renda Fixa\RENDA FIXA - BACKOFFICE\CONCILIAÇÃO - Custódia\Conciliação - Renda Fixa\Conciliacao.xlsx'
df_conciliacao = pd.read_excel(caminho_arquivo_conciliacao, sheet_name='Base_Eventos_Virtual')

# Crie uma lista com as colunas desejadas
colunas = ['Data', 'Matricula', 'Cliente', 'Cpf_Cnpj', 'Boleta', 'historico', 'Cod Titulo', 'Titulo', 'Vencimento', 'D/C', 'Liquidacao', 'Quantidade', 'Pu', 'ValorBruto', 'Imposto', 'ValorLiquido', 'ValorVinculado']

# Filtra as colunas do arquivo CSV
df_recentes = df_recentes[colunas]

# Remove a primeira linha
df_recentes = df_recentes.iloc[1:]

# Adiciona os dados à aba 'Base_Eventos_Virtual'
with pd.ExcelWriter(caminho_arquivo_conciliacao, engine='openpyxl', mode='a', if_sheet_exists='overlay') as writer:
    df_recentes.to_excel(writer, sheet_name='Base_Eventos_Virtual', startrow=len(df_conciliacao)+1, index=False, header=False)

print(f"Dados do arquivo {arquivo_csv} foram copiados para a aba 'Base_Eventos_Virtual'.")
