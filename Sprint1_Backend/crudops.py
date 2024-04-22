import mysql.connector
import creds

from mysql.connector import Error
from sql import create_connection
from sql import execute_query
from sql import execute_read_query

#create connection to mysql database
myCreds = creds.Creds() # getting from creds.py file
connection = create_connection(myCreds.connectionstring, myCreds.username, myCreds.passwd, myCreds.dataBase)

