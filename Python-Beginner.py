# CODING IN PYTHON
# WELCOME TO PYTHON

#Ingnore hashtage comments (#________), the're there to help you, guide you.
#Hashtag are used for comments, """ tripple double quotes for large comments""

"""
print("hello world") 

               # VARIABLE IN PYTHON
# In this case *age is the variable

age = 5 #This the proper way
age1 = 5  
age_2 = 5
#age-5 = 5 #invalid syntax
#5age = 5 #invalid syntax, error , cant start with a number.
Age = 5 #Does Work, But not recommended
age_of_a_boy = 5

print(age)
print(age1)
print(age_2)
#print(age-5)
#print(5age)
print(Age)
print(age_of_a_boy)

"""
#OPERATORS
#DIVISION OPERATORS

int_answer = 12 // 5  #/ =  Integer Division
float_answer = 12 / 5 #// = Float Division

print("Integer Answer =", int_answer) #Integer, an awnser without a decimal 
print("Float Answer =", float_answer)

#OR

#Method 1

import math

integer_answer1 = math.floor (float_answer)
print("Integer Answer =", int_answer) #Integer, an awnser without a decimal 
 

#Method 2
print("New Int Answer II =", math.floor(float_answer)) #math.floor = round down
print("New Int Answer III =", math.ceil(float_answer)) #math.ceil = round up 


print("---------------- Modulus Operator ---------------------------")
#MODULUS OPERATORS

slices_of_pizza = 12
people_to_share = 5 

print("Remaining pizza =", slices_of_pizza % people_to_share)  # %---> Modulus Operation

#POWERS OPERATOR

print(3*3*3) # 3 to the power 3
#OR
print(3 ** 3)

power_answer = math.pow(3, 3)
print(power_answer)  #Answer will be in double/ float

#OR Convert your Answers into an integers by :
print(math.floor(power_answer))

#Note Dont forget to use math operator (import math)

###################### STRINGS ########################

Alert = "Welcome to python"
print(Alert)

print("---------- New line strings -------------") #ignore
print("Welcome\nto\npython")  #To add a new line

print("---------- create space -------------") #igllnore
print("Welcome\tto\tpython")  # To create space

#Note : you can check other escape sequence on the internet.

print("---------- combining strings -------------")  #ignore

word = "pan"
word2 = "cake"
combined_words = word + word2
print("pan + cake =", combined_words)

print("---------- Long strings -------------") #ignore

lyrics = """baby girl, baby girrrlll... "you're my soulmate, you're my angel" """
print("Lyrics  =", lyrics)
#OR
print("Lyrics2 ="' baby girl, baby girrrlll... "you\'re my soulmate, you\'re my angel"')
#OR
print("Lyrics3 ="" baby girl, baby girrrlll... \"you\'re my soulmate, you\'re my angel\"")

print("---------- Slicing strings -------------") #ignore

movie_title = "gone in 60 seconds"

print(movie_title[3]) #Running this, words counted from 0-3 and you get 'e' "gon[e] in 60 seconds"
print(movie_title[3:]) #Running this, it grab and get all words after 'e' "gon[e in 60 seconds]"
print(movie_title[:3]) #Running this, it grab 3 words or get all words before 'e' "[gon]e in 60 seconds"
print(movie_title[-3]) #Running this, words counted backward from 0-3 'n' "gone in 60 seco[n]ds"
print(movie_title[-3:]) #Running this, it grab the last 3 words  "gone in 60 seco[nds]"
print(movie_title[:-3]) #Running this, it cut of last 3 words "[gone in 60 seco]nds"
print(movie_title[3:6])  #Running this, words counted from 0-3 'e' and 0-5 'i' "gon[e i]n 60 seconds"
print(movie_title[3:-6]) #Running this, it will cut of first 3 and last 6 words  "gon[e in 60 s]econds"

"""
# Note : [ : Any Number] [:3] This will include index
         [Any Number : ] [3:] This will exclude index
         [- Negative Any Number : ] [-3:] This will include Index
         [:- Negative Any Number] [:-3] This will exclude Index
"""
#OR Try  With :

#movie_title = "gone in 60 seconds"
cut_off = 3
print(movie_title[cut_off:cut_off + 3])  #This is the same as print(movie_title[3:6]), example.

