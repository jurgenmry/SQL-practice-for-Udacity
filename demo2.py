import psycopg2

cnn =  psycopg2.connect('dbname=example user=postgres password=123')
cursor = cnn.cursor()

#cursor.execute('DROP TABLE IF EXISTS table1;')

cursor.execute('''
    CREATE TABLE table1(
        id INTEGER PRIMARY KEY,
        completed BOOLEAN NOT NULL DEFAULT false
    );
''')

data = {
    'id':2,
    'completed': False,
}

SQL = ('INSERT INTO table1 (id, completed) VALUES (%(id)s, %(completed)s);')


cursor. execute(SQL, data)


cnn.commit()
cnn.close()

cursor.close()
