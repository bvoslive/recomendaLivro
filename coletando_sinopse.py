#--------------------------------------------#
#           Importando bibliotecas           #
#--------------------------------------------#

import pandas as pd
import requests
import re
import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#--------------------------------------------#
#               Data Cleaning                #
#--------------------------------------------#

#IMPORT DATASET
df = pd.read_csv('Todos os Livros.csv')

#instalar 
#sudo apt-get install chromium-chromedriver


#APPLY EVAL
converteLista = lambda x: eval(x)
df = [df.iloc[i].apply(converteLista) for i in range(len(df))]

#CLEANING LIST
for i in range(len(df)):
    for j in range(len(df[i])):
        lista = df[i][j]
        lista_tratada = [livro for livro in lista if livro != 'Mais vendido']
        lista_tratada = [livro for livro in lista if livro != 'Patrocinados']

        df[i][j] = lista_tratada

#DATAFRAME
df = pd.DataFrame(df)
df = df.T

CATEGORIAS = ['Auto Ajuda', 'Ficção Cientifica', 'Historia', 'Literatura', 'Policial Suspense Misterio', 'Romance']
df.columns = CATEGORIAS


#FUNÇÃO PARA TRATAR TEXTO
def dataCleaning(titulo: str) -> str:

    #ELIMINANDO ()
    titulo = titulo.replace('(', 'ini_parent')
    busca = re.search(r'(.*?) ini_parent', titulo)

    if busca != None:
        titulo = busca.group(1)

    # ELIMINANDO +
    titulo = titulo.replace('+', 'plus')
    busca = re.search(r'(.*?) plus', titulo)

    if busca != None:
        titulo = busca.group(1)

    #ELIMINANDO TRAÇOS
    busca = re.search(r'(.*?) - ', titulo)
    if busca != None:
        titulo = busca.group(1)

    return titulo

#TRATANDO TÍTULOS
for CATEGORIA in CATEGORIAS:
    for i in range(len(df)):
        lista_tratada = pd.Series(df[CATEGORIA][i]).apply(dataCleaning)
        df[CATEGORIA][i] = lista_tratada.to_list()



#--------------------------------------------#
#               Preliminares                 #
#--------------------------------------------#

#os.mknod('Historia.csv')

#--------------------------------------------#
#               Web Scraping                 #
#--------------------------------------------#

#CONECTANDO AO DRIVER
driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")

#CONECTANDO AO SKOOB
driver.get(f'https://www.skoob.com.br/')

#Login e senha da conta
input('Insira Logina e Senha\n')




for i in range(len(df)):
    for j in range(len(df['Historia'][i])):

        driver.refresh()

        try:

            #CAPTURANDO TÍTULO ORIGINAL
            titulo_original = df['Historia'][i][j]

            #PROCURANDO LIVRO
            busca = driver.find_element_by_xpath('//*[@id="search"]')
            busca.click()
            busca.send_keys(titulo_original)

            time.sleep(3)

            #CLICANDO NA LUPA
            lupa = driver.find_element_by_xpath('/html/body/div/div[1]/div/div[1]/form/div[2]/span/button').click()

            time.sleep(2)

            #CLICANDO NO PRIMEIRO ITEM DA LISTA (VERIFICAR SE EXISTE)
            try:
                driver.find_element_by_xpath('/html/body/div/div[2]/div[3]/div/div/div[2]/div[2]/div[2]/div[2]/a[1]').click()
            except:
                continue

            #CLICANDO EM ESPAÇO EM BRANCO
            webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()

            time.sleep(1)

            #CAPTURANDO TÍTULO CAPTURADO
            titulo_capturado = driver.find_element_by_css_selector('#pg-livro-titulo > h1')
            titulo_capturado = titulo_capturado.text

            #CAPTURANDO DESCRIÇÃO
            descricao = driver.find_element_by_css_selector('#livro-perfil-sinopse-txt > p')
            descricao = descricao.text

            nova_linha = titulo_original + ';' + titulo_capturado + ';' + descricao

            with open('FiccaoCientifica.csv', 'a') as acc_csv:
                acc_csv.write(nova_linha + '\n')
        except Exception as erro:
            print('Erro: ', erro)
            continue

with open('Historia.csv', 'r') as acc_csv:
    acc_csv.close()
