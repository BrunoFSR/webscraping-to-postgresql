from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from bs4 import BeautifulSoup
import requests
import pandas as pd

import psycopg2
from sqlalchemy import create_engine

def geet_book_info(url):
    # url = "http://books.toscrape.com/catalogue/tipping-the-velvet_999/index.html"
    html_data = requests.get(url).text
    
    soup = BeautifulSoup(html_data, "html.parser")
    
    # livro = pd.DataFrame(columns = ["Nome", "Categoria", "Estrelas", "Preço", "Possui Estoque"])
    
    nome = soup.find('h1').text
    categoria = soup.find_all('li')[2].find('a').text

    # star-rating
    div = soup.find('div', attrs={'class':'col-sm-6 product_main'})

    estrelas = 0
    if (div.find('p', attrs={'class':'star-rating One'})):
        estrelas = 1
    elif (div.find('p', attrs={'class':'star-rating Two'})):
        estrelas = 2
    elif (div.find('p', attrs={'class':'star-rating Three'})):
        estrelas = 3
    elif (div.find('p', attrs={'class':'star-rating Four'})):
        estrelas = 4
    elif (div.find('p', attrs={'class':'star-rating Five'})):
        estrelas = 5

    preco = soup.find('p', attrs={'class':'price_color'}).text[1:]
    estoque = soup.find('table').find_all('tr')[5].find('td').text
    
    return {"Nome": nome,
         "Categoria": categoria,
         "Estrelas": estrelas,
         "Preço": preco,
         "Possui Estoque": estoque}

def test_run_webscraping(selenium):
    #selenium = webdriver.Chrome('./chromedriver')
    selenium.get('http://books.toscrape.com/index.html')

    total_de_paginas = selenium.find_element(By.XPATH, "/html/body/div/div/div/div/section/div[2]/div/ul/li[1]")
    total_de_paginas = total_de_paginas.text.split(" ")[3]
    page_count = 1

    list = selenium.find_elements(By.XPATH, "/html/body/div/div/div/div/section/div[2]/ol/li")

    livro = pd.DataFrame(columns = ["Nome", "Categoria", "Estrelas", "Preço", "Possui Estoque"])

    while page_count <= int(total_de_paginas):
        books_count=1
        while books_count <= len(list):

            xpath_books = "/html/body/div/div/div/div/section/div[2]/ol/li[" + str(books_count) + "]/article/h3/a"

            try:
                selenium.find_element(By.XPATH, xpath_books).click()
                
                ### Código de coleta das informações dos livros
                book_info = geet_book_info(selenium.current_url)
                livro = livro.append(book_info, ignore_index = True)
                
                selenium.back()
            except Exception as e:
                print('Erro no click(): '+ str(e))

            books_count = books_count + 1

        if int(page_count) != int(total_de_paginas):
            selenium.find_element(By.LINK_TEXT, "next").click()
        
        page_count = page_count + 1
                
    selenium.close()

    #livro.to_csv("livros.csv", ";", index=False)

    engine = create_engine('postgresql://postgres:postgres@localhost:5432/postgres')
    livro.to_sql('bookinfo', engine, if_exists='replace', index=False)