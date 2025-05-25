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
        for i in range(n):
            if not visited_keeper[i]:
                queue_keeper.append(i)
                group = {'sum':0, 'count':0}
                while queue_keeper:
                    curr = queue_keeper.popleft()
                    if not visited_keeper[curr]:
                        visited_keeper[curr] = 1
                        group['sum'] += money_info[curr]
                        group['count'] +=1
                        for j in adjencylist[curr]:
                            if not visited_keeper[j]:
                                queue_keeper.append(j)
                if group['sum']%group['count']!=0 or group['sum']//group['count'] != avg:
                    flag = 0
                    break
    print(f"Case {t+1}: {"Yes" if flag else "No"}")