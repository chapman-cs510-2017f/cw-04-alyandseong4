#!/usr/bin/env python3
# -*- coding: utf-8 -*-

###
# Name: Aly and Seong
# Course: CS510 Fall 2017
###

""" The Sieve of Eratosthenes algorithm
This module contains a function that create the primes.
"""

def eratosthenes(n):
    """ prime function
    Args: 
        n (int): prime numbers will be smaller than this number  
 
    Returns:
        a list of prime numbers  
    """  
    if n < 2:
        raise ValueError("Enter an integer greater than 2")
    else:  
        list = [i for i in range(2, n+1)]
        for p in range(2, n+1):
            for n in list:
                if n % p == 0 and n != p:
                    list.remove(n)
        return list


def prime_generator(n):
    list = [i for i in range(2, n+1)]
    for p in range(2, n+1):
        for n in list:
            if n % p == 0 and n == p:
                # print("prime", n)
                yield n
            elif n % p == 0 and n != p:
                list.remove(n)


def gen_eratosthenes(n):
    """ prime function
    Args: 
        n (int): an integer greater than 2. 
    Returns:
        a list of the first prime numbers that are smaller than n.  
    """
    if n > 1:
        return(list(prime_generator(n)))
    else:
        raise ValueError("Enter a positive number greater than 2, please.")


def main(n):
    print(eratosthenes(n))
    print("generator- ", gen_eratosthenes(n))


if __name__ == "__main__":
    import sys
    n = int(sys.argv[1])
    main(n)

