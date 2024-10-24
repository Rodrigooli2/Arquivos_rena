import pandas as pd
import tkinter as tk
from tkinter import filedialog
import os
from datetime import datetime

# Obtém o caminho da pasta de Downloads do usuário
downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")

# Abre uma janela para selecionar o arquivo
root = tk.Tk()
root.withdraw()  # Oculta a janela principal
file_path = filedialog.askopenfilename(
    filetypes=[("All files", "*.*")],
    title="Selecione o arquivo"
)

# Verifica se um arquivo foi selecionado
if file_path:
    # Obtém o horário e a data de modificação do arquivo selecionado
    file_mod_time = os.path.getmtime(file_path)
    file_date = datetime.fromtimestamp(file_mod_time).strftime('%d-%m-%Y')
    file_time = datetime.fromtimestamp(file_mod_time).strftime('%HhT%Mmin')

    # Cria o nome do arquivo no formato desejado
    file_name = f"Operacao_{file_date}_{file_time}.xlsx"

    # Tenta ler o arquivo como um DataFrame, separando por TAB
    try:
        df = pd.read_csv(file_path, encoding='ISO-8859-1', delimiter=None, engine='python')
        
        # Define o caminho completo para salvar o arquivo Excel na pasta de Downloads
        save_path = os.path.join(downloads_folder, file_name)

        # Salva o DataFrame no formato Excel
        df.to_excel(save_path, index=False)
        print(f"Arquivo salvo como {save_path}")
    
    except UnicodeDecodeError as e:
        print(f"Erro ao ler o arquivo: {e}")
else:
    print("Nenhum arquivo foi selecionado.")
