from sqlalchemy import create_engine
import pandas as pd
import os

os.chdir('./')
data = pd.read_csv('./Health_Nutritions _databases/food.csv', encoding="ISO-8859-1")
engine = create_engine('sqlite:///:memory:')
data.to_sql('data_table', engine)
print(pd.read_sql_query('SELECT * FROM data_table', engine))