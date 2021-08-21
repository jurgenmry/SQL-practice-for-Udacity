import psycopg2

cnn =  psycopg2.connect('dbname=exmaple user=postgres password=123')
cursor = cnn.cursor()

cursor.execute('DROP TABLE IF EXIST example;')

cursor. execute('''
    CREATE TABLE table1(
        id INTEGER PRIMARY KEY,
        completed BOOLEAN NOT NULL DEFAULT false
    );
''')

data = {
    'id':1,
    'completed': True,
}

SQL = ('INSERT INTO table1 (id, completed) VALUES (%(id)s, %(completed)s);')


cursor. execute(SQL, data)


cnn.commit()
cnn.close()

cursor.close()
