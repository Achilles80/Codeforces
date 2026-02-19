def demo(n):
    cnt=0
    i,j=1,1
    ans=0
    for k in range(n):
        ans+=i*j 
        if cnt%2==0:
            j+=1 
        else:
            i+=1
    return (ans*2022)%(10**9+7)        

num=int(input())
for i in range(num):
    n=int(input())
    print(demo(n))