d=1000-int(input())
now=0
m=[500,100,50,10,5,1]
c=0
while d!=0:
    c+=d//m[now]
    d%=m[now]
    now+=1
print(c)