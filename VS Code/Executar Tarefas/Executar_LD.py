import schedule
import time
import os

def tarefa_diaria():
    print("Executando tarefa diária...")
    # Chama o script Insere_arquivos_cetip.py
    #os.system(r'python C:\Users\rodrigo.oliveira_war\Desktop\VS Code\Resgate LD\Insere_arquivos_cetip.py')
    os.system('python teste_nota.py')

# Agendar a tarefa para às 9:00 da manhã em todos os dias úteis
#schedule.every().monday.at("09:00").do(tarefa_diaria)
#schedule.every().tuesday.at("09:00").do(tarefa_diaria)
#schedule.every().wednesday.at("09:00").do(tarefa_diaria)
#schedule.every().thursday.at("09:00").do(tarefa_diaria)
schedule.every().thursday.at("11:32").do(tarefa_diaria)
schedule.every().thursday.at("11:36").do(tarefa_diaria)
schedule.every().thursday.at("11:40").do(tarefa_diaria)
schedule.every().friday.at("09:00").do(tarefa_diaria)

while True:
    schedule.run_pending()
    time.sleep(10)  # Aguarda um minuto antes de verificar novamente
