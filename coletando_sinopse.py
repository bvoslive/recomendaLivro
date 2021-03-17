import pandas as pd

df = pd.read_csv('Todos os Livros.csv')

cat = ['Auto Ajuda', 'Ficção Cientifica', 'Historia', 'Literatura', 'Policial Suspense Misterio', 'Romance']

df['Categorias'] = cat

converteLista = lambda x: eval(x)



df = [df.iloc[i].apply(converteLista) for i in range(len(df))]





len(df)



seq_cat_livros = []
for p in range(len(df)):

    TAM_CAT = len(df[p])

    seq_livros = []
    for i in range(TAM_CAT):
        livros =  [df[p][i][j] for j in range(len(df[p][i])) if df[p][i][j] != 'Mais vendido']
        seq_livros.append(livros)

    seq_cat_livros.append(seq_livros)


seq_cat_livros[0][0]


df[5]



