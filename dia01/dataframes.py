#%%
import pandas as pd
# %%

data = {
    "nome":["teo", "nah", "lara", "maria"],
    "sobrenome":["calvo", "ataide", "calvo", "calvo"],
    "idade":[31, 32, 31, 2]
}

#%%
data["idade"][0]
# %%
df = pd.DataFrame(data)
df

# %% serie da coluna idade
df["idade"]

# %% para garantir que vc irá pegar a posição correta
df["idade"].iloc[0]

# %%
type(df["idade"])

# %%
df["sobrenome"]
# %%
df["sobrenome"].iloc[0]

# %% primeira linha do df = Serie
 
df.iloc[0]
# %% 

type(df.iloc[0])
# %%
df.columns

# %%
df.index

# %%

df.info()
# %% 

df.info(memory_usage='deep')

# %% serie que carrega o tipos de cada coluna
df.dtypes

# %% aplica a estatistca para coluna que é numerica.

df.describe()

# %%

df['peso'] = [80, 53, 65, 14]
df.describe()

# %%

sumario = df.describe()
sumario['peso']['mean']

# %% mostra as 5 primieras linhas do DF

df.head()
# %% mostra as 5 ultimas linhas

df.tail(2)
# %%
