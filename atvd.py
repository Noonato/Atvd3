from math import sqrt
from time import time

def checkIntNumber(n):
	return int(n) == n


def verificaNumeroPrimoV1(n, showStatusFlag=False):
	if n == 2:
		return True
	elif (n == 1) or (n % 2 == 0) or (checkIntNumber(sqrt(n))):
		return False
	else:
		primoFlag = True
		limite = int(sqrt(n))

		if limite % 2 == 0:
			d = limite + 1
		else:
			d = limite
		o = n / d
		if (o <= d):
			return primoFlag

		d = 1 
		divisoes = 0
		count = 0
		while (d <= limite) and (divisoes <= 2):
			count = count + 1			
			if (n % d == 0):				
				divisoes = divisoes +1
				if (divisoes == 2) and (d != n):
					primoFlag = False
					break
			d = d + 2
		
		if showStatusFlag:
			print ('n:', n, 'd:', d, 'count:', count, 'divisoes:', divisoes)
		
		return primoFlag


def verificaNumeroPrimoV2(n, showStatusFlag=False):
	if n == 2:
		return True
	elif (n == 1) or (n % 2 == 0) or (checkIntNumber(sqrt(n))):
		return False
	else:
		primoFlag = True
		limite = int(sqrt(n))

		if limite % 2 == 0:
			d = limite + 1
		else:
			d = limite
		o = n / d
		if (o <= d):
			return primoFlag

		d, o, r = 1, 0, 0

		divisoes = 0
		count = 0
		while (d <= limite) and (divisoes <= 2):
			count = count + 1
			
			r = n % d
			
			if (r == 0):				
				divisoes = divisoes +1
				if (divisoes == 2) and (d != n):
					primoFlag = False
					break			
			else:
				o = n / d
				if (o <= d):
					primoFlag = True
					break

			d = d + 2
			
		if showStatusFlag: 
			print ('n:', n, 'd:', d, 'o:', o, 'r:', r, 'count:', count, 'divisoes:', divisoes)
		return primoFlag

def primos(max):
	primosArr = []
	for i in range(1, max+1):		
		if verificaNumeroPrimoV1(i):
			primosArr.append(i)
			print (i, True)
		else:
			print (i, False)
	return primosArr


tp1 =time()
print (primos(100))
tp2 = time()
print ('function primos takes %f' %(tp2-tp1))
