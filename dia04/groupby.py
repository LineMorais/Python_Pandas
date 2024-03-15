#%%
import pandas as pd
import numpy as np

# %%
df = pd.read_excel("../data/transactions.xlsx")
df

# %% quantos pontos o usuario tem acumulado

condicao = df['IdCustomer'] == '5f8fcbe0-6014-43f8-8b83-38cf2f4887b3'
df_user = df[condicao]
df_user['Points'].sum()
# %%

pontos = {}
for i in df['IdCustomer'].unique():
    condicao = df['IdCustomer']==i
    pontos[i] = df[condicao]['Points'].sum()

pontos

# %% agrupando e tranformando em dataframe

df_summary = df.groupby(['IdCustomer'])['Points'].sum()
df_summary.reset_index()


# %% quantas transações o usuario teve (RFV)

(df.groupby(['IdCustomer'])
            .agg({'Points': 'sum', 
                  'UUID':'count',
                  'DtTransaction': 'max'}
                )
            .rename(columns= {'Points': 'Valor',
                              'UUID': 'Frequecia',
                              'DtTransacrion': 'UltimaData'}
                    )
            .reset_index()
)

# %% lidar com datahora
import datetime

# %%
data1 = df['DtTransaction'][0]
now = datetime.datetime.now()

(now - data1).days

# %%
df

# %%
condicao = df['IdCustomer'] == '5f8fcbe0-6014-43f8-8b83-38cf2f4887b3'
df_user = df[condicao]
diff = datetime.datetime.now() - df_user['DtTransaction'].max()
diff.days

# %% função de agregação personalizada
def recencia(x):
    diff = datetime.datetime.now() - x.max()
    return diff.days

(df.groupby(['IdCustomer'])
            .agg({'Points': 'sum', 
                  'UUID':'count',
                  'DtTransaction': recencia}
                )
            .rename(columns= {'Points': 'Valor',
                              'UUID': 'Frequecia',
                              'DtTransacrion': 'UltimaData'}
                    )
            .reset_index()
)

# %%
