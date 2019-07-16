#!/usr/bin/python3

#Abaixo de 200 minutos cobra R$ 0.20 por min.
#Entre 200 e 400 minutos cobra R$ 0.18
#Acima de 400 minutos o preço é R$ 0.15

minutos = int(input('Minutos utilizados: '))
if minutos < 200:
	preco = 0.2
elif minutos <= 400:
	preco = 0.18
else:
	preco = 0.15



exit()
idade = int(input('Digite idade: '))
habilitacao = input('Possui habilitacao: ')
h = False

if habilitacao.lower().strip() == 'sim':
	h = True
if idade >= 18 and h == True:
	print('Pode dirigir')
else:
	print('Não pode dirigir')


exit()
velocidade = int(input('Informe vel.: '))

if velocidade > 110:
	multa = (velocidade -110) * 5
	print('multa: R$  {:.2f}'. format(multa))