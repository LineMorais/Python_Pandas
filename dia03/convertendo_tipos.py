#%%
import pandas as pd

df = pd.read_csv("../data/customers.csv", sep=';')
df
# %%
df.dtypes
# %% converter o tipo de dado da coluna ex: de int para str
df["Points"].astype(str)
# %%
