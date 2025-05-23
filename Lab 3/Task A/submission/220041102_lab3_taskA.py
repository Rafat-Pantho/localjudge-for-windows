from collections import deque

for t in range(int(input())):
    n,m= map(int, input().split())
    
    money_info = list(map(int, input().split()))
    adjencylist = [[] for i in range(n)]
    tot = sum(money_info)
    
    for i in range (m):
        u,v = map(int, input().split())
        adjencylist[u-1].append(v-1)
        adjencylist[v-1].append(u-1)
    
    flag = 1
    
    if tot%n!=0: flag = 0
    else:
        avg = tot//n
        visited_keeper = [0]*n
        queue_keeper =  deque()
        