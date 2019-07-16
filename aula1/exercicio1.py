#!/usr/bin/python3

nome = input('Digite nome do aluno: ')

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n3 = float(input('Digite a terceira nota: '))
n4 = float(input('Digite a quarta nota: '))

media = (n1+n2+n3+n4)/4

if media > 7:
	print('Aluno aprovado')
elif media >= 5 and media <= 7:
	print('Necessario fazer nova prova...')
	n5 = float(input('Digite a nova nota: '))
	novamedia = (media+n5)/2
	if novamedia >= 5:
		print('Aluno aprovado')
	else:
		print('Aluno reprovado')
else:
	print('Aluno reprovado')




#print(nome + ' teve media ' + str(media))