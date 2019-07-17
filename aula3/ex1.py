#!/usr/bin/python3

arq = 'arquivo.txt' #cria um arquivo .txt
	
def cadastrar(**kwargs): 
	with open(arq,'a') as arquivo: #abrindo e adicionando no arquivo.txt
		arquivo.write('{}\t{}\t{}\n'.format(kwargs['cpf'],kwargs['nome'],kwargs['estado'])) #escrevendo o arquivo com info recebidas do dicionario
	print('Cadastro adicionado com sucesso!')	

def busca(cpf):
	dic = {}
	k = 0
	chaved = ['cpf','estado','nome']
	with open(arq,'r') as arquivo:
		for linha in arquivo:
			itens = linha.split('\t')
			itens[-1] = itens[-1][:-1]

			# #print(itens)

			# for m in itens:
			# 	dic[chaved[k]] = m
			# 	k += 1
			# 	if k == 3:
			# 		k = 0

			# if dic[chaved[0]] == cpf:
			# 	print('{}\t{}\t{}\n'.format(dic['cpf'],dic['estado'],dic['nome']))
			# 	return dic
			if itens[0] == str(cpf):
				print('{}\t{}\t{}\n'.format(itens[0],itens[1],itens[2]))
				break

		else:
				print('não encontrado')			

while True:
	opt = int(input('Opçoes:\n\n0 - Sair\n1 - Cadastrar\n2 - Buscar\n\n'))
	if opt == 0: 
		break
		#ou exit()
	elif opt == 1: 
		lista = input('\nDigite o Nome,Estado,cpf: ').split(',') #recebendo 3 informacoes em um unico input e quebrando com slipt com (,)
		cadastrar(nome=lista[0],estado=lista[1],cpf=lista[2]) #criando um dicionario com chaves e valores
	else:
		cpf = input('Digite cpf: ')
		busca(cpf) 


