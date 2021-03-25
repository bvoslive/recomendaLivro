#--------------------------------------------#
#           Importando bibliotecas           #
#--------------------------------------------#

import pandas as pd
from gensim.models import KeyedVectors
from nltk.corpus import stopwords
import nltk
import time
nltk.download('stopwords')

#--------------------------------------------#
#               Data Cleaning                #
#--------------------------------------------#

df = pd.read_csv('FiccaoCientifica.csv', header=None, error_bad_lines=False)





lista_livros = [item for item in df[0] if 'Mais vendido' not in item]
df = pd.Series(lista_livros)

tam_str = lambda x: x.count(';')
catch_comma = df.apply(tam_str)
catch_comma = catch_comma > 0

df = df[catch_comma]
df.reset_index(drop=True, inplace=True)



for i in range(len(df)):

    texto_analisado = list(df[i])

    count = 0
    for j in range(len(texto_analisado)):
        
        
        if texto_analisado[j] == ';':
            texto_analisado[j] = '_'
            count+=1

        if count == 2: break
    
    df[i] = ''.join(texto_analisado)

#SEPARANDO POR _
sep_underline = lambda x: x.split('_')
df = df.apply(sep_underline)

df = df.to_list()
df = pd.DataFrame(df, columns = ['ORIGINAL', 'CAPTURADO', 'DESCRICAO'])

df.dropna(subset=['DESCRICAO'], inplace=True)
df.reset_index(drop=True, inplace=True)






#--------------------------------------------#
#         Natural Language Processing        #
#--------------------------------------------#


#IMPORTANDO MODELO PRE-TREINADO
model = KeyedVectors.load_word2vec_format('/home/bruno/Documents/Model Zoo/cbow_s100.txt')

#REMOVENDO STOPWORDS
portuguese_stopwords = stopwords.words('portuguese')


fragmento_sentenca_atual = df['DESCRICAO'][137]

sentenca_atual = fragmento_sentenca_atual.lower().split()
sentenca_atual = [word for word in sentenca_atual if not word in set(portuguese_stopwords)]
sentenca_atual = [word for word in sentenca_atual if not word.isnumeric()]


sentenca_atual



start = time.time()
pontuacoes = []
for i in range(len(df['DESCRICAO'])):


    sentenca_comparada = df['DESCRICAO'][i].lower().split()
    sentenca_comparada = [word for word in sentenca_comparada if not word in set(portuguese_stopwords)]
    sentenca_comparada = [word for word in sentenca_comparada if not word.isnumeric()]

    ponto = model.wmdistance(sentenca_atual, sentenca_comparada)
    pontuacoes.append(ponto)
stop = time.time()




stop - start


df['PONTOS'] = pontuacoes

df.sort_values('PONTOS')['DESCRICAO'].iloc[6]

