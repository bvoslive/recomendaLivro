
#########################################################################
#                                                                       #
# É preciso verificar se na data presente há disponível algum DO, se não#
# o programa é encerrado. Quando não há DO um texto é mostrado:         #
# Texto: 'Data sem publicacao.'                                         #
#                                                                       #
#########################################################################

# Bibliotecas
import selenium
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile

import time                         # Biblioteca para forçar o dalay
import datetime                     # Biblioteca para pegar datase horas
import requests                     # Fazer requisicao no site
import os                           # Sistema
from os import listdir, getcwd
import PyPDF2                       # Manipulacao de PDFs
from PyPDF2 import PdfFileMerger
import pathlib                      # Enderecos
import requests

import pandas as pd



#########################################################################
#                                                                       #
#                             Conectando ao site
#                                                                       #
#########################################################################
# Pre-Requisitos do Firefox
firefox_capabilities = DesiredCapabilities.FIREFOX
firefox_capabilities['marionette'] = True


# Bloco responsavel por permitir o salvamento automatico do xls gerado pelo site
fp = webdriver.FirefoxProfile()
fp.set_preference("browser.preferences.instantApply", True)
fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/pdf")
fp.set_preference("browser.helperApps.alwaysAsk.force", False)
fp.set_preference("browser.download.manager.showWhenStarting", False)
fp.set_preference("browser.download.folderList", 2)
fp.set_preference("browser.altClickSave", False)

binary = FirefoxBinary('C:\\Program Files\\Mozilla Firefox\\firefox.exe')


# Browser-Robo: configuracao do robo
web = webdriver.Firefox(firefox_binary=binary, executable_path='geckodriver.exe',
                        capabilities=firefox_capabilities, firefox_profile=fp)




#########################################################################
#                                                                       #
#                       Capturando Dados da Amazon
#                                                                       #
#########################################################################

#LINKS LIVROS




auto_ajuda = 'https://www.amazon.com.br/s?i=stripbooks&bbn=7841278011&rh=n%3A6740748011%2Cn%3A7841720011&dc&fs=true&qid=1613435977&rnid=7841278011&ref=sr_nr_n_4'

ficcao_cientifica = 'https://www.amazon.com.br/s?rh=n%3A7841775011&fs=true&ref=lp_7841775011_sar'

historia = 'https://www.amazon.com.br/s?i=stripbooks&bbn=7841278011&rh=n%3A6740748011%2Cn%3A7843068011&dc&fs=true&qid=1613436314&rnid=7841278011&ref=sr_nr_n_16'

literaturaEficcao = 'https://www.amazon.com.br/s?i=stripbooks&bbn=7841278011&rh=n%3A6740748011%2Cn%3A7872687011&dc&fs=true&qid=1613436486&rnid=7841278011&ref=sr_nr_n_21'

policial_suspense_misterio = 'https://www.amazon.com.br/s?i=stripbooks&bbn=7841278011&rh=n%3A6740748011%2Cn%3A7872829011&dc&fs=true&qid=1613520812&rnid=7841278011&ref=sr_nr_n_23'

romance = 'https://www.amazon.com.br/s?i=stripbooks&bbn=7841278011&rh=n%3A6740748011%2Cn%3A7882388011&dc&fs=true&qid=1613520812&rnid=7841278011&ref=sr_nr_n_26'

pd.DataFrame()



# Acessar pag com a data de hoje
web.get(policial_suspense_misterio)


num_elementos = web.find_elements_by_xpath('//*[@id="search"]/div[1]/div[2]/div/span[3]/div[2]/div')






#Número de elementos
num_elementos = len(num_elementos)
num_elementos = num_elementos-2

#Captura titulos
nomes = []
for k in range(1, num_elementos):
    print(k)
    nome = web.find_element_by_xpath(f'//*[@id="search"]/div[1]/div[2]/div/span[3]/div[2]/div[{k}]/div/span/div/div/div[2]/div[2]/div/div[1]/div/div/div[1]/h2/a/span')
    nome = str(nome.text)
    
    nomes.append(nome)





