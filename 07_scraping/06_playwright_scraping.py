from playwright.sync_api import sync_playwright

url = "https://midu.dev"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False) #, slow_mo=1000)
    page = browser.new_page()
    page.goto(url)

    first_article_anchor = page.locator('article a').first
    print(first_article_anchor.text_content())
    first_article_anchor.click()

    page.wait_for_load_state()

    # first_image = page.locator('img').first
    # image_src = first_image.get_attribute('src')
    # print(f"La imagen del primer curso es: {image_src}")

    # Usando xpath
    first_image = page.locator("xpath=/html/body/div[1]/div/div[1]/img")
    print(first_image.get_attribute("src"))

    # NO ME HA FUNCIONADO ESTA PARTE
    # curso_content_container = page.locator('text=" Contenido del curso "')
    # curso_content_sibling = curso_content_container.locator("xpath=/html/body/div[1]/div/div[3]/div[3]/h2")
    # print(curso_content_sibling.get_attribute("class"))


    browser.close()
