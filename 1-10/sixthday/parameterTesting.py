'''
Using the Python language, have the function LetterCapitalize(str) take the str parameter being
passed and capitalize the first letter of each word. Words will be separated by only one space. 
Use the Parameter Testing feature in the box below to test your code with different arguments.
'''

def LetterCapitalize(str):
	str=str.split()
	new_list=[]
	for elem in str:
		elem=elem[0].upper()+elem[1:]
		new_list.append(elem)
	return ' '.join(new_list)
print LetterCapitalize(raw_input('input the sentence.\n'))