def capturaNomesLivros():
    nomess = web.find_elements_by_xpath('//*[@id="search"]/div[1]/div[2]/div/span[3]/div[2]/div')

    TAM_NOMES = len(nomess)

    livros = []
    for i in range(TAM_NOMES-3):

        nome = nomess[i].text
        nome = nome.split('\n')
        nome = nome[0]

        livros.append(nome)

    return livros


capturaNomesLivros()






#########################################################################
#                                                                       #
#                       Capturando Dados da Amazon - CORRETO
#                                                                       #
#########################################################################


GENEROS = ['Auto Ajuda', 'Ficção Científica', 'História', 'Literatura e Ficção', 'Policial Suspense e Mistério', 'Romance']


LINKS = [
    'https://www.amazon.com.br/s?i=stripbooks&bbn=7841278011&rh=n%3A6740748011%2Cn%3A7841720011&dc&fs=true&qid=1613435977&rnid=7841278011&ref=sr_nr_n_4',
    'https://www.amazon.com.br/s?rh=n%3A7841775011&fs=true&ref=lp_7841775011_sar',
    'https://www.amazon.com.br/s?i=stripbooks&bbn=7841278011&rh=n%3A6740748011%2Cn%3A7843068011&dc&fs=true&qid=1613436314&rnid=7841278011&ref=sr_nr_n_16',
    'https://www.amazon.com.br/s?i=stripbooks&bbn=7841278011&rh=n%3A6740748011%2Cn%3A7872687011&dc&fs=true&qid=1613436486&rnid=7841278011&ref=sr_nr_n_21',
    'https://www.amazon.com.br/s?i=stripbooks&bbn=7841278011&rh=n%3A6740748011%2Cn%3A7872829011&dc&fs=true&qid=1613520812&rnid=7841278011&ref=sr_nr_n_23',
    'https://www.amazon.com.br/s?i=stripbooks&bbn=7841278011&rh=n%3A6740748011%2Cn%3A7882388011&dc&fs=true&qid=1613520812&rnid=7841278011&ref=sr_nr_n_26'
]


len(LINKS)

lista_pesquisa = pd.DataFrame({'GENEROS': GENEROS, 'LINKS': LINKS})

lista_pesquisa




#subir pro git


for i in range(len(lista_pesquisa)):

    # Acessar página
    web.get(lista_pesquisa['LINKS'])

    capta_livro = []

    paginas = 8
    #Percorrendo Página
    for pagina in range(0, 30):

        time.sleep(1)

        conteudo = capturaNomesLivros()

        print(conteudo)

        capta_livro.append(conteudo)

        time.sleep(1)
        proximo = web.find_elements_by_css_selector('.a-last > a:nth-child(1)')
        proximo = proximo[0]
        proximo.click()







capta_livro = []
for pagina in edf:
    for livro in pagina:
        capta_livro.append(livro)
















for k in range(6):
    print('K = ', k)
    
    print('metodo 1')

    web.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[2]/div/span[3]/div[2]/div[17]/span/div/div/ul/li[9]').click()


    
    print('metodo 2')

    web.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[2]/div/span[3]/div[2]/div[17]/span/div/div/ul/li[7]/a').click()











web.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[2]/div/span[3]/div[2]/div[17]/span/div/div/ul/li[7]/a').click()




/html/body/div[1]/div[2]/div[1]/div[2]/div/span[3]/div[2]/div[17]/span/div/div/ul/li[7]/a
/html/body/div[1]/div[2]/div[1]/div[2]/div/span[3]/div[2]/div[17]/span/div/div/ul/li[7]/a



//*[@id="search"]/div[1]/div[2]/div/span[3]/div[2]/div[17]/span/div/div/ul/li[3]/a



/html/body/div[1]/div[2]/div[1]/div[2]/div/span[3]/div[2]/div[17]/span/div/div/ul/li[7]/a

web.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[2]/div/span[3]/div[2]/div[17]/span/div/div/ul/li[9]/a').click()



/html/body/div[1]/div[2]/div[1]/div[2]/div/span[3]/div[2]/div[17]/span/div/div/ul/li[8]/a


nomes


p = 2

for p in range(1, num_elementos+1):
    nome = web.find_element_by_xpath(f'//*[@id="search"]/div[1]/div[2]/div/span[3]/div[2]/div[{p}]/div/span/div/div/div[2]/div[2]/div/div[1]/div/div/div[1]/h2/a/span')

    nome = str(nome.text)

    print(nome)


