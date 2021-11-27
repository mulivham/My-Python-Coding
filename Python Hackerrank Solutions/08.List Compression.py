"""

"""
""
#User Input /(STDIN)
x = 1
y = 1
z = 2
n = 3

#x = int(input())
#y = int(input())
#z = int(input())
#n = int(input())

"""
res=[]

for i in range( x+1):
	for j in range(y+1):
		for k in range(z+1):
			if i+j+k !=n:
				res.append([i,j,k])

print(res)
"""

#Inside Compression list [expression, for loop, condition]

res=[[i,j,k] for i in range( x+1) for j in range(y+1) for k in range(z+1) if i+j+k !=n]
print(res)