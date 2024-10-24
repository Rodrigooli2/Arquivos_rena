import win32com.client as win32
import time

# Caminho do arquivo Excel
caminho_arquivo = r"G:\Drives compartilhados\#Crossing - Diretoria COO\Distribuição Plataforma\Renda Fixa\RENDA FIXA - BACKOFFICE\CONCILIAÇÃO - Custódia\Conciliação RENDA FIXA.xlsm"

# Inicializar o Excel
excel = win32.Dispatch('Excel.Application')

# Abrir o arquivo Excel
workbook = excel.Workbooks.Open(caminho_arquivo)

# Esperar alguns segundos para garantir que o arquivo foi carregado (opcional)
time.sleep(5)

# Executar a macro "Base_eventos_virtual"
excel.Application.Run("Base_eventos_virtual")

# Manter o Excel aberto para que você possa verificar os resultados
# workbook.Save() # (Opcional) Salvar o arquivo se for necessário
# workbook.Close() # (Opcional) Fechar o arquivo depois de salvar

# Fechar o Excel (opcional)
# excel.Quit()
