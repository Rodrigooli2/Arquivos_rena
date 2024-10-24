import pyautogui as bot
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import inquirer

class LoginCetip:
    def __init__(self, dominio, login, senha):
        self.dominio = dominio.upper()
        self.login = login.upper()
        self.senha = senha
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)
        
    def fazer_login(self, url):
        try:
            self.driver.get(url)
            
            # Espera o campo de domínio estar presente
            dominio_input = self.wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/form/table/tbody/tr/td/div[2]/table/tbody/tr[2]/td[3]/input')))

            # Tenta localizar os elementos usando diferentes métodos
            login_input = self.wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/form/table/tbody/tr/td/div[2]/table/tbody/tr[3]/td[3]/input')))
            senha_input = self.driver.find_element(By.XPATH, '/html/body/form/table/tbody/tr/td/div[2]/table/tbody/tr[4]/td[3]/input')

            # Preenche os campos e faz o login
            dominio_input.send_keys(self.dominio)
            login_input.send_keys(self.login)
            senha_input.send_keys(self.senha)
            senha_input.send_keys(Keys.ENTER)

            # Aguarda a próxima página carregar
            self.wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/table/tbody/tr[2]/td/table/tbody/tr[1]/td[2]/a/img')))
            
            # Salva screenshot para verificação visual
            self.driver.save_screenshot('after_login_selenium.png')
            
            # Retorna o driver para operações adicionais
            return self.driver
        except TimeoutException:
            print("O login não foi realizado no tempo esperado.")
        except NoSuchElementException:
            print("Elementos não foram encontrados na página.")
        except Exception as e:
            print(f"Erro inesperado: {e}")

        # Tentativa de usar PyAutoGUI se o Selenium falhar
        self.usar_pyautogui_para_login()

    def usar_pyautogui_para_login(self):
        print("Tentando usar PyAutoGUI para login...")
        time.sleep(2)  # Ajuste o tempo de espera conforme necessário

        # Clica na coordenada x=893, y=315 e começa a inserir as informações
        bot.click(893, 315)  # Clica na coordenada especificada
        bot.press('tab')
        bot.typewrite(self.dominio)
        print("Inserindo domínio")
        time.sleep(1)
        bot.press('tab')  # Navega para o campo de login
        bot.typewrite(self.login)
        print("Inserindo login")
        bot.press('tab')  # Navega para o campo de senha
        time.sleep(1)
        bot.typewrite(self.senha)
        print("Inserindo senha")
        time.sleep(3)
        bot.press('enter')

        # Aguarda e tira um screenshot para verificação
        time.sleep(10)
        bot.press('enter')
            
        # Salva screenshot para verificação visual
        self.driver.save_screenshot('after_login_pyautogui.png')
    

class ConsultaCetip:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def botoes_clicar(self, botao, botao_fullxpath):
        try:
            botao_elemento = self.wait.until(EC.presence_of_element_located((By.XPATH, botao_fullxpath)))
            botao_elemento.click()
            print(f"Botão {botao} encontrado e clicado.")
        except TimeoutException:
            print(f"Botão {botao} não encontrado no tempo esperado.")
            raise
        except Exception as e:
            print(f"Erro ao interagir com o botão {botao}: {e}")
            raise
        time.sleep(3)

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
    url = 'https://nome.cetip.net.br/menu/ctp/TelaPrincipalCetip21'
    if dominio == 'WARRENCOR':
        login = 'RSOUZA'
        senha = '@Rsouza2'

    elif dominio == 'RENASCENCADTVM':
        login = 'RODRIG'
        senha = '@Rsouza3'

    login_cetip = LoginCetip(dominio, login, senha)    
    login_cetip.fazer_login(url)
    consulta_cetip = ConsultaCetip(login_cetip.driver)

    botao = 'inicio'
    xpath_botao = '/html/body/table/tbody/tr[2]/td/table/tbody/tr[1]/td[2]/a/img'
    consulta_cetip.botoes_clicar(botao, xpath_botao)

    botao = 'operacao'
    xpath_botao = '/html/body/div[2]/div/ul[2]/li[6]/a/span[1]'
    consulta_cetip.botoes_clicar(botao, xpath_botao)

    botao = 'consulta'
    xpath_botao = '/html/body/div[2]/div/ul[2]/li[6]/ul/li[1]/a/span[2]'
    consulta_cetip.botoes_clicar(botao, xpath_botao)

    botao = 'operacao_(nome)'
    xpath_botao = '/html/body/div[2]/div/ul[2]/li[6]/ul/li[1]/ul/li[1]/a'
    consulta_cetip.botoes_clicar(botao, xpath_botao)

    bot.hotkey('ctrl', '+')
    bot.scroll(-500)
    time.sleep(3)

    # Tentativa de clicar no botão 'pesquisar_dia'
    botao = 'pesquisar_dia'
    xpath_botao = '/html/body/table/tbody/tr/td/div/table/tbody/tr[3]/td/form/table[2]/tbody/tr/td[2]/span[1]/input'
    try:
        consulta_cetip.botoes_clicar(botao, xpath_botao)
    except TimeoutException:
        print(f"Botão {botao} não encontrado no tempo esperado. Tentando o botão alternativo...")
        
        # Tentativa de clicar no botão alternativo 'mudar_dia'
        botao = 'mudar_dia'
        xpath_botao = '/html/body/table/tbody/tr/td/div/table/tbody/tr[3]/td/form/table[1]/tbody/tr[16]/td[2]/input[1]'
        try:
            consulta_cetip.botoes_clicar(botao, xpath_botao)
            bot.press('enter')
            print("Enter pressionado com PyAutoGUI.")
        except TimeoutException:
            print("Botão alternativo também não encontrado no tempo esperado.")
        except Exception as e:
            print(f"Erro ao tentar clicar no botão alternativo: {e}")

    botao = 'carregando_pesquisa'
    xpath_elemento = '/html/body/table/tbody/tr[2]/td/table/tbody/tr[1]/td[3]/img'
    self.wait.until(EC.invisibility_of_element_located((By.XPATH, xpath_elemento)))
    
    botao = 'baixar'
    xpath_elemento = '/html/body/div/table/tbody/tr[7]/td/form/table/tbody/tr/td[1]/input'
    carregou = self.wait.until(EC.presence_of_element_located((By.XPATH, xpath_elemento)))

    if carregou:
        botao = 'baixar_arquivo' 
        xpath_botao = '/html/body/div/table/tbody/tr[7]/td/form/table/tbody/tr/td[1]/input'
        consulta_cetip.botoes_clicar(botao, xpath_botao)
    else:
        print("Erro de carregamento, favor verificar.")

    input("Pressione Enter para fechar o navegador...")
    login_cetip.driver.quit()
    
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
