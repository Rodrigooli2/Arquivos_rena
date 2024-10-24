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


class LoginCetip:
    def __init__(self, Dominio, login, senha):
        self.dominio = Dominio
        self.login = login
        self.senha = senha
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)
        
    def fazer_login(self, url):
        try:
            self.driver.get(url)
            dominio_input = self.wait.until(EC.presence_of_element_located((By.NAME, 'Entrada')))
            bot.hotkey('ctrl', '-')  

            login_input = self.driver.find_element(By.XPATH, '/html/body/form/table/tbody/tr/td/div[2]/table/tbody/tr[3]/td[3]/input')
            senha_input = self.driver.find_element(By.XPATH, '/html/body/form/table/tbody/tr/td/div[2]/table/tbody/tr[4]/td[3]/input')

            dominio_input.send_keys(self.dominio)
            login_input.send_keys(self.login)
            senha_input.send_keys(self.senha)
            senha_input.send_keys(Keys.ENTER)

            # Aguarda a próxima página carregar
            self.wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/form/nav/div/div[2]/ul[1]/li[5]/a')))
            
            # Retorna o driver para operações adicionais
            return self.driver
        except TimeoutException:
            print("O login não foi realizado no tempo esperado.")
        except Exception as e:
            print(f"Elementos não encontrados na página: {e}")

def main(dominio):
    url = 'https://nome.cetip.net.br/menu/ctp/TelaPrincipalCetip21'
    if dominio == 'WARRENCOR':
        login = 'rodrigo.souza'
        senha = 'finan@Vivo13'

    elif dominio == 'RENASCENCADTVM':
        login = 'rodrigo.souza'
        senha = 'finan@Vivo13'

    login_cetip = LoginCetip(dominio, login, senha)
    login_cetip.fazer_login(url)

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