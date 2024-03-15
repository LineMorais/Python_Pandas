#%% 
import pandas as pd

# %%
idades = [30, 42, 90, 34]
idades
# %% média
media = sum(idades) / len(idades)

total = 0
for i in idades:
    total += (media - i)**2

variancia = total /(len(idades)-1)

media, variancia
# %% tranformando lista em serie e atribuindo em uma variavel nova

series_idades = pd.Series(idades)
series_idades

# %% metodos da serie padas
# media

series_idades.mean()

# %% variancia | Desvio padrão

series_idades.var()
series_idades.std()
# %% mediana | Quartil

series_idades.median()
series_idades.quantile(0.75)
# %% Sumarização

series_idades.describe()

# %% atribuitos | dimensão da serie | tupa que me diz quantas series minha linha tem

series_idades.shape

# %% navegando na lista

idades[0]
#%% navegando na serie
series_idades[3]
# %%
series_idades.index
# %% alterando index da serie
series_idades.index = ['t', 'e', 'o', 'c']
# %% navegando nos indices
series_idades['o']
# %%
series_idades[2]
# %% pegando pela posição

series_idades.iloc[2:4]

# %% pegando pela posição 

series_idades.iloc[0:2]
# %% pegando o valor atrelado pelo indice
series_idades.loc[0]

#%% colocando o nome na serie.
series_idades.name = 'idades'
series_idades

# %% colocando o nome na serie quando já está sendo criada
series_idades = pd.Series(idades, name="idades")
series_idades

# %%

