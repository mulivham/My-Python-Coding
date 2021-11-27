"""
Task

* if n is odd, print "weird". 3 an example of odd number
* if n is even and inclusive range of 2 to 5, print "not weird" . 2 example of even number.
* if n is even and inclusive range of 6 to 20, print "weird"
* if n is even and greater than 20, print "not weird"
"""

n= int(input())
#n= 2 #Not Wierd
#n= 3 #Wierd
if n%2 != 0:
	print("Wierd")
else:
	if n > 2 and n < 5:
		print("not Wierd")
	elif n > 6 and n<=20:
		print("Wierd")
	elif n<20:
		print("not Wierd")