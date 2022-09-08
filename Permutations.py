n=int(input())
if n==1:
    print(1)
elif n<4:
    print("NO SOLUTION")
elif n==4:
    print("2 4 1 3")    #'''Above the edge cases are printed''''
else:
    for i in range(1,n+1,2): # print odd numbers
        print(i,end=" ")
    for i in range(2,n+1,2): #print even numbers 
        print(i,end=" ")
        
 
    
