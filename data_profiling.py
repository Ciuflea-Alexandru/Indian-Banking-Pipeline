from logger import log
import pandas as pd
from sqlalchemy import create_engine

logger = log()

# Ensure all columns are visible in logs
pd.set_option('display.max_columns', None)
pd.set_option("display.width", 10000)

logger.info('Retrieving Data...')
df = pd.read_csv('/home/alex/Project/Indian-Banking-Pipeline/banking_dataset.csv')

logger.info('')
logger.info(f'Printing original table: \n{str(df.info)}')

logger.info('')
logger.info(f'Running Diagnostics: '
            f'\n Amount of null instances: \n{str(df.isnull().sum())}'
            f'\n General information: \n{str(df.describe())}')
