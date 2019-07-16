#!/usr/bin/python3




nome = input('Digite nome do aluno: ')
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n3 = float(input('Digite a terceira nota: '))
n4 = float(input('Digite a quarta nota: '))

media = (n1+n2+n3+n4)/4

print(nome.title() + ' teve media ' + str(media))


exit() #Ok
nome = input('Digite nome: ')
idade = input('Digite idade: ')

print(nome.title() + ' tem ' + (idade) + ' anos. ')


exit() #Ok
a,b = 10,3
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)


exit() #Ok
nome = 'Joao'
idade = 20
mensagem = nome + ' tem ' + str(idade) + ' anos. '

print(mensagem)


exit() #Ok
nome = 'mcdonald\'s\n\t'
sobrenome = 'maddog'
completo = nome.title() + ' ' + sobrenome.title() #exibe a primeira da variável letra Maiscula

print(completo)


exit() #Ok
nome = '     maddog      '
print(nome.split()) #exibe o nome em forma de lista
print(nome.title()) #exibe a primeira letra Maiscula
print(nome.upper()) #exibe todas as letras MAIUSCULAS
print(nome.lower()) #exibe todas as letras minusculas
print(nome.lstrip()) #anula os espaços à esquerda
print(nome.rstrip()) #anula os espaços à direita


exit() #Ok
mensagem = 'Ola mundo!'
print(mensagem)

mensagem = 'Bem vindo!'
print(mensagem)
