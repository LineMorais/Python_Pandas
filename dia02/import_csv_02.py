#%% 
import pandas as pd
# %%
df = pd.read_csv("../data/products.csv", 
                 sep=';',
                 names=['Id', 'Name', 'Description']
                 )

# %%
df.rename(columns={'Name':'Nome', 'Description':'Descrição'}, inplace=True)
df

# %%
colunas = ['UUID', 'Points', 'IdCustomer', 'DtTransaction']

df= df[colunas]
# %%
df
# %%
df.info(memory_usage='deep')
# %%
