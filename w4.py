#2884
A,B=input().split()
A=int(A)
B=int(B)
if B>=45:
    print(A,B-45)
else:
    if A==0:
        print(23,B+15)
    else:
        print(A-1,B+15)

#1065
N_str=input()
number_of_hansu=0

def f(a):
    if a<100:
        return True
    else:
        a=str(a)
        if int(a[1])-int(a[0])==int(a[2])-int(a[1]):
            return True

for b in range(1,int(N_str)+1):
    if f(b) == True:
        number_of_hansu+=1

print(number_of_hansu)
