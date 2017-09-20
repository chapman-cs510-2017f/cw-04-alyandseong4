#!/usr/bin/env python3

def eratosthenes(n):
	nummult = []
	
	for i in range(2, n+1):
		
		if i not in nummult:
			print (i)
			
			for j in range(i*i, n+1, i):
				nummult.append(j) 

def gen_eratosthenes():
	"""Generator of prime numbers."""
	yield 2 #starts from 2
	i = 3 
	while i < n:
		for p in eratosthenes(int(math.sqrt(i))+1):
			if i % p == 0:
				break
		else:
			yield i
		i = i + 2


if __name__ == "__main__":

import sys

main(sys.argv)


 