# Note : You can use as many numbers you can use as example.

print("---------- LENGHTH FUNCTION -------------") #ignore
 
print(len(movie_title))  #18 characters long on a movie tltle
print("The title of the movie has", len(movie_title), "characters") #option 1
print("The title of the movie has"+str(len(movie_title))+"characters") #option 2


print("----------------- LIST -------------------")  #ignore

my_dinner = ["meat", "rice", "soup", "beans"]
print(my_dinner)
copy = my_dinner[:]
copy[1] = "maize"
print(copy)

#0R Try This :

kota_menu = ["cheese", "burger", "polony", "russian"]
#To change Menu :
change_menu = kota_menu[:]
#change_menu = Kota_menu.change_menu() #?????
change_menu[2] = "eggs"  #removing polony to add eggs, from index 2
print(kota_menu, change_menu)

#Now Try This Using Numbers:

numbers_in_order = [1, 2, 3, 4, 8, 6, 7, 8, 9, 10]
print("Original Numbers 1-10 =", numbers_in_order)
correct_number = numbers_in_order[:]
correct_number[4] = 5
print("Modified Numbers 1-10 =", correct_number)

print("------------- WORKING WITH A LIST ----------------")  #ignore


numbers_in_sequence = [1, 2, 3, [4, [4.0]], 5, 6]  #In this case you need to change 4,6 into "4,5"
print(numbers_in_sequence)
print(numbers_in_sequence[3]) #This will give "4"  from index 3
print(numbers_in_sequence[3][1])  #This will give you "4,5"
correct_sequence = numbers_in_sequence[:]
correct_sequence[3][1] = 4.5
print(correct_sequence)


#OTHER WAY :

import copy

numbers_in_sequence = [1, 2, 3, [4, [4.0]], 5, 6]
modified_number = copy.deepcopy(numbers_in_sequence)
modified_number[3][1] = 4.5
print(numbers_in_sequence, modified_number)

#TRY THIS :

gps_location = ["america", "europe", "africa", ["egypt", "s.africa", ["jo'burg", "durban"], "nigeria"], "asia"]
#change_location = gps_location[:] #Option 1 

import copy
change_location = copy.deepcopy(gps_location) #Option 2
change_location[3][2][1] = "cape town" #Changing Durban to Cape town
print(gps_location)
print(change_location)

correct_spelling = gps_location[:] #using option 1, you can use option 2
correct_spelling[3][2][0] = "Johannesburg"  # correcting spelling from jo'burg to johanne""
print(correct_spelling)

added_location = ["australia"] #OPTION  1
print(gps_location + added_location)

added_location_2 = gps_location + ["arctic"] #OPTION 2
print(added_location_2)

gps_location.append("antactica") #OPTION 3
print(gps_location)

modified_gps = gps_location + added_location + ["arctic"] #ALL OPTION IN ONE
print(modified_gps) #This will show the full list including added one


print(len(gps_location)) #To check your characters listed, print "len" length
print("There are",len(gps_location),"continent listed on my gps") #option 1
print("There are " + str(len(modified_gps)) + " modified continents listed on my gps")  #option 2

print("There are " + str(len(gps_location[3])) + " countries listed on my gps")  #option 2
print("There are",len(gps_location[3][2]),"cities listed on my gps") #option 1


