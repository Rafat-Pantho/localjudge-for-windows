n,x = map(int,input().split())
h = sorted(map(int,input().split()))
flag = 1
for i in range (n):
    if h[i+n]-h[i]<x :
        flag = 0
        break
print ("YES" if flag else "NO")