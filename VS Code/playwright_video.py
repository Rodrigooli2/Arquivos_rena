from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    navegador = p.chromium.launch(headless=False)
    pagina = navegador.new_page()
    pagina.goto("https://nome.cetip.net.br/menu/ctp/TelaPrincipalCetip21")
    pagina.locator('xpath=//*[@id="e1"]').click()
