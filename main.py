
from os import link, system
import time
from playwright.sync_api import Playwright, sync_playwright, expect
from bs4 import BeautifulSoup

#url = 'https://www.cartuseria.ro/sisteme-ciss-alimentare-continua/'
url = system.argv[1]

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to Cartuseria
    page.goto(url, wait_until="networkidle")
    
    html = page.inner_html("#content-wrapper")
    
    soup = BeautifulSoup(html, "html.parser")
    
    #Data Extraction Begins
    
    #Check if FAQ exist
    if soup.find("div", {"id": "c-faq-accord"}):
        faq_exists = True
    else:
        faq_exists = False    
    
    #print(f'FAQ exists: {faq_exists}')

    #Check if Description Exists and how many internal links
    description_html = soup.find("div", {"id": "category-description"})

    if description_html:
        #extract description text
        category_exists = True
        links = description_html.findAll('a')
    else:
        category_exists = False
    
    #print(f'Category exists: {category_exists}')
    #print(f'Internal Links: {len(links)}')


    
    #Exract number of products
    number_of_product_html = soup.find("div", {"class": "col-md-4"})
    if number_of_product_html:
        product_count = number_of_product_html.get_text().strip()
        #Stip all but total number of produtcts
        product_count = product_count.split('din ')[1].split(' produs')[0]
    else:
        product_count = 0
    #print (f'Number of products: {product_count}')


    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)


