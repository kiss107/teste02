import  sqlite3

conn  =  sqlite3 . conectar ( 'exemplo.db' )
c  =  con . cursor ()

c . execute ( '' 'CREATE TABLE teste(texto de dados, qtde real) '' ' )

c . execute ( '''INSERT INTO teste VALUES ('2020-09-24',10)''')
con . commit ()
con . fechar ()