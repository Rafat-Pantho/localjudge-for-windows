from collections import deque
def my_custome_dijkastra(n,edges_with_time_delay):
    dist =[float('inf')]*(n+1)
    visited = [0]*(n+1)
    dist[1]=0
    
    q = deque()
    q.append(1)
    visited[1]=1
    
    while q:
        u = q.popleft()
        visited[u]=0
        
        for c, time_delay in edges_with_time_delay[u]:
            if dist[c]>dist[u]+time_delay:
                dist[c]= dist[u]+time_delay
                if not visited[c]:
                    if q and dist[c]< dist[q[0]]:
                        q.appendleft(c)
                    else:
                        q.append(c)
                    visited[c] = 1
    return dist[1:]
n,m = map(int,input().split())

edges_with_time_delay = [[] for i in range(n+1)]

for i in range(m):
    u,v,time_delay = map(int,input().split())
    edges_with_time_delay[u].append((v,time_delay))

result = my_custome_dijkastra(n,edges_with_time_delay)
print(*result)