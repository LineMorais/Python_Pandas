#%%
import pandas as pd

# %%
df = pd.read_excel("../data/transactions.xlsx")
df


# %%
df.info()
# %% mostra quantas linhas e quandas colunas tem no dataframe

df.shape
# %% as primeiras 5 linhas
df.head()
# %% as ultimas 5 linhas
df.tail()
# %%
