import pandas as pd
import numpy as np
from datetime import date


today = str(date.today())
df_branch_service = pd.read_json("C:\Users\juanc\OneDrive\Documents\School\DataWarehousing\Labex3\KyleFile\branch_service_transaction_info.json")
df_customer_transaction = pd.read_json("C:\Users\juanc\OneDrive\Documents\School\DataWarehousing\Labex3\KyleFile\customer_transaction_info.json")
print("Succesfully loaded the data")

df_branch_service = df_branch_service.drop_duplicates(subset=['txn_id'])
df_customer_transaction = df_customer_transaction.drop_duplicates(subset=['txn_id'])
print("Dropping the duplicates")

##Saving data
df_