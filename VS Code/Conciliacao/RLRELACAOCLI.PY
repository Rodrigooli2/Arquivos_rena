import pandas as pd

# Caminho do arquivo CSV
arquivo_csv = r'C:\Users\rodrigo.oliveira_war\Downloads\RLRELACAOCLI - 2024-07-31T193225.022.CSV'

# Abra o arquivo CSV usando pandas
df_recentes = pd.read_csv(arquivo_csv, sep=';')

# Imprima as colunas do arquivo CSV
print("Colunas do arquivo CSV:")
print(df_recentes.columns.tolist())

# Carregar o arquivo de conciliação
sheet='Base_Operacoes_Virtual'
caminho_arquivo_conciliacao = r'G:\Drives compartilhados\#Crossing - Diretoria COO\Distribuição Plataforma\Renda Fixa\RENDA FIXA - BACKOFFICE\CONCILIAÇÃO - Custódia\Conciliação - Renda Fixa\Conciliacao.xlsx'
df_conciliacao = pd.read_excel(caminho_arquivo_conciliacao, sheet_name=sheet)

# Remover todas as linhas, exceto a primeira (cabeçalhos)
df_empty = pd.DataFrame(columns=df_conciliacao.columns)

# Crie uma lista com as colunas desejadas
#colunas = [
#    'Data', 'Boleta', 'Operacao', 'Matricula', 'Cliente', 'Titulo', 'Emissao', 'Vencimento', 'Qtde', 'Pu Oper', 'Valor Oper', 
#    'IOF', 'IR', 'Valor Liquido', 'Tx Comp', 'PU Comp', 'Valor Comp', 'Liquidacao', 'PU Fechamento', 'Mercado', 'Comando', 
#    'OBS', 'Cod Gerente', 'Nome Gerente', 'Remuneração Cliente', 'Remuneração Papel', 'Emissor', 'Cetip/Selic', 'CPF/CNPJ Cliente', 
#    'Chave Assoc', 'Broker', 'Data Aplicacao', 'PU Aplicação', 'Posição', 'Data Liquidação', 'Operador', 'Tx Corretagem', 
#    'Corretagem', 'Categoria', 'Grupo', 'Nome Operador'
#]

# Filtra as colunas do arquivo CSV
#df_recentes = df_recentes[colunas]
# Combine os DataFrames vazio e os novos dados
df_combined = pd.concat([df_empty, df_recentes])

# Adiciona os dados à aba 'Base_Operacoes_Virtual'
with pd.ExcelWriter(caminho_arquivo_conciliacao, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
    df_combined.to_excel(writer, sheet_name=sheet, index=False)
    
print(f"Dados do arquivo {arquivo_csv} foram copiados para a aba {sheet}.")
