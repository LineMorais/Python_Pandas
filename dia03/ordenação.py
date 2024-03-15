# %% 
import pandas as pd

# %%
df = pd.read_csv("../data/customers.csv", sep=';')
df
# %%
df.sort_values(by='Points', ascending=False, inplace=True)
df.rename(columns={'Name':'Nome', 'Points':'Pontos'}, inplace=True)
df

# %%
df = (df.sort_values(by='Pontos', ascending=False)
        .rename(columns ={'Name':'Nome', 'Points':'Pontos'}))
df
# %%
