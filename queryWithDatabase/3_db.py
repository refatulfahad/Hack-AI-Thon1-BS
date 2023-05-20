# ## Convert CSV to DB

# import sqlite3
# import pandas as pd
# # Load data file
# df=pd.read_csv('AI.csv')
# # data clean up
# df.columns=df.columns.str.strip()
# #create/connect to a sqlite database
# connection=sqlite3.connect('AI.db')
# #load data file to sqlite
# df.to_sql('Informations',connection,if_exists='replace')
# #close connection
# connection.close()
# query execute
# c=connection.cursor()
# c.execute("ALTER TABLE Informations RENAME COLUMN `index` TO Id;")
# print('command executed successfully...')
# connection.commit()
# connection.close()

# query with database
# from pydantic import ValidationError
from dotenv import load_dotenv
load_dotenv()
from langchain import OpenAI,SQLDatabase,SQLDatabaseChain

dburi='sqlite:///../queryWithDatabase/AI.db'
db=SQLDatabase.from_uri(dburi)

llm=OpenAI(temperature=0)
print('executed successfully..')

db_chain=SQLDatabaseChain(llm=llm, database=db, verbose=True)

db_chain.run("how many rows in this db?")
db_chain.run('what is the first question?')
db_chain.run('When the first neural network is built?')
db_chain.run('what is the most important question among those questions?')
db_chain.run('what is the less important question among those questions?')
db_chain.run('BFS space complexity')
db_chain.run('explain dfs algorithm')
db_chain.run('explain bfs algorithm')
db_chain.run('What is the first neural network called?')