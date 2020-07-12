#for문

#2739
a=int(input())
for i in range(1,10):
    print(a,"*",i,"=",a*i)

#10950
N=int(input())
for i in range(N):
    a,b=input().split()
    print(int(a)+int(b))

#11021
N=int(input())
for i in range(N):
    a,b=input().split()
    c=int(a)+int(b)
    print("Case #",i+1,':',' ',c,sep='')

#11022
N=int(input())
for i in range(N):
    a,b=input().split()
    c=int(a)+int(b)
    print("Case #",i+1,':',' ',a,' + ',b,' = ',c,sep='')

#8393
N=int(input())
sum=0
for i in range(1,N+1):
    sum+=i
print(sum)

#15552
import sys
N=int(sys.stdin.readline())
for i in range(1,N+1):
    a,b=map(int,sys.stdin.readline().split())
    print(int(a)+int(b))

#2741
N=int(input())
for i in range(N):
    print(i+1)

#2742
N=int(input())
for i in range(N,0,-1):
    print(i)

#2438
N=int(input())
for i in range(1,N+1):
    print("*"*i)

#2438두번째풀이
N=int(input())
for i in range(N):
    print("*"*(i+1))

#2439
N=int(input())
for i in range(1,N+1):
    print(' '*(N-i),"*"*i,sep='')

#10871
N,X=map(int,input().split())
A=list(map(int,input().split()))
for i in A:
    if i < X:
        print(i, end=' ')

#while문

#10952
while True:
    A,B=map(int,input().split())
    if(A==0 and B==0):
        break
    else:
        print(A+B)

#10951
while True:
    try:
        A,B=map(int,input().split())
        print(A+B)
    except:
        break

#1110더하기사이클,*****
number=int(input())
cycle=1
N=number

while True:
    ten=int(N)//10
    one=int(N)%10
    new=ten+one
    N=str(one)+str(new%10)
    if int(N)==number:
        break
    else:
        cycle+=1
print(cycle)

#함수

#4673셀프넘버,*****
def A(n):
    a=0
    for NN in list(str(n)):
        a=a+int(NN)
    return int(n)+a
a=[]
for i in range(1,10001):
    y= A(i)
    a.append(y)
for b in range(1,10001):
    if b in a:
        pass
    else:
        print(b)
#15596
def solve(a):
    return sum(a)
