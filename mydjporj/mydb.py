import mysql.connector

config = {'host' : 'localhost',
              'user' : 'root',
              'password' : 'Arulezhil@71',
              'database' : 'django'}

conn = mysql.connector.connect(**config)

cursor = conn.cursor()
print('All Done!')