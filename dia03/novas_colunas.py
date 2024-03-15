#%%
import pandas as pd
import numpy as np

# %%
df = pd.read_csv("../data/customers.csv", sep=';')
df

# %%
df['Points_double'] = df['Points'] *2
df
# %%
df['Points_ratio'] = df['Points_double'] / df['Points']
df

# %%
df['Constante'] = 1
df 

# %%
df["Points_log"] = np.log(df['Points'])
df

# %%
np.log(df[['Points', 'Points_double', 'Points_ratio' ]])

# %%
nomes_alta = []
for i in df['Name']:
    nomes_alta.append(i.upper())

df["Nome_alta"] = nomes_alta
df

# %%
df['Name'].str.upper()

# %% Função para retornar o primeiro nome da coluna Name.
def get_firts(nome:str):
    nome = nome.upper()
    return nome.split('_')[0]

#%%
df['Name_Fist'] = df['Name'].apply(get_firts)
df

# %%
get_f = lambda nome: nome.split('_')[0]
get_f('Téo')

# %%
df['Name'].apply(lambda x: x.upper().split('_')[0])


# %%

def intervalo_pontos(pontos):
    if pontos < 2500:
        return "baixo"
    elif pontos < 3500:
        return "medio"
    else:
        return "alto"
    
df["Faixa_Pontos"] = df["Points"].apply(intervalo_pontos)
df


# %%
