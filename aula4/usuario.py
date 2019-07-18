#!/usr/bin/python3





class Carro():
	def __init__(self,marca,modelo,ano):
		self.marca = marca
		self.modelo = modelo
		self.ano = ano
		self.hodometro = 0
		self.gasolina = 0

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

	def enche_tanque(self):
		self.gasolina = 100
		print('Gasolina: {}'.format(self.gasolina))


class Bateria():

	def __init__(self,bateria):
		self.bateria = bateria

	def descrever_bateria(self):
		print('Bateria : {}'.format(self.bateria))

	def calculo_distancia(self):
		calculo = self.bateria * 2
		print(('Estee carro possui {} km/h de bateria').format(calculo))


class Eletrico(Carro):

	def __init__(self,marca,modelo,ano):
		super().__init__(marca,modelo,ano)
		self.bateria = Bateria(100)

	def enche_tanque(self):
		print('esse carrro é eletrico')


c1 = Carro('VW','fusca','1980')		
c2 = Eletrico('tesla','model s','2016')

c2.bateria.descrever_bateria()
c2.bateria.calculo_distancia()

print('c1: {}'.format(c1.gasolina))
c1.enche_tanque()
print('c1: {}'.format(c1.gasolina))

# c2.descrever_bateria()
# print('c2: {}'.format(c2.gasolina))
# c2.enche_tanque()
# print('c2: {}'.format(c2.gasolina))

meu_carro = Carro('VW','fusca','1980')
# meu_carro.descrever()
# meu_carro.atualiza_hodometro(30000)
# meu_carro.ler_hodometro()
# meu_carro.incrementa_hodometro(100)
# meu_carro.ler_hodometro()




exit() #OK
class User():
	"""descricao"""
	#usuario = None

	def __init__(self,nome,sobrenome,username,senha):
		self.nome = nome
		self.sobrenome = sobrenome
		self.username = username
		self.senha = senha
		self.tentativas = 0


	def descrever(self):
		print('{} {}'.format(self.nome,self.sobrenome))
		
	def saudar(self):
		print('Olá {} {}'.format(self.nome,self.sobrenome))

	def reseta_tentativas(self):
		self.tentativas = 0
		print('Tentativas: {}'.format(self.tentativas))
		
	def incrementa_tentativas(self):
		self.tentativas += 1
		print('Tentativas {}'.format(self.tentativas)) 

	def login(self,username,senha):
		if username == self.username and senha == self.senha:
			print('Usuario logado com sucesso')
			self.reseta_tentativas()
		else: 
				#print('Login incorreto. Tente novamente')	
			self.incrementa_tentativas()

batman = User('Bruce','Waine','batman','123')

while True:
	user = input('Digite seu usuario :')
	senha = input('Digite sua senha :')

	batman.login(user,senha)


