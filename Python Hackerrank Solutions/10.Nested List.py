"""

"""
n = int(input())
res= []
grade= []
for i in range(n):
	name = input()
	mark = float(input())
	res.append([name, mark])
	grade.append(mark)
#print(res)
#print(grade)
grade=sorted(set(grade))
#print(grade)
mrk=grade[1]
#print(mrk)
name=[]
for val in res:
	if mrk==val[1]:
		name.append(val[0])
#print(name) #unsorted
name.sort() #Sorting
print(name) #Sorted
for namemark in name:
	print(namemark)