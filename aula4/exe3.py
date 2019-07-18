#!/usr/bin/python3

class Conta():
	def __init__(self,titular,numero,saldo):
		self.titular = titular
		self.numero = numero
		self.saldo = saldo

	def descrever(self):
		print(('Titular: {}\nCC: {}\n Saldo: {}\n').format(self.titular,self.numero,self.saldo))

	def saque(self,valor):
		self.saldo -= valor
		return self.saldo

	def deposito(self,valor):
		self.saldo += valor
		return self.saldo

class Poupanca(Conta):
	def __init__(self,titular,numero,saldo):
		super().__init__(titular,numero,saldo)
		self.juros = 1.006

	def descrever(self):
		print(('titular: {}\nPoupanca: {}\n saldo: {}\n').format(self.titular,self.numero,self.saldo))	

	def render(self):
		self.saldo	+= self.juros
		return self.saldo
		
# joao = Conta('joao','123',30000)
# joao.saque(10000)
# joao.descrever()
# joao.deposito(10000)
# joao.descrever()

joao_cc = Conta('joao','111',30000)
maria_cc = Conta('maria','222',2000)
joao_pp = Poupanca('joao','111',100)

joao_cc.transferir(3000,maria_cc)
joao_cc.descrever()
maria_cc.descrever()

joao_cc.transferir(5000,joao_pp)
joao_cc.descrever()
joao_pp.descrever()

joao_pp.render()
joao_pp.descrever()



