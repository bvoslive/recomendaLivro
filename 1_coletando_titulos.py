#--------------------------------------------#
#           Importando bibliotecas           #
#--------------------------------------------#

import pandas as pd
import time
from typing import List
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# Browser-Robo: configuracao do robo
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
web = webdriver.Firefox(firefox_binary=binary, executable_path='geckodriver.exe',
                        capabilities=firefox_capabilities, firefox_profile=fp)

#--------------------------------------------#
#             Capturando Títulos             #
#--------------------------------------------#

#PREPARANDO DADOS
GENEROS = ['Auto Ajuda', 'Ficção Científica', 'História', 'Literatura e Ficção', 'Policial Suspense e Mistério', 'Romance']

LINKS = [
    'https://www.amazon.com.br/s?i=stripbooks&bbn=7841278011&rh=n%3A6740748011%2Cn%3A7841720011&dc&fs=true&qid=1613435977&rnid=7841278011&ref=sr_nr_n_4',
    'https://www.amazon.com.br/s?rh=n%3A7841775011&fs=true&ref=lp_7841775011_sar',
    'https://www.amazon.com.br/s?i=stripbooks&bbn=7841278011&rh=n%3A6740748011%2Cn%3A7843068011&dc&fs=true&qid=1613436314&rnid=7841278011&ref=sr_nr_n_16',
    'https://www.amazon.com.br/s?i=stripbooks&bbn=7841278011&rh=n%3A6740748011%2Cn%3A7872687011&dc&fs=true&qid=1613436486&rnid=7841278011&ref=sr_nr_n_21',
    'https://www.amazon.com.br/s?i=stripbooks&bbn=7841278011&rh=n%3A6740748011%2Cn%3A7872829011&dc&fs=true&qid=1613520812&rnid=7841278011&ref=sr_nr_n_23',
    'https://www.amazon.com.br/s?i=stripbooks&bbn=7841278011&rh=n%3A6740748011%2Cn%3A7882388011&dc&fs=true&qid=1613520812&rnid=7841278011&ref=sr_nr_n_26'
]

lista_pesquisa = pd.DataFrame({'GENEROS': GENEROS, 'LINKS': LINKS})


#FUNÇÃO PARA CAPTURAR LIVROS DAS PÁGINAS
def capturaTitulosLivros() -> List:
    titulos = web.find_elements_by_xpath('//*[@id="search"]/div[1]/div[2]/div/span[3]/div[2]/div')

    TAM_NOMES = len(titulos)
    livros = []
    for i in range(TAM_NOMES-3):

        titulos = titulos[i].text
        titulos = titulos.split('\n')
        titulos = titulos[0]

        livros.append(titulos)

    return livros

#CAPTURANDO TÍTULOS DOS LIVROS
todos_os_livros = []
for i in range(len(lista_pesquisa)):

    # Acessar página
    web.get(lista_pesquisa['LINKS'][i])
    capta_livro = []
    paginas = 8
    #Percorrendo Página
    for pagina in range(0, 30):

        #CAPTURANDO TITULO
        time.sleep(1)
        conteudo = capturaTitulosLivros()
        capta_livro.append(conteudo)

        time.sleep(1)
        proximo = web.find_elements_by_css_selector('.a-last > a:nth-child(1)')
        proximo = proximo[0]
        proximo.click()

    todos_os_livros.append(capta_livro)

#EXPORTANDO RESULTADOS
todos_os_livros = pd.DataFrame(todos_os_livros)
todos_os_livros.to_csv('../CSVs/Todos os Livros.csv', index=False)

