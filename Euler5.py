'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 
10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the 
numbers from 1 to 20?
'''

def y(a,b): return b and y(b, a % b) or a
def z(a,b): return a * b / y(a,b)

n = 1
for i in xrange(1, 21):
     n = z(n, i)

print n
