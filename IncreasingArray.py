n=int(input())
a=[int(i) for i in input().split()] # storing the spaced intergers into list
count=0
prev=a[0]
for i in range(1,n):
    if a[i]< prev: #check if current is less than previous
        count+=(prev-a[i]) # cost of making it equal to the previous
        a[i]=a[i]+prev-a[i] #making it equal
 
    prev=a[i] 
print(count)