#######################  USER INPUT ###########################
print("----------------  USER INPUT ---------------------------")
"""
print('Please Enter You\'re name')
name = input()
print("Hi " + name + " Welcome To Python")
print("Add Two Numbers")
print("Firsy Input : ")
number1 = input()
print("Second Input :")
number2 = input()
equal_to = number1 + number2
print("Output =", equal_to)
print("Alert(Wrong Answer) : Try Again, Using Same Numbers")

print("Firsy Input : ")
number1 = int(input()) #print(type(3))  # <class 'int'>
print("Second Input :")
number2 = int(input()) #print(type(3))  # <class 'int'>
equal_to = number1 + number2
print("Output =", equal_to)
print("Alert (Right Answer) : Good")
print(str(number1) + " + " + str(number2) + " = " + str(number1 + number2)) #OPTION 1
print(number1 , "+" , number2 , "=", equal_to) #OPTION 2

#Note : In Order To Get a Right Answer You Need To Convert into a Type of a Data 
print("----------------  Type of data --------------------------")


print(type("Python")) # <class 'str'>
print(type(3))  # <class 'int'>
print(type(3.5)) # <class 'float'>

print(type(int("3")))  # Converting a String integer <class 'int'>
print(type(float("3.5")))  # Converting a String float <class 'int'>
print(type(complex("3")))  # Converting a String complex <class 'int'> #??????

#######################   LOGIC  ###########################
print("----------------  IF/ELSE/ELIF --------------------------")

print("Please Enter Your Age To vote")

age = int(input())

if age > 70:
    print("Ask For An Asistance!")
elif age >= 18:
    print('You\'re Eligible To Vote' )
elif age == 17:
    print("One More Year To Vote")
elif age <= 10:
    print('What Are You Doing Here?')
else:
    print("You're Not Old Enough")
print("Thank You 4 Participating" )
"""

#booleans value are either True or False
print(2<3) #Run this, you get "True" as output
print(2>3) #Run this, you get "False" as output
print(2==3)  #False
print(2!=3)   #True
print("Hello" == "Hello") #True
print("Hello" != "Hello") #False

age = 18
print("age>=18?", age >= 18) #age(18) is greater and equal to (>=) 18 : True

ice = "water"
cream = "milk"
print("ice == cream?", ice == cream)

print("----------- BOOLEAN WITH CONDITIONS ------------------")


you_win = True  #The output will skip "If, win, True" to print"try again" since its false
if you_win == True:
    print("Congrats!!!!")
else:
    print("Try again")

you_win = False
if you_win:     # if condition is alright since the statement agrees the condition 
    print("Congrats!!!!")
else:
    print("Try again")

you_win = False
you_succeeded = True

if you_win or you_succeeded: #example of "or"
    print("Well done!")

you_pass = True
you_succeeded = False #The output will not show up, because its false, change it to true and it will show up.

if you_pass and you_succeeded: #example of "and"
    print("Good Job!!!") #This will not give the output since they all not true, change 


points = 6
you_win = False

if points < 50 and not you_win: #example of "not, and" This will return the True value
    print("Nice Try")
else:
    print("Well done!")

# or : one of the condion had to be true ( 5 > 10 or 5 < 10) in order to return "True"
# and : all the condtion had to be the same ( 10 > 5 or 5 < 10) in order to return a "True" Value
# not : When two false makes it True, like[ - x - = +] , so two false + false = True  [not ( 10 < 5 or 5 > 10)]

################# FOR LOOP #######################
print("---------- FOR LOOP ---------------------")

#Remember : kota_menu = ["cheese", "burger", "polony", "russian"]

for taste in kota_menu:
    print(taste)  #This will give the list of kota_menu in a new line

for taste in kota_menu:
    print(taste, end=" ") #This will list the iterms in the same line
print()  #To create a new line in python

#RANGE IN A FOR LOOP

for x in range(10): #OUTPUT : 0-9
    print(x)

for a in range(10,100): #OUTPUT: 10 - 99
    print(a, end=" ")
print()

for b in range(10,100,2): # Inside the range(start,stop,step)
    print(b, end=" ")   # OUTPUT : Will go go by 2 step = 10,12, 14 ....96, end at 98
print()

for c in range(100,10,-2): # This will go in decending order,
    print(c, end=" ")   # OUTPUT : Will go go by 2 step = 98,96,94 ....14, end at 12
print()

#LISTING > RANGE > FOR LOOP 
# Rembember : numbers_in_order = [1, 2, 3, 4, 8, 6, 7, 8, 9, 10]
print(numbers_in_order)  #Print this , Will gives us the list i created before

number_in_order2 = list(range(1, 11)) #OUTPUT : Will be the same as the first one = 1-10 
print(number_in_order2)  #This will automatically gives us the list

number_in_order2 = list(range(100)) #OUTPUT 0-100 
print(number_in_order2)  #This will automatically gives us the list

#PRINTING INDEX IN EACH ELEMENT

#REMEMBER AGAIN!
"""
kota_menu = ["cheese", "burger", "polony", "russian"]

"""
for taste in kota_menu:
    print(taste, end=" ") 
