n= int(input())
commas = 1
res=0
cur=1000
while cur<=n:
    next=cur*1000
    nums=min(n-cur+1,next-cur)
    res+=nums*commas
    cur=next
    commas+=1
print(res)