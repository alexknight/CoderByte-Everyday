'''
Using the Python language, have the function SimpleAdding(num) add up all the numbers from 1 to num.
For the test cases, the parameter num will be any number from 1 to 1000. Use the Parameter Testing 
feature in the box below to test your code with different arguments.
'''

def SimpleAdding(num):
	num=int(num)
	return sum(range(1,num))

print SimpleAdding(raw_input('Pls input the number:\n'))