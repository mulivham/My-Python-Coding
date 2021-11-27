"""

"""
#OPTION 1
"""
def swap_case(s):
	x = ""
	for c in s:
		if c.isupper():
			c=c.lower()
		else:
			c=c.upper()
		x+="".join(c)
	return x
	 
print(swap_case("muLiVhA")) #MUlIvHa
print(swap_case("CHANGING STRING FROM UPPERCASE TO LOWER")) #OUTPUT : changing string from uppercase to lower
print(swap_case('changing a string from lowercase to upper')) #OUTPUT : CHANGING A STRING FROM LOWERCASE TO UPPER
		#OR TRY
"""

#OPTION 2

def swap_case(s):
	return s.swapcase()

#print(swap_case("Www.HackerRank.com")) #OUTPUT : wWW.hACKERrANK.COM
#print(swap_case("Pythonist 2"))  #OUTPUT : pYTHONIST 2
