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

def main():
    login = 'rodrigo.souza'
    senha = 'finan@Vivo13'
    url = 'https://virtual.rena.warren.com.br/Virtual/Open/Vir_Opn/'

    login_virtual = LoginVirtual(login, senha)
    login_virtual.fazer_login(url)
    consulta_virtual = ConsultaVirtual(login_virtual.driver)
    botao = 'inicio'
    xpath_botao = '/html/body/form/nav/div/div[1]/div[1]/div[1]/a/img'
    consulta_virtual.botoes_virtual(botao, xpath_botao)

    input("Pressione Enter para fechar o navegador...")
    
if __name__ == "__main__":
    main()