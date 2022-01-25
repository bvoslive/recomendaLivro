#--------------------------------------------#
#           Importando bibliotecas           #
#--------------------------------------------#

import pandas as pd
from gensim.models import KeyedVectors
from nltk.corpus import stopwords
import nltk
import time
import glob
import string
nltk.download('stopwords')

#--------------------------------------------#
#               Data Cleaning                #
#--------------------------------------------#

COLUNAS = ['ORIGINAL', 'CAPTURADO', 'DESCRICAO']

#IMPORTANDO DATASETS
df_ficcao = pd.read_csv('../CSVs/FICCAO_CIENTIFICA.csv', header = None, sep = ';', error_bad_lines=False, names = COLUNAS)
df_ajuda = pd.read_csv('../CSVs/AUTO_AJUDA.csv', header = None, sep = ';', error_bad_lines = False, names = COLUNAS)
df_historia = pd.read_csv('../CSVs/HISTORIA.csv', header = None, sep = ';', error_bad_lines = False, names = COLUNAS)
df_literatura = pd.read_csv('../CSVs/LITERATURA.csv', header = None, sep = ';',error_bad_lines = False, names = COLUNAS)
df_misterio = pd.read_csv('../CSVs/POLICIAL_SUSPENSE_MISTERIO.csv', sep = ';',header = None, error_bad_lines=False, names = COLUNAS)
df_romance = pd.read_csv('../CSVs/ROMANCE.csv', header = None, sep = ';',error_bad_lines = False, names = COLUNAS)

df_ficcao['TIPO'] = 'FICCAO CIENTIFICA'
df_ajuda['TIPO'] = 'AUTO AJUDA'
df_historia['TIPO'] = 'HISTORIA'
df_literatura['TIPO'] = 'LITERATURA'
df_misterio['TIPO'] = 'POLICIAL SUSPENSE MISTERIO'
df_romance['TIPO'] = 'ROMANCE'

#CONCATENANDO DATAFRAMES
df = pd.concat([df_ficcao, df_ajuda, df_historia, df_literatura, df_misterio, df_romance])

#ELIMINANDO NULOS
df.dropna(inplace=True)

df.reset_index(drop=True, inplace=True)

#--------------------------------------------#
#         Natural Language Processing        #
#--------------------------------------------#

#IMPORTANDO MODELO PRE-TREINADO
model = KeyedVectors.load_word2vec_format('/home/bruno/Documents/Model Zoo/glove_s300.txt')

#REMOVENDO STOPWORDS
portuguese_stopwords = stopwords.words('portuguese')

#ELIMINANDO PONTUACOES
pontuacoes = string.punctuation

def textCleaning(descricao: str) -> str:

    descricao = [letra for letra in descricao if letra not in pontuacoes]
    descricao = ''.join(descricao)
    descricao = descricao.lower().split()
    descricao = [palavra for palavra in descricao if not palavra in set(portuguese_stopwords)]
    descricao = [palavra for palavra in descricao if not palavra.isnumeric()]

    return descricao

#TEXT CLEANING
lista_descricao = df['DESCRICAO'].to_list()

for i in range(len(lista_descricao)):
    lista_descricao[i] = textCleaning(lista_descricao[i])

sentenca_atual = str(input('Digite aqui uma descrição: '))
sentenca_atual = textCleaning(sentenca_atual)

pontos_acc = []
for i in range(len(lista_descricao)):
    sentenca_compara = lista_descricao[i]
    pontuacao = model.wmdistance(sentenca_atual, sentenca_compara)
    pontos_acc.append(pontuacao)

df_sort = df.copy()
df_sort['PONTOS'] = pontos_acc
df_sort.drop_duplicates('DESCRICAO', inplace=True)
df_sort.sort_values('PONTOS', inplace=True)
df_sort.reset_index(drop=True, inplace=True)

print(df_sort.iloc[:5])
