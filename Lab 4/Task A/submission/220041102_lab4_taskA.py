import heapq

class heap_pair:
    def __init__(self,node,distance):
        self.node = node
        self.distance = distance
    def __lt__(self,other):
        return self.distance<other.distance
def my_custome_dijkastra(n,edges_with_time_delay):
    dist =[float('inf')]*(n+1)
    dist[1]=0
    
    q = []
    heapq.heappush(q,heap_pair(1,0))
    
    while q:
        temp_container = heapq.heappop(q)
        u = temp_container.node
        d = temp_container.distance
        
        if dist[u]<d:continue
        
        for c, time_delay in edges_with_time_delay[u]:
            if dist[c]>dist[u]+time_delay:
                dist[c]= dist[u]+time_delay
                heapq.heappush(q,heap_pair(c,dist[c]))
    return dist[1:]
n,m = map(int,input().split())

edges_with_time_delay = [[] for i in range(n+1)]

for i in range(m):
    u,v,time_delay = map(int,input().split())
    edges_with_time_delay[u].append((v,time_delay))

result = my_custome_dijkastra(n,edges_with_time_delay)
print(*result)