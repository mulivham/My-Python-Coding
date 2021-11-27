"""
"""

n = int(input())
student_marks = {}
for _ in range (n):
	name, *line = input().split()  #Input can like : Jean 54 60 39 26 < That a name and marks
	scores = list(map(float, line)) #Converting The Line from intrgers to float, and assign it in Score Variable.
	student_marks[name] = scores
query_name = input()
marks = student_marks[query_name]
print(format(sum(marks)/3,".2f")) # Note : '.2f' Coverting it into 2 decimal 

"""
#Example on Line 6
#Try

name, *line = input().split() #Input can like : Jean 54 60 39 26 < That a name and marks
scores = list(map(float, line)) #Converting The Line from intrgers to float, and assign it in Score Variable.
print(name, line)
print(scores) #Output in float

"""

