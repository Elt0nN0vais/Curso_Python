
#importando banco de dados MySQL
import MySQLdb

try:
	con = MySQLdb.connect(host='localhost', db='gotham', user='robin', passwd='Gotham@123')
	print('Conectou')
	cur = con.cursor()
except Exception as e:
	print('Erro: {}'.format(e))

#cur.execute('create table herois(id int auto_increment primary key, nome varchar(50), idade int);')
	
#cur.execute('insert into herois(nome,idade) values (\'batman\',80);')
#cur.execute('insert into herois(nome,idade) values (\'robin\',20);')
#cur.execute('insert into herois(nome,idade) values (\'asa noturna\',30);')

#cur.execute('update herois set nome=\'asa notuna\' where nome=\'asa noturna\';')

#cur.execute('delete from herois where nome=\'asa notuna\';')

cur.execute('select  * from herois;')
print(cur.fetchone()) #traz a primeira posicao
print(cur.fetchall()) #traz todas as ṕosicoes

con.commit()
cur.close()
con.close()


