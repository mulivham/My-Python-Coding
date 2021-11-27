"""

"""
#Quick Example of Split and Joint
"""
x = 'spliting the string'
y=x.split() 
z=x.split('i') #This is going to cut-off all the 'i'
print(y)
print(z)

a = "------".join(y)
print(a) #OUTPUT : splitin-----the----- string

"""

def split_and_join(line):
	a=line.split()
	x="-".join(a)
	return x

#print(split_and_join("this is a string")) #OUTPUT : this-is-a-string