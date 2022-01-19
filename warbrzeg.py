#!/usr/bin/python

from __future__ import division
import numpy as np 
import math
from sympy import Symbol, nsolve, linsolve, solve
import sympy
import mpmath

output = open("atm_szar_b.dat", 'w')

#warunki brzegowe
def WB(n):
	p = [4]
	k = [3]
	Q = Symbol('Q')
	L1 = Symbol('L1')
	L2 = Symbol('L2')
	L3 = Symbol('L3')	
	L4 = Symbol('L4')
	if n==3:
		p = [0.932469514203 , 0.661209386466 , 0.238619186083]
		k = [0 , 1.22521088034294 , 3.20294525377648] 
		f1 = -p[0] + Q + L1 / ( 1 - k[1] * p[0] ) + L2 / ( 1 - k[2] * p[0] ) 
		f2 = -p[1] + Q + L1 / ( 1 - k[1] * p[1] ) + L2 / ( 1 - k[2] * p[1] ) 
		f3 = -p[2] + Q + L1 / ( 1 - k[1] * p[2] ) + L2 / ( 1 - k[2] * p[2] ) 
		y, = linsolve((f1, f2, f3), Q, L1, L2)
		output.write('\n------------------------n==3---------------------------')
		output.write('\nQ = '+  str(y[0]) +', L1 = ' + str(y[1]) + ', L2 = '+ str(y[2]))
		output.write('\nI_i (t, p_i) = 3F / 4pi * (t + ' + str(y[0]) + ' + p_i + (' + str(y[1]) + ' * exp(-' + str(k[1]) + ' * t) ) / (1 - ' + str(k[1]) + ' * p_i) + (' + str(y[2]) + ' * exp(-' + str(k[2]) + ' * t) ) / (1 - ' + str(k[2]) + ' * p_i)')
		output.write('\nS (t) = J(t) = 3F / 4pi * (t + ' + str(y[0]) + ' + (' + str(y[1]) + ' * exp(- ' + str(k[1]) + ' * t)) + (' + str(y[2]) + ' * exp(- ' + str(k[2]) + ' * t))')
	elif n==4:
		p = [0.960289856498 , 0.796666477414 , 0.525532409916 , 0.183434642496]
		k = [0.0 , 1.10318532050959 , 1.59177887606493 , 4.45808571931660] 
		f1 = -p[0] + Q + L1 / ( 1 - k[1] * p[0] ) + L2 / ( 1 - k[2] * p[0] ) + L3 / ( 1 - k[3] * p[0] ) 
		f2 = -p[1] + Q + L1 / ( 1 - k[1] * p[1] ) + L2 / ( 1 - k[2] * p[1] ) + L3 / ( 1 - k[3] * p[1] ) 
		f3 = -p[2] + Q + L1 / ( 1 - k[1] * p[2] ) + L2 / ( 1 - k[2] * p[2] ) + L3 / ( 1 - k[3] * p[2] ) 
		f4 = -p[3] + Q + L1 / ( 1 - k[1] * p[3] ) + L2 / ( 1 - k[2] * p[3] ) + L3 / ( 1 - k[3] * p[3] ) 
		y, = linsolve((f1, f2, f3, f4), Q, L1, L2, L3)
		output.write('\n\n------------------------n==4---------------------------')
		output.write('\nQ = ' + str(y[0]) +  ', L1 = ' + str(y[1]) + ', L2 = ' + str(y[2]) + ', L3 = ' + str(y[3]))
		output.write('\nI_i (t, p_i) = 3F / 4pi * (t + ' + str(y[0]) + ' + p_i + (' + str(y[1]) + ' * exp(-' + str(k[1]) + ' * t) ) / (1 - ' + str(k[1]) + ' * p_i) + (' + str(y[2]) + ' * exp(-' + str(k[2]) + ' * t) ) / (1 - ' + str(k[2]) + ' * p_i) + (' + str(y[3]) + ' * exp(-' + str(k[3]) + ' * t) ) / (1 - ' + str(k[3]) + ' * p_i)')
		output.write('\nS (t) = J(t) = 3F / 4pi * (t + ' + str(y[0]) + ' + (' + str(y[1]) + ' * exp(- ' + str(k[1]) + ' * t)) + (' + str(y[2]) + ' * exp(- ' + str(k[2]) + ' * t)) + (' + str(y[3]) + ' * exp(- ' + str(k[3]) + ' * t))')
	else:
		print('Zle n w funkcji WB')



WB(3)
WB(4)
output.close()