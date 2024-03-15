# %% 
import pandas as pd
import numpy as np
# %%
data = {
    "nome":["Téo", "Nah", "Lah", "Mah", "Jo"],
    "idade":[31, 32, 34, 12, np.nan],
    "renda":[np.nan, 3245, 357, 12432, np.nan]
}

df=pd.DataFrame(data)
df

# %% retorna True e Falso  e True == NAN
df['idade'].isna()

# %% Somar para saber a quantidade de NAN tem 

df['idade'].isna().sum()


# %%
df.isna()

# %% retorna quantos NAN tem em cada coluna do dataframe
df.isna().sum()

# %% taxa (proporção) de NAN dentro de cada coluna do dataframe.
df.isna().mean()

# %% como preencher os nulos(NAN)
df.fillna({
    'idade': df['idade'].mean(),
    'renda': df['renda'].mean() 
    })

# %% remoção de nAN
df.dropna()
df

# %% avalia linha (all = as duas tem que ser nan 
#   | any = ao menos 1 tem que nan
df.dropna(subset=['idade', 'renda'], how='any')

# %% avaliar colunas
df.dropna(axis=1)
# %%
