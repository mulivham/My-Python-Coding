"""
this isthe coding this manyp ofthe contraint 
"""
#n =23665 #The list
arr=list(map(int,input().split())) #Put it in the list
arr.sort() #Sorting up the list [23566]
print(arr[(arr.index(max(arr)))-1]) # [(23566(max=6))-1] = (index of max - 1)