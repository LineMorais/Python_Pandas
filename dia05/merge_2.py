#%%
import pandas as pd

df_customers = pd.read_csv("../data/customers.csv", sep=';')
df_customers
# %%
df_transactions = pd.read_excel("../data/transactions.xlsx")
df_transactions

#%%
df_transactions_product = pd.read_parquet('../data/transactions_cart.parquet')
df_transactions_product
# %%
df_join = df_transactions.merge(df_customers, 
                      how='inner', 
                      left_on='IdCustomer', 
                      right_on='UUID',
                      suffixes=['_transacao', '_cliente']
                      )
df_join
# %%
df_join.merge(df_transactions_product,
              how='inner',
              left_on='UUID_transacao',
              right_on='IdTransaction'
              )
df_join.head()

# %%
df_join = (df_transactions.merge(df_customers, 
                                how='inner', 
                                left_on='IdCustomer', 
                                right_on='UUID',
                                suffixes=['_transacao', '_cliente'])
                            .merge(df_transactions_product,
                                how='inner',
                                left_on='UUID_transacao',
                                right_on='IdTransaction'
              ))
df_join.head()
# %%
