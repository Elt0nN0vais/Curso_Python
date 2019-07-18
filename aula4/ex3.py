#!/usr/bin/python3

class Ccorrente():
	def __init__(self,nome,saldo):
		self.nome = nome
		self.saldo = saldo

	def saldo_atual(self):
		print('{} seu saldo atual é: R$  {}'.format(self.nome,self.saldo,))

	#def saque(self):
		


	# def transferencia(self):
	# 	saldoJoao = self.saldo - 3000
	# 	saldoMaria = self.saldo + 3000
	# 	print('{} seu saldo atual é: R$  {}'.format(self.nome,self.saldo,))

primeiro = Ccorrente('Joao',30000)
segundo = Ccorrente('Maria',2000)

	# def status(self):
	# 	if self.aberto == True:
	# 		print('{} está aberto'.format(self.nome))
	# 	else:
	# 		print('{} está fechado'.format(self.nome))


#terceiro = Restaurante('Marianas','brasileira',True)

primeiro.saldo_atual()
segundo.saldo_atual()

