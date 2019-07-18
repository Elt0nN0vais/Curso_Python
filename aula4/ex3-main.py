#!/usr/bin/python3

from ex3 import Conta as CC
from ex3 import Poupanca as CP

def main():
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

if __name__ == '__main__':
	main()