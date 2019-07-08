p1=int(input())
r2=list(map(int,input().split()))
a3=int(p1/2)
la1=r2[:a3]
lb2=r2[a3::]
if ((sum(la1)//len(la1))==(sum(lb2)//len(lb2))):
    print("yes")
else:
    print("no")
