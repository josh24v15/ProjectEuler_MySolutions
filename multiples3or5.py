#Project Euler - Problem 1
#https://projecteuler.net/problem=1
#
#Prompt:
#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.


def test_1():
    sum = 0
    for number in range(1,1000):
        if number % 3 == 0 or number % 5 == 0:
            sum += number
    return sum

print(test_1())
#prints 233168

def test_2():
    return sum([x for x in range(1,1000) if x % 3 == 0 or x % 5 == 0])

print(test_2())
#prints 233168