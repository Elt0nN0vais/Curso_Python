#!/usr/bin/python3


#exemplo de dicionario dentro de dicionário
herois = {'batman':{'identidade':'bruce waine','cidadde':'gottham'},
'superman':{'identidade':'clark kent','cidade':'metroplolis'}}

print(herois['batman']['identidade'])


#exemplo de lista dentro de dicionario
exit() #OK
lanche = {'pão':['integral','4 queijos','italiano'],'queijo':['prato','cheddar','suiço'],'recheio':['frango','carne','almondega']}
print(lanche['pão'][2])


exit()
koppa1 = {'cor':'vermelho', 'pontos':30}
koppa2 = {'cor':'verde', 'pontos':50}
koppa3 = {'cor':'azul', 'pontos':100}

koppa = [koppa1, koppa2, koppa3]
print(koppa[1]['cor'])

lista = []

for k in range(10):
	lista.append(koppa1)

print(lista)	

exit()
usuario = {'username':'exemplo', 'nome':'joao', 'sobrenome':'silva'}
print(usuario)

for chave,valor in usuario.items():
	print('chave: {}'.format(chave)) #imprime chaves 'nome''sobrenome''userneme
	print('valor: {}'.format(valor)) #imprime valores 'exemplo''joao''silva'

for chave in usuario.keys():
	print('chave: {}'.format(chave)) #imprime chaves 'nome''sobrenome''userneme

for valor in usuario.values():
	print('valor: {}'.format(valor)) #imprime valores 'exemplo''joao''silva'	

#OK
exit()

cores = {'red':'vermelho', 'blue':'azul', 'green':'verde'}
print(cores['red'])

koppa1 = {'cor':'vermelho', 'pontos':30}
pontos = koppa1 ['pontos']
print(pontos)

koppa1['eixo_x'] = 5
koppa1['eixo_y'] = 15
koppa1['velocidade'] = 'rapido'

print(koppa1)

if koppa1['velocidade'] == 'lento':
	anda_x = 1
elif koppa1['velocidade'] == 'médio':
	anda_x = 2
else:	
	anda_x = 3
print(koppa1)


exit()
retangulo = (100,50)
print(retangulo[0], retangulo[1])

retangulo = (30,50)
print(retangulo[0], retangulo[1])

x = list(retangulo)
x[0] = 300
print(x)


exit()
pot = []

for valor in range(1,11):
	if valor % 2 == 0:
		pot.append(valor)
print(pot)	


#outra forma: 

#pot = [valor for valor in range(1,11) if valor % 2 == 0]
#print(pot)