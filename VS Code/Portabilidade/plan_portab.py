from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import datetime

# Configuração do Selenium para depuração remota
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

# Conecte-se ao navegador Chrome existente
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
wait = WebDriverWait(driver, 10)

# Função para fazer login
def login_google(email, senha):
    driver.get('https://accounts.google.com/')
    email_input = wait.until(EC.presence_of_element_located((By.ID, 'identifierId')))
    email_input.send_keys(email)
    email_input.send_keys(Keys.ENTER)

    password_input = wait.until(EC.presence_of_element_located((By.NAME, 'password')))
    time.sleep(2)  # Adicione um pequeno delay para evitar problemas de carregamento
    password_input.send_keys(senha)
    password_input.send_keys(Keys.ENTER)

    wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="gb"]/div[2]/div[3]/div[1]/div[2]/div/a/img')))

# Função para acessar a planilha
def acessar_planilha(url):
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[-1])
    driver.get(url)
    wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="docs-titlebar"]')))

# Função para encontrar e copiar linhas com a data de hoje na coluna M
def copiar_linhas_com_data_hoje():
    hoje = datetime.now().strftime("%d/%m/%Y")
    linhas_copiadas = []

    # Encontra todas as células na coluna M
    col_m_celulas = driver.find_elements(By.XPATH, '//div[@data-col="13"]')

    for celula in col_m_celulas:
        if celula.text == hoje:
            linha_num = celula.get_attribute('data-row')
            linha = driver.find_elements(By.XPATH, f'//div[@data-row="{linha_num}"]')
            linha_dados = [cel.text for cel in linha]
            linhas_copiadas.append(linha_dados)

    return linhas_copiadas

# Main
if __name__ == "__main__":
    email = 'rodrigo.oliveira@warrenbrasil.com.br'
    senha = 'sua_senha'
    planilha_url = 'https://docs.google.com/spreadsheets/d/1OGno1ApWC2OVGmUGrqsgj9x0phzZt5jdthQ0oEXfGsk/edit?gid=1329386731'

    # Realiza login no Google
    login_google(email, senha)

    # Acessa a planilha no Google Sheets
    acessar_planilha(planilha_url)

    # Aguarda alguns segundos para garantir que a planilha está totalmente carregada
    time.sleep(5)

    # Copia as linhas com a data de hoje na coluna M
    linhas_hoje = copiar_linhas_com_data_hoje()
    print("Linhas com a data de hoje:")
    for linha in linhas_hoje:
        print(linha)

    # Feche o navegador (opcional)
    # driver.quit()
