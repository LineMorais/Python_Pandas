#%%
import pandas as pd

# %%
data_01 = {
    "id":[1, 2, 3, 4],
    "nome":["Téo", "Nah", "Lah", "Mah"],
    "idade":[31, 32, 34, 32]
}

df_01 = pd.DataFrame(data_01)
df_01

#%%
data_02 = {
    "id":[5,6,7,8],
    "nome":["Jose", "Nathan", "Arnaldo", "Mario"],
    "idade":[23, 33, 19, 21]
}
df_02 = pd.DataFrame(data_02)
df_02

#%%
data_03 = {
    "sobrenome":["Calvo", "Silva", "Costa", "Souza"],
    "renda":[3100, 3100, 3200, 3200]
}
df_03 = pd.DataFrame(data_03)
df_03

# %% coloca uma planilha em baixo da outra
# concatenar em linhas
# reseta o index para deixar a numeraçao correta

pd.concat([df_01, df_02]).reset_index(drop=True)


# %% concaternar na coluna (pelo indice)

pd.concat([df_01, df_03], axis=1)

# %% 
df_03 = pd.DataFrame(data_03).sort_values(['renda','sobrenome'], ascending=True)
df_03

# %%

