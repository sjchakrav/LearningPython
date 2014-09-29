'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.
'''
def multiples(x):
    sum = 0
    for i in range(1,x):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    else:
        return sum

print(multiples(10)) 
print("answer: ", multiples(1000))
