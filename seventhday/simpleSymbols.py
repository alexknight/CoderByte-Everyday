'''
Using the Python language, have the function SimpleSymbols(str) take the str parameter 
being passed and determine if it is an acceptable sequence by either returning the string 
true or false. The str parameter will be composed of + and = symbols with several letters 
between them (ie. ++d+===+c++==a) and for the string to be true each letter must be surrounded 
by a + symbol. So the string to the left would be false. The string will not be empty and will 
have at least one letter. 
'''


# def SimpleSymbols(str):
# 	list=str.split("+")
# 	list_a=[]
# 	for elem in list:
# 		if elem:
# 			list_a.append(elem)

# 	for elem in list_a:
# 		if not elem.isalpha():
# 			return false
# 		else:
# 			continue

# print SimpleSymbols(raw_input("input a str"))