print()

print(len(kota_menu)) #To check the length

for x in range(len(kota_menu)):
    print(x, kota_menu[x], end=" ")  #This will give the list of kota_menu in a new line
print()

#BREAK FUNCTION
print("------------------- BREAK FUNTION -----------------------------")

#REMEMBER AGAIN!
"""
kota_menu = ["cheese", "burger", "polony", "russian"]

"""
for ingredient in kota_menu:
    print(ingredient )
    if ingredient == "polony":
        print(' "polony detected!" ')
        break

print("Search For Menu")
menu = "russian"

for ingredient in kota_menu:
    print(ingredient)
    if ingredient == menu:
        print(menu, "detected!" )
        break
    print("Searching... Please Wait!")

kota_menu = kota_menu + ["eggs","vienna", "chips","russian", "source"] #adding more ingredient
print(kota_menu)

#Now The List look like this:
"""
['cheese', 'burger', 'polony', 'russian', 'eggs', 'vienna', 'chips', 'russian', 'source']

"""
print("------------------- CONTINUE FUNCTION -----------------------------")
#CONTINUE FUNCTION

print("Search For Menu")
menu = "russian"

for ingredient in kota_menu:
    print(ingredient)
    if ingredient == menu:
        print(menu, "detected!" )
        continue #//This function is useful when there more more same element.
    print("Searching... Please Wait!")

"""
#ELSE (The same example can work on else statement)
print("Search For Menu")
menu = input()

for ingredient in kota_menu:
    print(ingredient)
    if ingredient == menu:
        print(menu, "detected!" )
    else:
        print("Searching... Please Wait!")

"""
print("--------------------------- PASS  ------------------------------------")

print("Search For Menu")
menu = "russian"
pass  # PASS : Can be used to patch some broken code that you can deal later.
for ingredient in kota_menu:
    pass #print(ingredient)
    if ingredient == menu:
        pass # PASS : Can be used to jump some code that you can deal later.
        print(menu, "detected!" )
        pass  #continue  / break / else
    pass #print("Searching... Please Wait!")
pass

print("--------------------------- ELSE  -------------------------------")
"""
print("Search For Menu")
menu = input()

for ingredient in kota_menu:
    print(ingredient)
    if ingredient == menu:
        print(menu, "detected!")
        break
    print("Searching... Please Wait!")
else:
    print(menu + " ?.. Not detected!")

"""

#OR YOU CAN TRY OTHER OPTION :
print("--------------------------- BOOLEAN -------------------------------")

print("Search For Menu")
menu = "spices" #input() #Since There is no spices on the kota_menu list, code will pass till end, or will execute depending on user input.
detect = False
for ingredient in kota_menu:
    print(ingredient)
    if ingredient == menu:
        print(menu, "detected!")
        detect = True
    print("Searching... Please Wait!")
if not detect:
    print(menu + " ?.. Not detected!") #Code will execute until down here

################# WHILE LOOP #######################
print("------------  WHILE LOOP --------------------")

"""
while (START < STOP):  // (initialization < condition/stop)
        print("Comment", START) // ("string" + initialization)
        START = STEP      // initialization = increment

"""

x = 0 #START // INITIALIZATION
while x < 10: #STOP // CONDITION
    print(x, end=" ")
    x += 1 #STEP // UPDATE
print()

#This The While Loop Format Without Details
"""
x = 0 
while x < 10:
    print(x)
    x += 1 
"""
#The Same Can Be Done With For Loop
for x in range(10): # Actual range(0,10,1), You get the same OUTPUT : 0-9
    print(x, end=" ")
print()

for x in range(0,10,1): #(INIT//START, COND//, UPT//STEP), You get the same OUTPUT : 0-9
    print(x, end=" ")

# Remember :
"""
#RANGE IN A FOR LOOP

for a in range(10,100): #OUTPUT: 10 - 99
    print(a, end=" ")
print()

for b in range(10,100,2): # Inside the range(start,stop,step)
    print(b, end=" ")   # OUTPUT : Will go go by 2 step = 10,12, 14 ....96, end at 98
print()

for c in range(100,10,-2): # This will go in decending order,
    print(c, end=" ")   # OUTPUT : Will go go by 2 step = 98,96,94 ....14, end at 12
print()

"""
#Do The Same With While loop

