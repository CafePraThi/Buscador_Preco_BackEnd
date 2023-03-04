import psycopg2
from datetime import datetime, timezone
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
#from selenium.webdriver.common.options import Options
from selenium.common.exceptions import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support import expected_conditions as ec
from time import sleep

connection = psycopg2.connect(
    database='railway',
    user='postgres',
    password='C5aoBl40CU5DEH0xIfmk',
    host='containers-us-west-75.railway.app',
    port='7312'
)
    
sql = connection.cursor()


def new_product(sql, connection, name, price, site, quote_date, link_img):
    query = "SELECT * FROM app_buscapreco_produto WHERE name=%s and price=%s and site=%s"
    values = (name, price, site)
    result = sql.execute(query, values)
    dados = sql.fetchall()

    if len(dados) == 0:
        query = "INSERT INTO app_buscapreco_produto(name, price, site, quote_date, link_img) VALUES(%s, %s, %s, %s, %s)"
        values = (name, price, site, quote_date, link_img)
        sql.execute(query, values)
    else:
        print("Dados ja cadastrados anteriormente")

new_product(sql, connection, 'Corsarebaixado', 10000, 'Amazon.com/corsa', datetime.now(), 'https://source.unsplash.com/random/150x150' )
connection.commit()