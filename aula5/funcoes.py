


def cria_tabela():
	cur.execute('create table usuarios(id int auto_increment primary key, nome varchar(50), cpf int, estado char);')
	print('Tabela criada')

def drop_tabela():
	cur.execute('drop table usuarios')
	print('Tabela dropada')

def busca():
	nome = input('Digite nome: ')
	cur.execute('select * from usuarios where nome=\'{}\';'.format(nome))
	tuplas = cur.fetchall()

	for k in tuplas:
		print('{}'.format(k))

def cadastro():
	nome = input('Digite nome: ')
	cpf = int(input('Digite cpf: '))
	estado = input('Digite estado: ')

	query = 'select * from usuayrios where cpf={}'.format(cpf)

	if cur.execute(query):
		print('Cadastro existente')
	else:
		cur.execute('insert into usuarios(nome,cpf,estado)values(\'{}\'{}\'{}');')	
		con.commit()

def atualizacao():
	while True:
		uid = int(input('uid '))

	print('1 - nome\n2 - cpf\n3 - estado')
	o = int(input('Digite: '))

	if o == 1:
		nome = input('Digite nome: ')
		cur.execute('update usuarios set nome=\'{}\' where id={};'.format(nome,uid))

	elif o == 2:
		cpf = input('Digite cpf: ')
		cur.execute('update usuarios set cpf=\'{}\' where id={};'.format(cpf,uid))

	else:
		estado = input('Digite estado: ')
		cur.execute('update usuarios set estado=\'{}\' where id={};'.format(estado,uid))
	con.commit()

def delecao():
	while True:
		uid = int(input('uid '))

	cur.execute('delete from usuarios where id={}'.format(uid))
	con.commit	

def sair():	
	print('Saindo do sistema')
	exit()