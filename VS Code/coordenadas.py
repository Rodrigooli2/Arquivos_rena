import pyautogui
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginCetip:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)
        
    def capturar_coordenadas(self, url):
        self.driver.get(url)

        print("Navegador carregado. Mova o cursor para o ponto desejado e aguarde 5 segundos...")
        time.sleep(5)

        # Captura as coordenadas do cursor
        x, y = pyautogui.position()
        print(f"As coordenadas do ponto são: x={x}, y={y}")

        print("A página continuará aberta. Feche manualmente quando terminar.")

def main():
    url = "https://nome.cetip.net.br/menu/ctp/TelaPrincipalCetip21"
    login_cetip = LoginCetip()
    login_cetip.capturar_coordenadas(url)

if __name__ == "__main__":
    main()
