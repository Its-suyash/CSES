s=input()
temp=s[0] 
count1=1 #by default count is 1 of every char
count2=1
for i in range(1,len(s)):
    if s[i]==temp: #check if previous and current are equal 
        count1+=1
    else:
        count1=1 # if previous and current are not equal the reset the counter 
    temp=s[i] #change Previous
    count2=max(count1,count2) #max till not stored in the count2
 
print(count2)
