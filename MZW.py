#!/usr/bin/python

from __future__ import division
import numpy as np 
import math
from sympy import Symbol, nsolve, linsolve, solve
import sympy
import mpmath

#miejsca zerower wielomaniu Legendre'a
def MZL(n):
	if n == 3:
		p = [231/16, 0, -315/16, 0, 105/16, 0, -5/16]

	elif n == 4: 
		p = [6435/128, 0, -12012/128, 0, 6930/128, 0, -1260/128, 0, 35/128]
	else:
		print("Zle n")

	y = np.roots(p)


	return y

#wagi miejsc zerowych w postaci wspolczynnikow a
def WA(n):
	p = [8]
	a1 = Symbol('a1')
	a2 = Symbol('a2')
	a3 = Symbol('a3')	
	a4 = Symbol('a4')
	if n==3:
		p = MZL(n)
		f1 = a1 + a2 + a3 - 1
		f2 = a1 * p[2]**2 + a2 * p[3]**2 + a3 * p[5]**2 - 1 / 3
		f3 = a1 * p[2]**4 + a2 * p[3]**4 + a3 * p[5]**4 - 1 / 5
		y, = linsolve((f1, f2, f3), a1, a2, a3)
	elif n==4:
		p = MZL(n)
		f1 = a1 + a2 + a3 + a4 - 1
		f2 = a1 * p[2]**2 + a2 * p[3]**2 + a3 * p[5]**2 + a4 * p[7]**2 - 1 / 3
		f3 = a1 * p[2]**4 + a2 * p[3]**4 + a3 * p[5]**4 + a4 * p[7]**4 - 1 / 5
		f4 = a1 * p[2]**6 + a2 * p[3]**6 + a3 * p[5]**6 + a4 * p[7]**6 - 1 / 7
		y, = linsolve((f1, f2, f3, f4), a1, a2, a3, a4)
	else:
		print('Zle n w funkcji WA')
	return y

#wyznaczanie k w wielomianie W(k)
def SK(n):
	k=Symbol('k')
	mi=MZL(n)
	a=WA(n)
	if n==3:
		output.write("\nMiejsca zerowe wielomianu Legendre'a o n=" + str(n) + ':  ' + str(mi[2]) + ' , ' +  str(mi[3]) + ' , ' + str(mi[5]))
		output.write("\nWagi miejsc zerowych 'a' dla n="+ str(n) + ':  ' + str(a))
		y = solve(1-a[0]/(1-k**2*mi[2]**2)-a[1]/(1-k**2*mi[3]**2)-a[2]/(1-k**2*mi[5]**2), k)
		output.write("\nMiejsca zerowe wielomianu W(k): " + str(y))
	elif n==4:
		output.write("\nMiejsca zerowe wielomianu Legendre'a o n=" + str(n) + ':  ' + str(mi[2]) + ' , ' +  str(mi[3]) + ' , ' + str(mi[5]) + ' , ' + str(mi[7]))
		output.write("\nWagi miejsc zerowych 'a' dla n="+ str(n) + ':  ' + str(a))
		y = solve(1-a[0]/(1-k**2*mi[2]**2)-a[1]/(1-k**2*mi[3]**2)-a[2]/(1-k**2*mi[5]**2)-a[3]/(1-k**2*mi[7]**2), k)
		y[6] = 0
		y[7] = 0
		output.write("\nMiejsca zerowe wielomianu W(k): " + str(y))

	else:
		print('Zle n w funkcji SK')
	

output = open("atm_szar_a.dat", 'w')
output.write('------------------------n==3---------------------------')
SK(3)

#output.write(SK(3))
output.write('\n\n------------------------n==4---------------------------')
#output.write(SK(4))
SK(4)
output.close()

#output = open("P6.dat", 'w')
#for n in range (1, 10000001):
#	k = n/10000000
#	mi = [0.2368, 0.6612, 0.924]
#	a = [0.4679, 0.3608, 0.1713]
#	b = [1-k**2*mi[0]**2, 1-k**2*mi[1]**2, 1-k**2*mi[2]**2]
#	W = 1 - a[0] / b[0] - a[1] / b[1] - a[2] / b[2]
#	print(str(y))
#	if abs(W) < 0.00000000001:
#		m+=1
#		print('k = ' + str(m) + ' = ' + str(k))
#		output.write('mi=' + str(a) + '=' + str(x))


#output.close()