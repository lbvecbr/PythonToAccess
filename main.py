import pyodbc

conn = pyodbc.connect(r'Driver={Microsoft Access Driver(*.mdb, *.accdb)};DBQ= /home/dimon/Documents/data.mdb;')
cursor = conn.cursor()
