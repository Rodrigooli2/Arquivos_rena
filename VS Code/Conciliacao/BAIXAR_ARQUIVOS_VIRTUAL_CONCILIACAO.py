from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from time import sleep
import arrow
import inquirer
import pyautogui as bot
import pandas as pd
import openpyxl
from openpyxl.utils.dataframe import dataframe_to_rows
import os
from glob import glob

def encontrar_arquivo_recente(prefixo):
    # Procura pelos arquivos mais recentes que começam com o prefixo
    lista_arquivos = glob(f"{prefixo}*.csv")
    if not lista_arquivos:
        raise FileNotFoundError(f"Nenhum arquivo encontrado com o prefixo {prefixo}")
    arquivo_mais_recente = max(lista_arquivos, key=os.path.getctime)
    return arquivo_mais_recente

def processar_arquivos_excel():
    # Caminho do arquivo Excel de destino
    arquivo_excel = r"G:\Drives compartilhados\#Crossing - Diretoria COO\Distribuição Plataforma\Renda Fixa\RENDA FIXA - BACKOFFICE\CONCILIAÇÃO - Custódia\Conciliação RENDA FIXA.xlsm"
    
    # Encontra os arquivos CSV mais recentes
    arquivo_csv_rlatufinan = encontrar_arquivo_recente("RLATUFINAN")
    arquivo_csv_rlrelacaocli = encontrar_arquivo_recente("RLRELACAOCLI")
    
    # Carrega os arquivos CSV (pulando a primeira linha)
    df_rlatufinan = pd.read_csv(arquivo_csv_rlatufinan, skiprows=1)
    df_rlrelacaocli = pd.read_csv(arquivo_csv_rlrelacaocli, skiprows=1)

    # Abre o arquivo Excel e carrega as planilhas desejadas
    workbook = openpyxl.load_workbook(arquivo_excel, keep_vba=True)
    
    # Processando RLATUFINAN
    sheet_rlatufinan = workbook['Base_Eventos_Virtual']
    for r in dataframe_to_rows(df_rlatufinan, index=False, header=False):
        sheet_rlatufinan.append(r)

    # Processando RLRELACAOCLI
    sheet_rlrelacaocli = workbook['Base_Operacoes_Virtual']
    for r in dataframe_to_rows(df_rlrelacaocli, index=False, header=False):
        sheet_rlrelacaocli.append(r)
    
    # Salva as alterações no arquivo Excel
    workbook.save(arquivo_excel)

    print("Os dados foram inseridos com sucesso nas planilhas.")

class LoginVirtual:
    def __init__(self, login, senha):
        self.login = login
        self.senha = senha
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)
        
    def fazer_login(self, url):
        try:
            self.driver.get(url)
            login_input = self.wait.until(EC.presence_of_element_located((By.NAME, 'txtUsuario')))
            senha_input = self.driver.find_element(By.NAME, 'txtSenha')

            login_input.send_keys(self.login)
            senha_input.send_keys(self.senha)
            senha_input.send_keys(Keys.ENTER)

            # Aguarda a próxima página carregar
            self.wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/form/nav/div/div[2]/ul[1]/li[5]/a')))
            for _ in range(3):
                bot.hotkey('ctrl', '-')  

        except TimeoutException:
            print("O login não foi realizado no tempo esperado.")
        except Exception as e:
            print(f"Elementos não encontrados na página: {e}")

class ConsultaVirtual:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def botoes_virtual(self, botao, botao_fullxpath):
        try:
            botao_elemento = self.wait.until(EC.presence_of_element_located((By.XPATH, botao_fullxpath)))
            botao_elemento.click()
            print(f"Botão {botao} encontrado e clicado.")
        except TimeoutException:
            print(f"Botão {botao} não encontrado no tempo esperado.")
        except Exception as e:
            print(f"Erro ao interagir com o botão {botao}: {e}")

    def enviar_dados(self, botao, botao_fullxpath, dados):
        try:
            campo = self.wait.until(EC.presence_of_element_located((By.XPATH, botao_fullxpath)))
            campo.click()
            campo.send_keys(Keys.CONTROL + 'a')  # Selecionar tudo
            sleep(3)
            campo.send_keys(dados)
            print(f"Dados enviados para o campo {botao}.")
        except TimeoutException:
            print(f"Campo {botao} não encontrado no tempo esperado.")
        except Exception as e:
            print(f"Erro ao enviar dados para o campo {botao}: {e}")

