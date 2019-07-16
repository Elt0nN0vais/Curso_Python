#!/usr/bin/python3

nome = input('Digite nome do aluno: ')
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n3 = float(input('Digite a terceira nota: '))
n4 = float(input('Digite a quarta nota: '))

media = (n1+n2+n3+n4)/4

print(nome + ' teve media ' + str(media))


exit()
nome = input('Digite nome: ')
idade = input('Digite idade: ')

print(nome.title() + ' tem ' + (idade) + ' anos. ')


exit()
a,b = 10,3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)


exit()
nome = 'Joao'
idade = 20
mensagem = nome + ' tem ' + str(idade) + ' anos. '

print(mensagem)


exit()
nome = 'mcdonald\'s\n\t'
sobrenome = 'maddog'
completo = nome.title() + ' ' + sobrenome.title()

print(completo)


exit()
nome = '     maddog      '
print(nome.split())
print(nome.title())
print(nome.upper())
print(nome.lower())
print(nome.lstrip())


exit()
mensagem = 'Ola mundo!'
print(mensagem)

mensagem = 'Bem vindo!'
print(mensagem)
