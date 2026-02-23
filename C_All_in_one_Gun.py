import os,sys
from io import BytesIO,IOBase
BUFSIZ=8192
class FastIO(IOBase):
    newlines=0
    def __init__(self,file):
        self._fd=file.fileno()
        self.buffer=BytesIO()
        self.writable="n"in file.mode or "r" not in file.mode
        self.write=self.buffer.write if self.writable else None
    def read(self):
        while True:
            b=os.read(self._fd,max(os.fstat(self._fd).st_size,BUFSIZ))
            if not b:
                break
            ptr=self.buffer.tell()
            self.buffer.seek(0,2),self.buffer.write(b),self.buffer.seek(ptr)
        self.newlines=0
        return self.buffer.read()
    def readline(self):
        while self.newlines==0:
            b=os.read(self._fd,max(os.fstat(self._fd).st_size, BUFSIZ))
            self.newlines=b.count(b"\n")+(not b)
            ptr=self.buffer.tell()
            self.buffer.seek(0, 2),self.buffer.write(b),self.buffer.seek(ptr)
        self.newlines-=1
        return self.buffer.readline()
    def flush(self):
        if self.writable:
            os.write(self._fd,self.buffer.getvalue())
            self.buffer.truncate(0),self.buffer.seek(0)
class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer=FastIO(file)
        self.flush=self.buffer.flush
        self.writable=self.buffer.writable
        self.write=lambda s:self.buffer.write(s.encode("ascii"))
        self.read=lambda:self.buffer.read().decode("ascii")
        self.readline=lambda:self.buffer.readline().decode("ascii")
if sys.version_info[0]<3:
    sys.stdin,sys.stdout=FastIO(sys.stdin),FastIO(sys.stdout)
else:
    sys.stdin,sys.stdout=IOWrapper(sys.stdin),IOWrapper(sys.stdout)
input=lambda:sys.stdin.readline().rstrip("\r\n")

def solve():
    n,h,k=input().split(" ")
    n=int(n)
    h=int(h)
    k=int(k)
    a=input().split(" ")
    for i in range(n):
        a[i]=int(a[i])
    s=sum(a)
    pr=[0 for i in range(n)]
    pmin=[0 for i in range(n)]
    pr[0]=a[0]
    pmin[0]=a[0]
    for i in range(1,n):
        pr[i]=pr[i-1]+a[i]
        pmin[i]=min(pmin[i-1],a[i])
    sma=[0 for i in range(n)]
    sma[n-1]=a[n-1]
    for i in range(n-2,-1,-1):
        sma[i]=max(sma[i+1],a[i])
    ans=float('inf')
    o=[]
    for r in range(1,n+1):
        z=r-1
        gain=0
        if r<n:
            if sma[z+1]>pmin[z]:
                gain=sma[z+1]-pmin[z]
        p=pr[z]+gain 
        rem=h-p 
        if rem<=0:
            c=0 
        else:
            c=(rem+s-1)//s 
        t=c*(n+k)+r
        if t<ans:
            ans=t
    print(ans)
         




tcs = int(input())
for tc in range(tcs):
    solve()