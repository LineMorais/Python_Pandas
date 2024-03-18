#%%
import pandas as pd
import sqlalchemy as sql

# %%
engine = sql.create_engine('sqlite:///../data/database')

# %%
df_transactions_cart = pd.read_sql_table('transaction')
df_transactions_cart

# %% 
query = 'SELECT * FROM customers as t1
LEFT JOIN transactions AS t2
ON T1.UUID = t2.IdCustomer
LIMIT 10'

#%%
data_01 = {
    "id":[1, 2, 3, 4],
    "nome":["Téo", "Nah", "Lah", "Mah"],
    "idade":[31, 32, 34, 32]
}

df_01 = pd.DataFrame(data_01)

data_02 = {
    "id":[5,6,7,8],
    "nome":["Jose", "Nathan", "Arnaldo", "Mario"],
    "idade":[23, 33, 19, 21]
}
df_02 = pd.DataFrame(data_02)

df_01.to_sql("tb_teste", engine, index=False)

# %%