a = 10
while a < 20:
    print(a) #OUTPUT: 10 - 19
    a += 1


b = 10
while b < 100:
    print(b, end=" ") # OUTPUT : Will go go by 2 step = 10,12, 14 ....96, end at 98
    b += 2
print()


c = 100  #//for c in range(100,10,-1): # This will go in decending order
while c > 10:
    print(c, end=" ") #OUTPUT: 100 - 10
    c -= 1
print()

#LISTING > WHILE LOOP 

# Rembember : numbers_in_order = [1, 2, 3, 4, 8, 6, 7, 8, 9, 10]
x = 0
while x<len(numbers_in_order):
    print(numbers_in_order[x], end=" ")
    x += 1
print()


#????????????????????????
"""
print("Enter a number 0-9")
x = 0
random_number = 7
while x < len(numbers_in_order):
    if numbers_in_order[x] > random_number:
        print( numbers_in_order[x], "is greater than >", random_number)
        break
    x += 1
    print(numbers_in_order[x] ," is less than <", random_number )
else:
    print(random_number + "is invalid ")

"""

################# DO WHILE LOOP #######################
print("------------ DO WHILE LOOP --------------------")

# Do While Loop Structure

x = 11  #OUTPUT : 11
print(x)
#x += 1
while x < 10:
    print(x, end = " ")
    x += 1


x = 1      #OUTPUT : 1 2 3 4 5 6 7 8 9
print(x)
#x += 1
while x < 10:
    print(x, end = " ")
    x += 1
print()

#Option 2

y = 11
while True:
    print(y, end = " ")
    y += 1
    if y > 10:
        break
print()

y = 1
while True:
    print(y, end = " ")
    y += 1
    if y > 9:
        break
print()

################# Sentinel / Indefinite Loop #######################
print('-----------  Sentinel / Indefinite Loop  ------------------')

#OPTION 1
"""
#EXAMPLE 1

print("Please Press : Y = TO ENTER OR Q = TO QUIT")
input_ = input()
while input_ == "Y": #Upper case "Y" will excute 
#while input_ == "y": # Do the same for lowercase
    print('Do You Want To Proceed? "Y"/"N"')
    input_ = input()
"""
#// OR YOU CAN USE ".upper()"/ ".lower()" case method
"""

print("Please Press : YES/yes = TO ENTER OR Q = TO QUIT")
input_ = input()
while input_.upper() == "YES": # This will excute both upper and lower
#while input_.lower()== "yes": # This will excute both upper and lower
    print('Do You Want To Proceed? "Y"/"N"')
    input_ = input() # YES/yes
"""
#OPTION 2 ALL EXAMPLES
"""
while True:
    print("Please Press : Y = TO CONTINUE OR Any keys = TO STOP" )
    input_ = input()
    #if input_ != "Y":
    #if input_ == "Y":
    #if input_.lower() == "y":
    if input_.upper() == "Y":
    #if input_ != "Y" and input_ !="y":
    #if input_ == "Y" or input_ == "y":
        #break #( You might wanna break if "!=" is no equal to)
        continue #( You might wanna continue if "==" is no equal to)
    break
"""

#EXAMPLE 1
"""
while True:
    print( "Do you want to proceed? y/n" )
    input_ = input()
    if input_ != "y": #This will will respond to lowercase only
        break  #( You might wanna break if "!=" is no equal to)
"""
#EXAMPLE 2
"""

loop = True

while loop:
    input_ = input("Do you want to proceed? yes/no ")
    if input_ == "yes": #This will will respond to lowercase only 
        continue #( You might wanna continue if "==" is no equal to)
    break
"""

#EXAMPLE 3
"""
while True:
    print( "Do you want to proceed? y/N" )
    input_ = input()
    if input_ != "y" and input_ != "Y":  #This will will respond to both lowe and upper case (Y/y)
        break  #( You might wanna break if "!=" is no equal to)

"""
#EXAMPLE 4
"""
while True:
    print( "Do you want to proceed? YES/no" )
    input_ = input()
    if input_ == "yes" or input_ == "YES":  #This will will respond to both lowe and upper case (yes/YES)
        continue  #( You might wanna continue if "==" is no equal to)
    break
"""

