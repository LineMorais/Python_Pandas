#%%
import pandas as pd

# %%
dados = [10, 20, 42, 9, 12, 35, 24, 10, 8, 14,21]

series_dados = pd.Series(dados)
series_dados

# %%

series_dados.mean()
# %%
series_dados.std()
# %%
series_dados.max()





# %%

dados2 = {"nome":["Téo", "Nah", "Napoleão"], "idade":[31, 32, 14]}

df = pd.DataFrame(dados2)
df

#%%

sumario = df.columns
sumario

# %%
sumario = df.describe()
sumario['idade']['mean']

# %%
df['nome'].iloc[2]
# %%
