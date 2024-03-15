# %% 
import pandas as pd
# %%
df = pd.read_excel("../data/transactions.xlsx")

# %%
df_last = (df.sort_values('DtTransaction', ascending=False)
            .drop_duplicates)