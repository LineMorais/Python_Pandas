# %%
import pandas as pd

# %%

df_customers = pd.read_csv("../data/customers.csv", sep=";")
df_customers
# %%
df_customers.shape
# %%
df_customers.info(memory_usage='deep')
# %%
df_customers['Points'].describe()
# %%
df_customers['Points'] > 1000

# %%
condicao = df_customers['Points'] > 1000
df_customers[condicao]

# %%

maximo = df_customers['Points'].max()
condicao = df_customers['Points'] == maximo
df_customers[condicao]

# %%
notas = [4.5, 6, 7, 3.5]
for i in notas:
    if i > 5:
        print(i)
# %%
notas_novas = []
for i in notas:
    notas_novas.append(i+1)

notas_novas

#%%
df_customers[df_customers['Points'] == df_customers['Points'].max()]['Name'].iloc[0]

# %%
condicao = df_customers['Points'] == df_customers['Points'].max()
df_maior = df_customers[condicao]
df_maior['Name'].iloc[0]


# %% utilizando & = AND = e
condicao = (df_customers['Points'] >= 1000) & (df_customers['Points'] <= 2000)
df_customers[condicao].describe()

# %% referencia 

a = [1, 2, 3, 4]
b = a
print(a)
print(b)

b.append(5)
print(a)
print(b)

# %% fazendo um copia da lista a e atribuindo na variavel b

a = [1, 2, 3, 4]
b = a.copy()
print(a)
print(b)

b.append(5)
print(a)
print(b)

# %% Criar um copia do dados filtrados

condicao = (df_customers['Points'] >= 1000) & (df_customers['Points'] <= 2000)
df_1000_2000 = df_customers[condicao].copy()
df_1000_2000['Points'] = df_1000_2000['Points'] + 1000
df_1000_2000

# %% Filtrar 2 colunas ao mesmo tempo

df_customers[['UUID', 'Name']]

# %% converter para lista e .sort() para ordenar a lista
colunas = df_customers.columns.tolist()
colunas.sort()
colunas

# %%
df_customers[colunas]

# %%

df_customers =df_customers[colunas]
df_customers

# %% renomear colunas
df_customers = df_customers.rename(columns={"Name":"Nome", "Points":"Pontos"})


# %% renomenado a coluna já direto no df passando o inplace=True
df_customers.rename(columns={'UUID':'ID'}, inplace=True)
df_customers

