#!/usr/bin/python3

#inserindo parametros diretamento no terminal utilizando o espaço
import sys

print(sys.argv)

for k in range(len(sys.argv)):
	print('parametro {}: {}'.format(k,sys.argv[k]))


exit()
def descobre_dic(**kwargs): #**kwagrsdescobre dicionarios
	print(kwargs)

	for k in kwargs.keys():
		print('Chave: {}'.format(k))
		print('Valor: {}'.format(kwargs[k]))

descobre_dic(nome='servidor',ip='192.168.16.1',dominio='4linux.com.br')
print("\n")	
descobre_dic(user='joazinho',nome='joao',sobrenome='silva',idade='20')


exit()
def calcular_fig_geometrica(*args): #*args descobre listas
	if len(args) == 1:
		print('Area do quadrado: {}'.format(args[0]**2))
	elif len(args) == 2:
		print('Area do retangulo: {}'.format(args[0]*args[1]))
	else:
		print('Volume: {}'.format(args[0]*args[1]*args[2]))	

calcular_fig_geometrica(2)
calcular_fig_geometrica(2,10)
calcular_fig_geometrica(2,10,10)


exit() #Ok
#passando 2 parametros dentro de uma funcao
def animal(tipo='cachorro',nome='rex'):
	print('Eu tenho um {} que se chama {}'.format(tipo,nome))
animal()

#outra forma de passar 2 parametros dentro de uma funcao
def animal(tipo,nome):
	print('Eu tenho um {} que se chama {}'.format(tipo,nome))

animal('cachorro','Rex')

exit() #Ok
#PASSANDO UMA FUNCAO PARA DENTRO DE OUTRA FUNCAO
def diga_ola(n):
	print('Olá ' + n)

def pergunta():
	nome = input('Digite nome: ')
	return nome

x = pergunta()
diga_ola(x)	


exit() #OK
#FUNCAO
def diga_ola():
	print('ola')

diga_ola()

#Ok
