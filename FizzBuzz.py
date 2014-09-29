/* 
Create a program that prints "Fizz" fizz for multiples of 3, "buzz" for multiples #of 5, 
"FizzBuzz" for multiples of 3 AND 5, and the actual raw number itself for #everything else 
within the range of 1-100 
*/

for i in xrange(1,101):
		x = ""
		if i % 3 == 0: x += "Fizz"
		if i % 5 == 0: x += "Buzz"
		print x if len(x) else i
