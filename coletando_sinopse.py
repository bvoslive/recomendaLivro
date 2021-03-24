#--------------------------------------------#
#           Importando bibliotecas           #
#--------------------------------------------#

import pandas as pd
import requests
import re
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
        df[i][j] = lista_tratada

#DATAFRAME
df = pd.DataFrame(df)
df = df.T

CATEGORIAS = ['Auto Ajuda', 'Ficção Cientifica', 'Historia', 'Literatura', 'Policial Suspense Misterio', 'Romance']
df.columns = CATEGORIAS


#CAPTURANDO TITULO
titulo = df['Ficção Cientifica'][0][0]


df['Ficção Cientifica'][8]


teste = 'O Sangue do Olimpo - Volume 5. Série Os Heróis do Olimpo'

#O rei perverso (Vol. 2 O Povo do Ar)

#ELIMINANDO PARENTESIS
teste = teste.replace('(', 'ini_parent')
busca = re.search(r'(.*?) ini_parent', teste)

if busca != None


# ELIMINANDO +
teste = teste.replace('+', 'plus')
busca = re.search(r'(.*?) plus', teste)

if busca != None


busca = re.search(r'(.*?)-', teste)
if busca != None









s = 'Part 1. Part 2. Part 3 then more text'
re.search(r'(.*?)Part 3', s).group(1)


df
#Elimimar tudo que tiver 
#     eliminar +% (tudo que está entre parentesis) .%



#--------------------------------------------#
#               Web Scraping                 #
#--------------------------------------------#

#CONECTANDO AO DRIVER
driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")

#CONECTANDO AO SKOOB
driver.get(f'https://www.skoob.com.br/')


#Login e senha da conta


#PROCURANDO LIVRO
busca = driver.find_element_by_xpath('//*[@id="search"]')
busca.click()
busca.send_keys('Senhor dos Anéis')

#CLICANDO NA LUPA
lupa = driver.find_element_by_xpath('/html/body/div/div[1]/div/div[1]/form/div[2]/span/button').click()

#CLICANDO NO PRIMEIRO ITEM DA LISTA (VERIFICAR SE EXISTE)
driver.find_element_by_xpath('/html/body/div/div[2]/div[3]/div/div/div[2]/div[2]/div[2]/div[2]/a[1]').click()

#CLICANDO EM ESPAÇO EM BRANCO
webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()

#CAPTURANDO TÍTULO
titulo = driver.find_element_by_css_selector('#pg-livro-titulo > h1')
titulo = titulo.text

#CAPTURANDO DESCRIÇÃO
descricao = driver.find_element_by_css_selector('#livro-perfil-sinopse-txt > p')
descricao = descricao.text









#---------------------------------
df['Ficção Cientifica'][0]


idt = driver.find_elements_by_xpath('//*[@id="bookDesc_iframe_wrapper"]')












search = driver.find_element_by_xpath('//*[@id="twotabsearchtextbox"]')
search.send_keys(titulo)

#Clicando em procurar
click = driver.find_element_by_xpath('//*[@id="nav-search-submit-button"]')
click.click()


path_primeiro_livro = '//*[@id="search"]/div[1]/div/div[1]/div/span[3]/div[2]/div[2]/div/span/div/div/div[2]/div[2]/div/div[1]/div/div/div[1]/h2/a/span'

#COLOCAR AQUI O WAITUNTIL
click = driver.find_element_by_xpath(path_primeiro_livro)
click.click()



driver.get('https://www.skoob.com.br/livro/636009ED637542')

click = driver.find_element_by_xpath('//*[@id="livro-perfil-sinopse-txt"]/p')
click.text

click.click()







iframe = driver.find_element_by_xpath('//*[@id="bookDesc_iframe_wrapper"]')
driver.switch_to.frame(iframe)
aa = driver.switch_to.default_content()





# Pega o XPath do iframe e atribui a uma variável
iframe = driver.find_element_by_xpath("//*[@id="editor"]/div[3]/div[3]/iframe")

# Muda o foco para o iframe
driver.switch_to.frame(iframe)

# Retorna para a janela principal (fora do iframe)
driver.switch_to.default_content()
type(aa)




desc_iframe = driver.switch_to.frame('//*[@id="bookDesc_iframe"]')




driver.find_element_by_id('//*[@id="bookDescription_feature_div"]')

dir(driver.find_element_by_xpath('//*[@id="bookDescription_feature_div"]'))

driver.find_element_by_xpath('//*[@id="bookDescription_feature_div"]').value_of_css_property


driver.text