#EXAMPLE 5 (".lower()" method)

"""
while True:
    print( "Do you want to proceed? yes/NO" )
    input_ = input()
    if input_.lower() != "yes": #This will will respond to lowercase only
        break  #( You might wanna break if "!=" is no equal to)

"""
#EXAMPLE 6 (".upper()" method)
"""
while True:
    print( "Do you want to proceed? yes/no" )
    input_ = input()
    if input_.upper() == "YES": #This will will respond to lowercase only 
        continue #( You might wanna continue if "==" is no equal to)
    break
"""

loop = True

while loop:
    password = input('Enter Password: ')
    if int(password)== 1234:
        print('Now Loging-in....')
    else:
        print( "Wrong Password! Try Again")

        
# TO CHECK IF THE STRING IS UPPER OR LOWERCASE

string = "PHP"  #OUTPUT :  UPPER - Because they're all in uppercase
#string = "python"  #OUTPUT :  LOWER - Because they're all in lowercase
#string = "JaVa"  #OUTPUT :  MIXED - Because they're all in uppercase and lowercase
#string = input() # You can try your output here
if string.isupper():
    print('IT\'S UPPER CASE')

elif string.islower():
    print('IT\'S LOWER CASE')

else:
    print('IT\'S MIXED CASE')

################# NESTED IF STATEMENT #######################
print("----------- Nested if statement ---------------------")


print("Please Enter Your Name To Sign In ______")
sign_in = True
signing_in = True
account = 'Yannick'
#account = input()

if signing_in == True:
    if sign_in == True:
        print("Loading.....", account, "Is Signing In")
    print("Welcome To Python :", account)

#Nested Loop
print("----------- Nested Loops ---------------------")

for x in range(4):  #Vertical loop - counting downward
    for y in range(6): #Horizontal Loop - counting upward
        print(y, end=" ")
    print()

print("----------- Colunm ---------------------")

for x in range(4):  #Vertical loop - counting downward
    #print("Colunm", str(x), ":")
    print("Colunm", str(x + 1), "=") #Can start at any column .. str(x+1, or 2. or 3)
    for y in range(6): #Horizontal Loop - counting upward
        print(y, end=" ")
    print()

print("----------- Multiples ---------------------")

for x in range(4):  #Vertical loop - counting downward
    #print("Counting by", str(x), ":")
    print("Counting by", x ,":") #Can start at any column .. str(x+1, or 2. or 3)
    for y in range(6): #Horizontal Loop - counting upward
        print(y*x, end=" ")
    print()

#TRIANGLE STRUCTURES
print("------------ TRIANGLE STRUCTURES -----------")
print("------------range(x)------------------------")

for x in range(10):  #Vertical loop - counting downward
    for y in range(x): #Horizontal Loop - counting upward
        print(y, end=" ")
    print()

print("----------range(x,10)------------------------")

for x in range(10):  #Vertical loop - counting downward
    for y in range(x,10): #Horizontal Loop - counting upward
        print(y, end=" ")
    print()

print("----------range(x + 1)------------------------")

for x in range(10):  #Vertical loop - counting downward
    for y in range(x+1): #Horizontal Loop - counting upward
        print(y, end=" ")
    print()

################# NESTED WHILE STATEMENT #######################
print("----------- Nested while statement ---------------------")

#BASIC/ STANDARD VS NESTED WHILE LOOP
#Basic/ Standard while loop

x = 0
while x< 10:
    print(x)
    x += 1

#Basic/ Standard While Loop/ Nested While Loop If You Remove the "#" Hastags

x = 0
while x < 10:
    #y = 0
    #while y < 10:
    #    print(y, end=" ")  #print(x , y)
    #    y += 1
    print(x, end=" ")
    x += 1
print()

print("----------- Nested While Examples -----------------")
print()

x = 0
while x < 10:
    y = 0
    while y < 10:
        print(y, end=" ")  #print(x , y)
        y += 1
    print()
    x += 1

print("----------- Bas/Stardard W.loop Total Output -----------")
print()  # New line 

