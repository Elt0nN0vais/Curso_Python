#!/usr/bin/python3

pot =[]

for valor in range(1,11):
	if valor % 2 == 0:
		pot.append(valor)
print(pot)		



exit()
palavra = input('Digite uma palavra: ')
vogais = 'aeiouAEOIUãàáâéêíôóôú' 

for k in palavra:
	if k in vogais:
		palavra = palavra.replace(k,'*')

print(palavra)

#outra forma de fazer o looping, separacao e substituicao das vogais

#palavra = input('Digite uma palavra: ')
#vogais = 'aeiou'
#troca = '' 

#for k in palavra:
#	if k in vogais:
#		troca += '*'
#	else:
#		troca += k
#print(troca)


exit()
palavra = input('Digite uma palavra: ')

if palavra == palavra[::-1]:
	print('Essa palavra É palindrome')
else:
	print('Essa palavra NAO é palindrome')	