def collatz(number):

    while number > 1:
        if number % 2 == 0:
            print(number//2)
            number = number //2

        elif number % 2 ==1:
            print(3*number+1)
            number = 3*number+1

        else:
            print(number)

number = int(input("Enter a number : "))
collatz(number)
