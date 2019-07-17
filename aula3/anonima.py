#!/usr/bin/python3

temp = [21,32,50,10,15]
print(temp)

f = list(map(lambda t: float(9/5) * t + 32,temp))
c = list(map(lambda t: float(5/9) * (t - 32),f))

print('F: {}\nC: {}'.format(f,c))


exit()
def farenheit(t):
	return float(9/5) * (n -32)

def celsius(t):
	return  (9/5) * (n + 32)

temp = [21,32,50,10,15]
print(temp)

f = list(map(farenheit, temp))
c = list(map(celsius, temp))


print('F: {}\nC: {}'.format(f,c))


# def dobro(n):
# 	return 2 * n

# num = (1,2,3,4,5)
# r = list(map(dobro,num))
# print(r)


exit()
def quadrado(n):
	return n ** 2

def raiz(n):
	return n ** (0.5)

f  = [quadrado,raiz]

for k in range(0,26):
	valores = list(map(lambda x : x(k), f))
	print(valores)	

print('\n')
[print(list(map(lambda x : x(k),f))) for k in range(0,26)]		


exit()
n1 = [1,2,3]
n2 = [4,5,6]

r = list(map(lambda x,y : x * y, n1,n2))
print(r)


exit()
num = (1,2,3,4,5)
r = list(map(lambda n : 2 * n, num))
print(r)


exit()
#funcao map, capaz de utilizar modulos (bibliotecas) com outras funcoes
import math

l1 = [1,4,9,16,25]
l2 = list(map(math.sqrt, l1))#funcao map só funciona com 'list'

print(l2)


exit()
def dobro(n):
	return 2 * n

num = (1,2,3,4,5)
r = list(map(dobro,num))
print(r)


exit()
#CALCULADORA COM FUNCAO ANONIMA
calcula = {'+':lambda x,y : x + y,
			'-':lambda x,y : x - y,
			'*':lambda x,y : x * y,
			'/':lambda x,y : x / y
			}

operadores = '+-*/'
operacao = input('Digite: ')

for k in operacao:
	if k in operadores:
		o = k
		a,b = operacao.split(k)
		a = int(a)
		b = int (b)

print(calcula[o](a,b))		


exit()
#exemplo2
tamanho = lambda frase : [len(palavra) for palavra in frase]
frase = 'joao foi para a escola'.split()
print(frase)
print(tamanho(frase))


#exemplo1
def tamanho(frase):
	return [len(palavra) for palavra in frase]
frase = 'joao foi para a escola'.split()
print(frase)
print(tamanho(frase))


exit()
def multiplica(n):
	return lambda a : a * n
dobro = multiplica(2)
triplo = multiplica(3)

print(dobro(12))
print(triplo(12))


exit()
#FUNCAO ANONIMA
x = lambda a, b : a + b #a,b, passagem de parametros 
a = x(5,3)
print(a)