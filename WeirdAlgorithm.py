n=int(input()) #input taken
while n!=1:
    print(n,end=" ") # printing the value and creating space next to it for further printing
    if n%2==0:
        n=n//2 #floor value is stored
    else:
        n=n*3+1
print(1)
