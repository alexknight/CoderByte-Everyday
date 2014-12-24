'''
Have the function FirstFactorial(num) take the num parameter being passed and return the factorial of
it (ie. if num = 4, return (4 * 3 * 2 * 1)). For the test cases, the range will be between 1 and 18.
Use the Parameter Testing feature in the box below to test your code with different arguments. 
'''

def FirstFactorial(num):
	a=1
	for i in range(1,num+1):
		a=a*i
	return a

print FirstFactorial(raw_input())  