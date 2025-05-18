for tt in range(int(input())):
    n = int(input())
    s1=[]
    s = list(map(int, input().split()))
    e = list(map(int, input().split()))
    for i in range(n):
        s1.append((s[i],e[i]))
    s1.sort(key = lambda x:x[1])
    #print(*s1)
    cout = 1;
    l = 0
    r = 1
    while r<n:
        if s1[r][0]> s1[l][1]:
            cout+=1
            l = r
        r+=1
    print(cout)