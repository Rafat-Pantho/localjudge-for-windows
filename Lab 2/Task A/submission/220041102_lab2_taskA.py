for tt in range (int(input())):
    n,x = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse = True)
    sum =0
    i =0
    while sum<x and i<n:
        sum+=a[i]
        i+=1
    print(i if sum>=x else -1)