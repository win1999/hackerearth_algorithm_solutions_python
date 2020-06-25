x=int(input())
arr=list(map(int,input().split()))
z=sorted(arr)
s=z[0:x-1]
y=z[1:x]
print(sum(s),sum(y))
