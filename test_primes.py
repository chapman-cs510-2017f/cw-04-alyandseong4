#!/usr/bin/env python3
# -*- coding: utf-8 -*-

###
# Name: Aly and Seong
# Course: CS510 Fall 2017
###

"""Testing the Sieve of Eratosthenes algorithm (prime algorithm)
This module contains three test functions to keep the prime function safe from errors.
"""

import primes

def test_primes():
    """test the first 10 prime numbers"""
    
    result = primes.eratosthenes(30)
    correct = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    assert result == correct

def test_primes1():
    """test the first prime numbers smaller than 500"""
    
    result = primes.eratosthenes(500)
    correct = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499]
    assert result == correct

def test_primes2():
    "test the last prime number below 1000"
    result = primes.eratosthenes(1000)[-1]
    assert result == 997
