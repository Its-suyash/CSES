s=input()
d={}
p=""
for i in s:# creating hashmap
    if i not in d:
        d[i]=1
    else:
        d[i]=d[i]+1
count=0
for i in d:# checking for odd length sring
    if d[i]%2!=0:
        count+=1
        if count==2: #more than one not allowed direct not soln
            break
    if len(s)%2==0: #for even length string 
        pass    
    elif d[i]%2!=0: #for odd length string we need to make it in the middle
        p=i 
if count==2:
    print("NO SOLUTION")
elif len(s)%2==0: #even length string 
    ans=""
    for i in d:
        ans=ans+(i*(d[i]//2)) #store half string by adding half times the characters
    print(ans+ans[::-1])
else:
    ans=""
    for i in d:
        if d[i]%2==0:
            ans=ans+(i*(d[i]//2)) #same as even but added the odd frequency length in the middle
    print(ans+(p*d[p])+ans[::-1])
