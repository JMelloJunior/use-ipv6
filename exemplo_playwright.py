# from playwright.sync_api import sync_playwright

# with sync_playwright() as p:
#     navegador = p.firefox.launch(headless=False)  # Abre o Firefox com interface
#     pagina = navegador.new_page()
#     pagina.goto('https://www.google.com')
#     print(pagina.title())
#     pagina.wait_for_timeout(3000)  # Aguarda 3 segundos
#     navegador.close()

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    navegador = p.firefox.launch(headless=False)
    pagina = navegador.new_page()
    pagina.goto('https://duckduckgo.com')
    pagina.wait_for_selector('input[name="q"]', timeout=5000)
    pagina.fill('input[name="q"]', 'Playwright Python')
    pagina.keyboard.press('Enter')
    pagina.wait_for_timeout(5000)
    navegador.close()