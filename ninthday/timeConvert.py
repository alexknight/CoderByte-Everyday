'''
Using the Python language, have the function TimeConvert(num) take the num
parameter being passed and return the number of hours and minutes the parameter 
converts to (ie. if num = 63 then the output should be 1:3). Separate the number 
of hours and minutes with a colon.Use the Parameter Testing feature in the box 
below to test your code with different arguments. 
'''


def TimeConvert(num):
	hours=int(num)/60
	if hours==0:
		return "0"+":"+num
	if hours>0:
		mintus=int(num)-60*hours
		return str(hours)+":"+str(mintus)


print TimeConvert(raw_input()) 







