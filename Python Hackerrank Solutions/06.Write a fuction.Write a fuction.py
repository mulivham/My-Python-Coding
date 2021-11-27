"""
TASK

"""

def is_leap(year):
	leap = False
	if (year % 4 == 0) and (year % 100 !=0 or year % 400 == 0):
		leap= True
	return leap

year =  int(input())  #User input for leap year check
#year = 1990 #OUTPUT : FALSE, Means 1990 is not a multiple of 4, Not a leap year
#year = 1992 #OUTPUT : TRUE, Means 1992 is a multtiple of 4, Its a leap year
print(is_leap(year))
#print("True or false :", year,"is a leap year? =", is_leap(year))
