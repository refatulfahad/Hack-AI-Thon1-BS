from dotenv import load_dotenv
load_dotenv()
import sqlite3
from langchain import OpenAI,SQLDatabase,SQLDatabaseChain
from langchain.document_loaders import TextLoader,DirectoryLoader

dburi='sqlite:///../queryWithDatabase/Chinook_Sqlite.db'
db=SQLDatabase.from_uri(dburi)


llm=OpenAI(temperature=0)
print('executed successfully..')

db_chain=SQLDatabaseChain(llm=llm, database=db, verbose=True)
# db_chain.run('show me total number of employees in this database')
# db_chain.run('Can you provide a list of customers who have made purchases in multiple genres?')
# db_chain.run('Which employee has generated the highest total revenue for the company?')
# db_chain.run('Can you find the top 10 tracks with the highest average rating from customers?')
## db_chain.run('Is there a correlation between the number of tracks in an album and its average rating?')
# db_chain.run('Can you identify any seasonal trends in customer purchases?')
# db_chain.run('How does the average purchase amount vary between different countries?')
## db_chain.run('Can you recommend tracks to customers based on their purchase history and genre preferences?')
# db_chain.run('What is the overall sales distribution across different genres?')
##db_chain.run('select this customers who earn at least 5000')
##db_chain.run('select this customers who earn at least 5000 from customers table')
