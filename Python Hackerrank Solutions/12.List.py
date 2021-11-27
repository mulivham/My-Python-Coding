"""

"""


n = int(input()) #INPUT : Numbers of command
list_ = []
for i in range(n):
	command= input().split()
	if command[0]=="insert": #INSERT COMMAND
		list_.insert(int(command[1]), int(command[2]))
	elif command[0] =="print": #PRINT COMMAND
		print(list_)
	elif command[0] == "remove": #REMOVE COMMAND
		list_.remove(int(command[1]))
	elif command[0] == "append": #APPEND COMMAND
		list_.append(int(command[1]))
	elif command[0] == "sort": #SORT COMMAND
		list_.sort()
	elif command[0] == "pop": #POP COMMAND
		list_.pop()
	else:
		list_.reverse() #REVERSE COMMAND

"""
Try To Run This Code USing The Given Input. 

15 # Command , First Input 
insert 0 5  #1
insert 1 10 #2
insert 0 6  #3
print       #4
[6, 5, 10]        #OUTPUT
remove 6    #5
print       #6
[5, 10]
append 9    #7
print       #8
[5, 10, 9]
append 1    #9
print       #10
[5, 10, 9, 1]
sort        #10
print       #11
[1, 5, 9, 10]
pop         #12
print       #13
[1, 5, 9]
reverse     #14
print       #15 There are 15 command
[9, 5, 1]

"""