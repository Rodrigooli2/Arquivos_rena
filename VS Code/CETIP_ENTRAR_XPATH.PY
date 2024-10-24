from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import inquirer

class LoginCetip:
    def __init__(self, Dominio, login, senha):
        self.dominio = Dominio
        self.login = login
        self.senha = senha
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)

    def get_element_xpath(self, element):
        # Função para gerar um XPath básico para um elemento
        try:
            return self.driver.execute_script(
                "function getElementXPath(element) {"
                "   var path = '';"
                "   for (; element && element.nodeType == Node.ELEMENT_NODE; element = element.nodeParentNode) {"
                "       var index = 0;"
                "       var sibling = element.previousSibling;"
                "       while (sibling) {"
                "           if (sibling.nodeType == Node.ELEMENT_NODE && sibling.nodeName == element.nodeName) {"
                "               index++;"
                "           }"
                "           sibling = sibling.previousSibling;"
                "       }"
                "       path = '/' + element.nodeName.toLowerCase() + (index ? '[' + (index + 1) + ']' : '') + path;"
                "   }"
                "   return path || '/';"
                "}"
                "return getElementXPath(arguments[0]);", element)
            
        except Exception as e:
            return str(e)

    def fazer_login(self, url):
        try:
            self.driver.get(url)
            
            # Espera até que a página esteja carregada
            self.wait.until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
            print("Página carregada")

            # Tenta encontrar e listar todos os elementos com diferentes atributos
            print("Listando elementos por 'id':")
            elements_by_id = self.driver.find_elements(By.XPATH, '//*[@id]')
            for element in elements_by_id:
                xpath = self.get_element_xpath(element)
                print(f"Elemento ID: {element.get_attribute('id')} - XPath: {xpath}")

            print("Listando elementos por 'class':")
            elements_by_class = self.driver.find_elements(By.XPATH, '//*[@class]')
            for element in elements_by_class:
                xpath = self.get_element_xpath(element)
                print(f"Elemento Class: {element.get_attribute('class')} - XPath: {xpath}")

            # Exemplo de tentar encontrar o elemento com 'name' se ele estiver presente
            try:
                dominio_input = self.driver.find_element(By.NAME, 'Entrada')
                login_input = self.driver.find_element(By.NAME, 'login')
                senha_input = self.driver.find_element(By.NAME, 'senha')

                dominio_input.send_keys(self.dominio)
                login_input.send_keys(self.login)
                senha_input.send_keys(self.senha)
                senha_input.send_keys(Keys.ENTER)

                # Aguarda a próxima página carregar
                self.wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/form/nav/div/div[2]/ul[1]/li[5]/a')))
                
                return self.driver
            except NoSuchElementException:
                print("Não foi possível encontrar os campos de entrada.")

        except TimeoutException:
            print("O login não foi realizado no tempo esperado.")
        except Exception as e:
            print(f"Ocorreu um erro: {e}")

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
