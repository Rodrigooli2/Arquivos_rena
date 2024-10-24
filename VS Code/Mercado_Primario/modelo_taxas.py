import os
import pandas as pd

# Define o caminho da pasta
pasta = r"C:\Users\rodrigo.oliveira_war\Documents\OUTLOOK - MACRO\21-08-2024\"

# Define a ordem correta das colunas
ordem_colunas = [
    "Data Envio", "Emissor", "Ativo", "Vencimento (dc)", 
    "Data Vencimento", "Carência (dc)", "Data Carência", 
    "Indexador", "TAXA", "Spread mínimo", "PU Emissão", 
    "Estoque por vertice", "Volume mínimo", "Validade"
]

# Lista todos os arquivos na pasta
arquivos = [f for f in os.listdir(pasta) if os.path.isfile(os.path.join(pasta, f))]

# Processa cada arquivo
for arquivo in arquivos:
    caminho_completo = os.path.join(pasta, arquivo)
    
    # Lê o arquivo em um DataFrame
    df = pd.read_excel(caminho_completo)
    
    # Reordena as colunas conforme a ordem especificada
    df = df[ordem_colunas]
    
    # Salva o DataFrame com a nova ordem de colunas
    df.to_excel(caminho_completo, index=False)
    
    print(f"Arquivo {arquivo} processado com sucesso.")
