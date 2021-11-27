"""
TASK

The provided code stub read and integer, n, fom STDIN. for all non-negative integers i < n, print i(square)

"""
#n = int(input())
n = 5     #If the iput is 5, Output is : 0,1,4,9,16
for i in range(n): #range(START // INITIALIZATION, STOP // CONDITION, #STEP // UPDATE) = (n=0, n=n-1, n=1) 
    #print( i ) #The Ouput
    print( i * i) #Output x Output

print() #New Line 
print("---------- Using While Loop --------------")

n = 5
i = 0 #START // INITIALIZATION
while i < n: #STOP // CONDITION
	#print(i)
    print(i * i, end=" ")
    i += 1  #STEP // UPDATE



    
