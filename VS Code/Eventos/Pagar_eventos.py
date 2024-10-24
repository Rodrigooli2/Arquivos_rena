from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from time import sleep

class LoginVirtual:
    def __init__(self, login, senha):
        self.login = login
        self.senha = senha
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)
        
    def fazer_login(self):
        try:
            self.driver.get('http://virtual.broker.warren.com.br/Virtual/Open/Vir_opn/PrcOperacao.aspx')
            login_input = self.wait.until(EC.presence_of_element_located((By.NAME, 'txtUsuario')))
            senha_input = self.driver.find_element(By.NAME, 'txtSenha')

            login_input.send_keys(self.login)
            senha_input.send_keys(self.senha)
            senha_input.send_keys(Keys.ENTER)

            # Aguarda a próxima página carregar
            self.wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/form/nav/div/div[2]/ul[1]/li[5]/a')))
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
            ## Aguarda encontrar a presença do elemento, ele usa o codigo do elemento na pagina para localizar ele. No caso foi o FULL XPATH
            botao = self.wait.until(EC.presence_of_element_located((By.XPATH, botao_fullxpath)))
            if botao:
                botao.click()
                print(f"Botão {botao} encontrado.")
            else:
                print(f"Botão {botao} não encontrado.")

        except Exception as e:
            print(f"Elemento não encontrado na página: {e}")

def main():
    login = 'rodrigo.souza'
    senha = 'finan@Vivo13'

    # Botões dentro da página da virtual
    controle = 'controle'
    xpath_controle = '/html/body/form/nav/div/div[2]/ul[1]/li[5]/a'
    financeiro = 'financeiro'
    xpath_financeiro = '/html/body/form/nav/div/div[2]/ul[1]/li[5]/ul/li[3]/a'
    atualizacao = 'atualizacao'
    xpath_atualizacao = '/html/body/form/nav/div/div[2]/ul[1]/li[5]/ul/li[3]/ul/li[1]/a'
    #inicio = 'inicio'
    #xpath_inicio = '/html/body/form/nav/div/div[1]/div[1]/div[1]/a/img'

    # Criando instância para a classe Login
    login_virtual = LoginVirtual(login, senha)
    login_virtual.fazer_login()
    
    # Criando instância para a classe ConsultaVirtual
    consulta_virtual = ConsultaVirtual(login_virtual.driver)
    ## CAMINHO PARA EVENTOS DENTRO DA VIRTUAL
    consulta_virtual.botoes_virtual(controle, xpath_controle)
    consulta_virtual.botoes_virtual(financeiro, xpath_financeiro)
    consulta_virtual.botoes_virtual(atualizacao, xpath_atualizacao)

    ## BOTAO PARA VOLTAR AO INICIO DA VIRTUAL
    ##consulta_virtual.botoes_virtual(inicio, xpath_inicio)


    # Mantém o navegador aberto após a consulta
    input("Pressione Enter para fechar o navegador...")

if __name__ == '__main__':
    main()
