#!/usr/bin/python3

class Carro():
	def __init__(self,marca,modelo,ano):
		self.marca = marca
		self.modelo = modelo
		self.ano = ano
		self.hodometro = 0

	def descrever(self):
		print('{} {} {}'.format(self.marca,self.modelo,self.ano))

	def ler_hodometro(self):
		print('Este caroo rodou {} Km'.format(self.hodometro))

	def atualiza_hodometro(self,kms):
		if kms >= self.hodometro:
			self.hodometro = kms
		else:
			print('Não é possivel diminuir Km')

	def incrementa_hodometro(self,kms):
		if kms >= 0:
			self.hodometro += kms
		else:
			print('Não é possivel diminuir Km')

meu_carro = Carro('VW','fusca','1980')
meu_carro.descrever()
meu_carro.atualiza_hodometro(30000)
meu_carro.ler_hodometro()
meu_carro.incrementa_hodometro(100)
meu_carro.ler_hodometro()





exit() #OK
class Restaurante():
	""" DOCSTRING FOR CLASS NAME"""
	def __init__(self,nome,tipo,aberto):
		self.nome = nome
		self.tipo = tipo
		self.aberto = aberto

	def descrever(self):
		print('{} é um restaurante de comida {} e está {}'.format(self.nome,self.tipo,self.aberto))

	def status(self):
		if self.aberto == True:
			print('{} está aberto'.format(self.nome))
		else:
			print('{} está fechado'.format(self.nome))

primeiro = Restaurante('Mcdonalds','fast food',True)
segundo = Restaurante('Outback','australiana',False)
terceiro = Restaurante('Marianas','brasileira',True)

primeiro.descrever()
segundo.descrever()
terceiro.descrever()

primeiro.status()
segundo.status()
terceiro.status()





exit() #OK
class Saudacao():
	"""descricao"""
	usuario = None

	def __init__(self,nome,sobrenome):
		self.nome = nome
		self.sobrenome = sobrenome

	def descrever(self):
		print('Sobrenome: {}'.format(self.sobrenome))
		
	def saudar(self):
		print('\n{} {} bom dia'.format(self.nome,self.sobrenome))


	
meu_usuario = Saudacao('Elton','Novais')
meu_usuario.dono = 'Elton'
print('Usuario: {}'.format(meu_usuario.dono))
meu_usuario.descrever()
meu_usuario.saudar()





exit() #OK
class Cachorro():
	"""descricao"""
	dono = None

	def __init__(self,nome,idade):
		self.nome = nome
		self.idade = idade

	def descrever(self):
		print('{}\nIdade: {}'.format(self.nome,self.idade))
		
	def sentar(self):
		print('{} esta sentado'.format(self.nome))

	def rolar(self):
		print('{} esta rolando de um lado para outro'.format(self.nome))

meu_cachorro = Cachorro('Jake',2)
print('O dono é {}'.format(meu_cachorro.dono))

meu_cachorro.dono = 'Joao'
print('O dono é {}'.format(meu_cachorro.dono))

meu_cachorro.descrever()
meu_cachorro.sentar()
meu_cachorro.rolar()

