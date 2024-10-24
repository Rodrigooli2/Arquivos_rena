from playwright.sync_api import sync_playwright

def run(playwright):
    # Inicia o navegador Chrome em modo headless ou com interface
    browser = playwright.chromium.launch(headless=False)  
    page = browser.new_page()

    # Navega até a página de login
    page.goto("https://nome.cetip.net.br/menu/ctp/TelaPrincipalCetip21")

    # Define os valores para cada campo
    dominio = 'RENASCENCADTVM'
    login = 'RODRIG'
    senha = '@Rsouza3'

    # Preenche o campo de domínio (ID: e1)
    page.fill("#e1", dominio)

    # Preenche o campo de login (ID: e2)
    page.fill("#e2", login)

    # Preenche o campo de senha (ID: e3)
    page.fill("#e3", senha)

    # Ação adicional, como clicar em um botão de login
    page.click("button[type='submit']")  # Exemplo de clique em um botão de login

    # Espera até que a próxima página esteja completamente carregada
    page.wait_for_load_state('networkidle')

    # Outros passos de automação
    ...

    browser.close()

with sync_playwright() as playwright:
    run(playwright)
