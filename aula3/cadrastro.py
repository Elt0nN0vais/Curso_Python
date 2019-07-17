#!/usr/bin/python3

#opcao = int(input('Digite a opcao desejada:\n [1] Add\n [2] Buscar\n [0] Sair'))
#print(opcao)


while True:

	opcao = int(input('Digite a opcao desejada:\n [1] Add\n [2] Buscar\n [0] Sair'))
	print(opcao)

	if opcao == 1:
		novo_cpf = int(input('Insira um novo CPF: '))
		novo_cli = int(input('Digite o nome do cliente e seu estado (UF)'))
	elif opcao == 2:
		cad = int(input('Digite um CPF já existente...'))
	elif opcao == 0:
		print('Sair do sistema')
		break
	else:
		print('Opcao invalida.Digite [1] Add, [2] Buscar ou [0] Sair')			








# cad = 'cadrastro.txt'
# cliente = {'000.000.000.00':{'nome':'Bruce','estado':'SP'},
# '111.111.111.11':{'nome':'Clark','estado':'RJ'},
# '222.222.222.22':{'nome':'Flash','estado':'RS'}}

# with open(cad) as cadrastro:
# 	conteudo = cadrastro.read()
# 	print(conteudo)
