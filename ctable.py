import psycopg2
#conexão com o banco de dados
conn = psycopg2.connect(database = "postgres", user = "postgres", password = "senha123", host = "127.0.0.1", port = "5432")
print("Conexão com o Banco de Dados aberta com sucesso!")
cur = conn.cursor()
cur.execute('''CREATE TABLE Agenda(ID INT PRIMARY KEY NOT NULL,Nome TEXT NOT NULL,Telefone CHAR(12));''')
print("Tabela criada com sucesso!")
conn.commit()
conn.close()
#Inserção de dados na tabela
cur.execute("""INSERT INTO public."AGENDA" ("id", "nome" , "telefone" ) VALUES (1, 'Pessoa 1' , '02199999999' )""") 
conn.commit() 
print("Inserção realizada com sucesso!"); 8conn.close()
#Seleção dos dadso inseridos
cur.execute("""select * from public."AGENDA" where "id"=1""") 
registro=cur.fetchone() 
print(registro) 8 conn.commit() 9 print("Seleção realizada com sucesso!"); 
conn.close()
