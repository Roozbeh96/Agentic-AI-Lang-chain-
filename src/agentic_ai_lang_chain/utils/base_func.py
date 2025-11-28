import pandas as pd
from sqlalchemy import create_engine
import os


def read_transform(*, file_path:str) -> pd.DataFrame:
    if 'online_retail_database.db' in os.listdir(file_path):
        return create_engine('sqlite:///data/online_retail_database.db')
    else:
        print('Starting to read and transform the data...')
        file_path = os.path.join(file_path, 'online_retail_II.xlsx')
        df = pd.read_excel(file_path, sheet_name = None)
        df = pd.concat(df.values(), ignore_index=True)

        engine = create_engine('sqlite:///data/online_retail_database.db')
        df.to_sql('online_retail_table', con=engine, if_exists='replace', index=False)
        
        print('Transformation complete.')
        return engine