num_elementos


nome.text







#########################################################################
#                                                                       #
#                         Capturando dados do Skoob
#                                                                       #
#########################################################################


# Acessar pag com a data de hoje
web.get(f'https://www.skoob.com.br/')

busca = web.find_element_by_xpath('//*[@id="search"]')
busca.click()
busca.send_keys('Senhor dos Anéis')

lupa = web.find_element_by_xpath('/html/body/div/div[1]/div/div[1]/form/div[2]/span/button').click()

filmes = web.find_element_by_xpath('/html/body/div/div[2]/div[3]/div/div/div[2]/div[2]/div[2]/div[2]/a[1]').click()

webdriver.ActionChains(web).send_keys(Keys.ESCAPE).perform()

filmes = web.find_elements_by_xpath('//div[@id="resultadoBusca"]/div/div[@class="box_lista_busca_vertical_capa"]/a/img')
len(filmes)
filmes[0]

filmes = web.find_elements_by_xpath('//div[@class="detalhes"]/a')

len(filmes)

dir(filmes[0])

filmes[30].text




#########################################################################
#                                                                       #
#                               Rascunhos
#                                                                       #
#########################################################################



proximo = web.find_element_by_xpath(
    '//*[@id="topo-menu-search"]/div[2]/span/button')  # Botao "Proxima"
proximo.click()


proximo = web.find_element_by_xpath(
    '/html/body/div/div[2]/div[3]/div/div/div[2]/div[2]/div[2]/div[2]
')  # Botao "Proxima"
proximo.click()


div.box_lista_busca_vertical:nth-child(2) > div:nth-child(2) > div:nth-child(2) > a:nth-child(1)



verificar_DOU = web.find_element_by_xpath('//span[@id="txtError"]')
verificar_DOU = str(verificar_DOU.text)

teste = web.find_element_by_xpath('//*[@id="livro-perfil-sinopse-txt"]')




if verificar_DOU == 'Data sem publicacao.':
    for repetir in range(0, 6):
        print('Sem DOU no dia! Obtendo DOU de sabado.')
        print('Apagando os PDFs antigos.')
    pdf_delete = path + "\\PDFs"

    # Deletar os arquivos .pdf
    filelist = [f for f in os.listdir(pdf_delete) if f.endswith(".pdf")]
    for f in filelist:
        os.remove(os.path.join(pdf_delete, f))

    for i in range(0, 10):
        for k in range(0, 10):
            for j in range(0, 10):
                r  = requests.get(f'http://diariooficial.imprensaoficial.com.br/doflash/prototipo/{data_ano_sabado}/{mes_sabado}/{data_dia_sabado}/cidade/pdf/pg_0{j}{i}{k}.pdf')

                time.sleep(0.3)
                if r.status_code == 200:
                    with open(f'{path}\\PDFs\\pdf_cidade_SP{j}{i}{k}.pdf', 'wb', ) as f:
                        f.write(r.content)
                else:
                    break
                

else:
    print('Hoje tem DOU. Apagando os PDFs antigos!')
    # Apagar os pdf já baixado baixados
    pdf_delete = path + "\\PDFs"
    # Deletar os arquivos .pdf
    filelist = [f for f in os.listdir(pdf_delete) if f.endswith(".pdf")]
    for f in filelist:
        os.remove(os.path.join(pdf_delete, f))

    # Acessar pagina para fazer o download dos pdfs
    for i in range(0, 10):
        for k in range(0, 10):
            for j in range(0, 10):
                r  = requests.get(f'http://diariooficial.imprensaoficial.com.br/doflash/prototipo/{data_ano}/{mes}/{data_dia}/cidade/pdf/pg_0{i}{j}{k}.pdf')
                time.sleep(0.3)
                if r.status_code == 200:
                    print(i,k,j)
                    with open(f'{path}\\PDFs\\pdf_cidade_SP{i}{j}{k}.pdf', 'wb', ) as f:
                        time.sleep(0.1)
                        f.write(r.content)
                else:
                    break


print('Terminou')
web.close()
web.quit()  # Fechar a pagina0