def main(dominio):
    if dominio == 'WARRENCOR':
        login = 'rodrigo.souza'
        senha = 'finan@Vivo13'
        url = 'http://virtual.broker.warren.com.br/Virtual/Open/Vir_opn/PrcOperacao.aspx'

    elif dominio == 'RENASCENCADTVM':
        login = 'rodrigo.souza'
        senha = 'finan@Vivo13'
        url = 'https://virtual.rena.warren.com.br/Virtual/Open/Vir_Opn/'

    login_virtual = LoginVirtual(login, senha)
    login_virtual.fazer_login(url)
    consulta_virtual = ConsultaVirtual(login_virtual.driver)

    # Caminho Relações de Operações (RLRELACAO)
    botoes_xpaths = [
        ('relatorio', '/html/body/form/nav/div/div[2]/ul[1]/li[6]/a'),
        ('financeiro', '/html/body/form/nav/div/div[2]/ul[1]/li[6]/ul/li[3]/a'),
        ('relac_operacao', '/html/body/form/nav/div/div[2]/ul[1]/li[6]/ul/li[3]/ul/li[6]/a'),
        ('relac_operacao_periodo', '/html/body/form/nav/div/div[2]/ul[1]/li[6]/ul/li[3]/ul/li[6]/ul/li[6]/a'),
        ('relac_operacao_data', '/html/body/form/nav/div/div[2]/ul[1]/li[6]/ul/li[3]/ul/li[6]/ul/li[6]/ul/li[1]/a')
    ]

    for botao, xpath_botao in botoes_xpaths:
        consulta_virtual.botoes_virtual(botao, xpath_botao)
        sleep(3)  # Espera 3 segundos entre cada interação

    botao = 'de'
    xpath_botao = '/html/body/form/div[3]/div/div[1]/table[1]/tbody/tr[1]/td[2]/input[1]'
    dados = '29/07/2024'
    consulta_virtual.enviar_dados(botao, xpath_botao, dados)
    sleep(3)

    botao = 'até'
    xpath_botao = '/html/body/form/div[3]/div/div[1]/table[1]/tbody/tr[1]/td[4]/input[1]'
    dados = '29/07/2024'
    consulta_virtual.enviar_dados(botao, xpath_botao, dados)
    sleep(3)

    # Baixando o arquivo csv RLRELACAO
    botao = 'csv'
    xpath_botao = '/html/body/form/div[3]/div/div[1]/table[2]/tbody/tr/td[2]/a'
    consulta_virtual.botoes_virtual(botao, xpath_botao)
    sleep(3)


    # Caminho Fluxo Financeiro (RLATUFINAN)
    botoes_xpaths = [
        ('relatorio', '/html/body/form/nav/div/div[2]/ul[1]/li[6]/a'),
        ('financeiro', '/html/body/form/nav/div/div[2]/ul[1]/li[6]/ul/li[3]/a'),
        ('fluxo_finan', '/html/body/form/nav/div/div[2]/ul[1]/li[6]/ul/li[3]/ul/li[8]/a'),
        ('fluxo_finan_data', '/html/body/form/nav/div/div[2]/ul[1]/li[6]/ul/li[3]/ul/li[8]/ul/li[1]/a'),
    ]

    for botao, xpath_botao in botoes_xpaths:
        consulta_virtual.botoes_virtual(botao, xpath_botao)
        sleep(3)  # Espera 3 segundos entre cada interação

    botao = 'data'
    xpath_botao = '/html/body/form/div[3]/div/div[1]/table[1]/tbody/tr[1]/td[2]/input[1]'
    dados = '29/07/2024'
    consulta_virtual.enviar_dados(botao, xpath_botao, dados)
    sleep(3)

    # Baixando o arquivo csv RLATUFINAN
    botao = 'csv'
    xpath_botao = '/html/body/form/div[3]/div/div[1]/table[2]/tbody/tr/td[2]/a'
    consulta_virtual.botoes_virtual(botao, xpath_botao)
    sleep(3)

    input("Pressione Enter para fechar o navegador...")

if __name__ == "__main__":
    questions = [
        inquirer.List(
            'dominio',
            message="Escolha o domínio",
            choices=['WARRENCOR', 'RENASCENCADTVM']
        ),
    ]
    answers = inquirer.prompt(questions)
    dominio = answers['dominio']
    main(dominio)
