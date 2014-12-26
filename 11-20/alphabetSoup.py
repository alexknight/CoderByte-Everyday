#-*-coding=utf-8-*-
'''
Using the Python language, have the function AlphabetSoup(str) take the str string 
parameter being passed and return the string with the letters in alphabetical order 
(ie. hello becomes ehllo). Assume numbers and punctuation symbols will not be included 
in the string.Use the Parameter Testing feature in the box below to test your code with 
different arguments. 
将字母按字母表排序
'''

def AlphabetSoup(str):
	return ''.join(sorted(str))

print AlphabetSoup(raw_input())