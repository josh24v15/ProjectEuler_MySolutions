# Project Euler, problem 3: https://projecteuler.net/problem=3
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

# The largest prime factor has to be less than the square root of the target number so I'll look within that range.
# (each factor of target less than square root has a corresponding factor of target above square root, so any number larger than square root will be accounted for.)

from math import sqrt
target1 = 600851475143

def largestPrime(target):
    answer = 0
    #Want to check all numbers from 2 up to square root of target to determine if prime
    for i in range(2, int(sqrt(target))):
        #skip the inner loop if i is an even number (i.e. not prime)
        if i % 2 == 0:
            continue
        #skip the inner loop if i isn't a factor of target
        elif target % i != 0:
            continue
        #for each factor of target, check to see if factor is prime
        for j in range(2, int(sqrt(i))):
            #check to see if j is a factor i (i.e. i is not prime)
            if i % j == 0:
                break
            #update answer if i is determined to be a prime factor
            if j == int(sqrt(i))-1:
                answer = i
    return answer
            







'''First attempt through a linear approach that just didn't eliminate enough of the numbers.
MIGHT have worked, but it was taking unreasonably long to justify waiting around to see.

def largestPrime(target):
    answer = 0
    half_target = int(target/2)+1 # Only numbers less than half of target can be a factor of target
    while half_target > 1:
        if target % half_target != 0:
            print(f'{half_target} is not a factor of {target}')
            half_target -= 1
            continue
        if half_target % 2 == 0:
            print(f'{half_target} is not a prime number')
            continue
        quarter_target = int(half_target/2)+1 # Only numbers less than half of half_target can be a factor of half_target
        for i in range(2, quarter_target):
            if half_target % i == 0:
                print(f'{i} is not a prime number')
                break
            if i == 2:
                return half_target
        half_target -= 1

''' 
print(largestPrime(target1))
