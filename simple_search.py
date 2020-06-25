x=int(input())
arr=list(map(int,input().split()))
b=int(input())
s=list(idx for idx, val in enumerate(arr) if(val==b))
for ele in s:
    print(ele)
