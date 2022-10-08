# Each new term in the Fibonacci sequence is generated by adding the previous two terms. 
# By starting with 1 and 2, the first 10 terms will be:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

# Recursion is useful for fibonacci when trying to find the nth number in the series,
# however, it works differently in this context. This solution just steps linearly through the Fibonacci sequence,
# adding the even numbers to a sum, and stopping when the number value is greater than 4,000,000

def FibonacciEvens():
    sum, num1, num2, num3 = 0, 0, 1, 1
    while num3 <= 4000000:
        if num3 % 2 == 0:
            sum += num3
        num1 = num2
        num2 = num3
        num3 = num1 + num2
    print(sum)


'''Original Recursion idea
    while numb <= 4000000:
        if numb <= 1:
            numb = numb
            if numb % 2 == 0:
                sum += numb
    else:
        numb = FibonacciEvens(numb-1) + FibonacciEvens(numb-2)
        if numb % 2 == 0:
            sum += numb
    print(sum)
'''

FibonacciEvens()