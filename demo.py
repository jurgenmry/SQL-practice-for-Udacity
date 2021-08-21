import psycopg2

cnn = psycopg2.connect("dbname=example user=postgres password=123") #, user="postgres", password="123")

cursor = cnn.cursor()

cursor.execute('''
    CREATE TABLE table1 (
    id INTEGER PRIMARY KEY,
    completed BOOLEAN NOT NULL DEFAULT false
    );
'''
)

cursor.execute('INSERT INTO table1 (id, completed) VALUES (1,true);')

cnn.commit()

cnn.close()
cursor.close()