x = 10
plus = 0
while x > 0:
    plus += x
    x -= 1
print("Total Output of Bas/St W.Loop =", plus)
print()


print("----------- Nested W.loop Total Output -----------------")
x = 10
while x > -1:
    plus = 0
    y = x
    while y > 0:
        if y > 1:
            print(y , " + " , end=" ")
        else:
            print(y , " = " , end=" ")
        plus += y
        y -= 1
    print(plus)
    x -= 1
print() # New line 

################# DEF & RETURN FUNCTION #######################
print("----------- DEF & RETURN FUNCTION ---------------------")
print("----------- DEF FUNCTION ---------------------")

#STEP 1

#ingredient = "source"
def food ():
    print("Would You like to try our", ingredient, "sir/madam")
    print("enjoy your meal")

food()  # This function saves a lot of line of code 

#STEP 2

def food (ingredient):
    print("Would You like to try our", ingredient, "sir/madam")
    #print("enjoy your meal")

ingredient = "chips"
food(ingredient)
food("burger")
food("eggs")

print("----------- RETURN FUNCTION ---------------------")

def food(ingredient):
    if ingredient == "cheese":
        print("mmmhhhh", ingredient, "is so milky")
        return
        
    print("Would You like to try our", ingredient, "sir/madam")
    

ingredient = "chips"
food(ingredient)
food("burger")
food("cheese")

#The same can work on else fuction

def food(ingredient):
    if ingredient == "cheese":
        print("mmmhhhh", ingredient, "is so milky")
        
    else:    
        print("Would You like to try our", ingredient, "sir/madam")
    

ingredient = "chips"
food(ingredient)
food("burger")
food("cheese")

print("----------- PEREMETERS ---------------------")

"""
def funcname(parameter_list):
    pass

"""

def earth(continent): # inside the prethesis is a peremeter
    if continent == "Antarctica":
        return "Its freezing out there, so cold"
    return "Welcome to, " + continent + " i hope you enjoy your stay"

planet = earth("Africa")
print(planet)
                                #OPTION 1
planet = earth("Antarctica")
print(planet)
                                #OPTION 2
print(earth("Antarctica"))
print(earth("Africa"))

print() #--------------------- New line

def earth(continent= "World"): # Default peremeter, Meaning if no input, the "world" as output o standby
    if continent == "Antarctica":
        return "Its freezing out there, so cold"
    return "Welcome to, " + continent + " i hope you enjoy your stay"

print(earth())
print(earth("Africa"))
print(earth("Australia"))

print() #--------------------- New line
#Flag Viables Inside The Peremeter :

def earth(continent= "World", it_is_hot=True): 
    if not it_is_hot:
        return "Its freezing out there, so cold"
    return "Welcome to, " + continent + " i hope you enjoy your stay"

print(earth(it_is_hot=False ))
print(earth("Africa"))
print(earth("Asia"))

print() #--------------------- New line


def earth(continent= "World", it_is_hot=True): 
    if not it_is_hot:
        return "Its freezing out there, so cold"
    return "Welcome to, " + continent + " i hope you enjoy your stay"

print(earth("Africa", it_is_hot=True ))
print(earth("Africa"))
print(earth("Asia"))

print() #--------------------- New line
#Inside the peremeter :

#Example 1
def earth(city, country, continent):
    print(city + " is inside " + country + " in " + continent)
    
earth('Joburg', 'South Africa', 'Africa')  #Joburg is inside South Africa in Africa

#Example 2

def earth(continent, land_mass, population):
    print(continent + " is the " + land_mass + " largest continent in the world, has " + str(population) + " billion people")
    
earth('Africa', '2nd', 2)

print() #--------------------- New line
#Listing in def Function :

world = ['Africa', '2nd', 2]
earth(*world)

print()  #OR 

world = ['Africa', '2nd', 2]
earth(world[0], world[1], world[2])

print() #--------------------- New line
#Last Example

def earth(continent, land_mass, population):
    print(continent + " is the " + land_mass + " largest continent in the world, has " + str(population) + " billion people")

print("Enter a continent")
continent = input()
print("Enter a land mass")
land_mass = input()
print("Enter a population")
population = int(input())
world = [continent, land_mass, population]
earth(*world)

