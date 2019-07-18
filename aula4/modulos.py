#!/usr/bin/python3

import time,random
from datetime import datetime
from subprocess import run,PIPE
from pasta.som import qual_nota

b = False

while b == False:
	f = random.randint(264,528)
	b = qual_nota(f)



exit()
#r = run(['apt','install','-y','sl'],stdout=PIPE,stderr=PIPE)
#print(r)

#r = run(['ls','l'],stdout=PIPE,stderr=PIPE)
#print(r)

#if r.returncode != 0:
#	print('deu ruim')
#else:
#	print('OK')


#ESCOLHER UM NUMERO ALEATORIO ENTE 100 E 999
# k = 0
# while k != 505:
# 	k = random.randint(100,999)
# 	print(k)


#VOGAIS ALEATORIAS
vogais = 'aeiouAEIOU'
print(random.choice(vogais))
time.sleep(2)
print(random.choice(vogais))

 