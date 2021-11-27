num1 = input("Enter first number : ")
num2 = input("Enter secound number : ")
num3 = input("Enter third number : ")

def assum():
	if num1 == num2 or num2 == num3 or num1 == num3:
		return 0
	else:
		return int(num1) + int(num2) + int(num3)

print(assum())
