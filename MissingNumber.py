n=int(input())
a=[int(i) for i in input().split()] #string the spaced value in list
n=n*(n+1)//2 #formula for the sum of n natural numbers
print(n-sum(a))
