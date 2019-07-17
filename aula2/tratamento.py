#!/usr/bin/python3




arq = 'arquivo.txt'
nomes = ['Robin\n','mulher maravilha\n','Supermman\n']

with open(arq,'a') as arquivo: #'a' append - acresenta os arquivos
	arquivo.writelines(nomes)

with open(arq) as arquivo:
	conteudo = arquivo.read()
	print(conteudo)

cores = {'red':'vermelho', 'blue':'azul', 'green':'verde'}
print(cores['red'])

koppa1 = {'cor':'vermelho', 'pontos':30}
pontos = koppa1 ['pontos']
print(pontos)

koppa1['eixo_x'] = 5
koppa1['eixo_y'] = 15
koppa1['velocidade'] = 'rapido'

print(koppa1)
exit()
with open('arquivo.txt') as arquivo:
	linhas = arquivo.readlines()
print(linhas)	


exit()
with open('arquivo.txt') as arquivo:
	for linha in arquivo:
		print(linha)


exit()
with open('arquivo.txt') as arquivo:
	conteudo = arquivo.read()
	print(conteudo)


# exit()
arquivo = open('arquivo.txt')
print(arquivo.read())
arquivo.close()


exit() #Ok
while True:
	n1 = int(input('Digite: '))
	n2 = int(input('Digite: '))

	try:
		r = n1/n2
	except ZeroDivisionError as e:
		print('Impossível dividir por zero!')
	except	NameError as e:
		print('Variável inexistente')
	except ValueError as e:
		print('Digite somente numeros')	
		break
	else:
		print (r)


exit() #Ok
try:
	print(5/0)
except ZeroDivisionError as e:	
	print('Erro: {}'.format(e))
