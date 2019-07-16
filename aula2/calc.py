#!/usr/bin/python3


#CALCULADORA USANDO FUNCAO
def soma(a,b):
	return a + b
def sub(a,b):
	return a - b
def mult(a,b):
	return a * b
def div(a,b):
	return a / b

operadores = '+-*/'
operacao = input ('Digite: ')

for k in operacao:
	if k in operadores:
		o = k
		a,b = operacao.split(k)
		a = int(a)
		b = int(b)

dic = {'+':soma,'-':sub,'*':mult,'/':div}

z = dic[o](a,b)
print(z)


exit()
#CALCULADORA USANDO IF, ELSE
operadores = '+-*/'
operacao = input ('Digite: ')

for k in operacao:
	if k in operadores:
		a,b = operacao.split(k)
		a = int(a)
		b = int(b)
		o = k	

if o == '+':
	print(a+b)
elif o == '-':
	print(a-b)
elif o == '*':
	print(a*b)
else:
	print(a/b)	

