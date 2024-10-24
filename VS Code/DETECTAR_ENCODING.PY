import chardet

# Abre o arquivo em modo binário para detectar o encoding
with open(rf"G:\Drives compartilhados\#Crossing - Diretoria COO\Distribuição Plataforma\Renda Fixa\RENDA FIXA - BACKOFFICE\CONCILIAÇÃO - Custódia\08 AGOSTO_2024\08\CETIP21_240808_DCUSTODIAPART-CDB.txt", 'rb') as file:
    raw_data = file.read()
    result = chardet.detect(raw_data)
    encoding = result['encoding']

print(f"O encoding detectado é: {encoding}")
