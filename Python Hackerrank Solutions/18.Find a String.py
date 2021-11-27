"""

"""

"""
#OPTION 1

def count_substring(string, sub_string):
	c=0
	x=-1
	while x<len(string):
		y=string.find(sub_string, x+1)
		if y==-1:
			break
		c+=1
		x=y
	return c

#string = input() #ABCDCDC 
#sub_string = input() #C
#all_strings = [string, sub_string]
#print(count_substring(*all_strings)) #OUTPUT IS : 3 #There are 3 C

"""
#OPTION 2

def count_substring(string, sub_string):
	c=0
	length=len(sub_string)
	for x in range(len(string)):
		s=string[x:x+length]
		if s==sub_string:
			c+=1
	return c
#print(count_substring('ABCDCDC','CDC')) #OUTPUT : 2
