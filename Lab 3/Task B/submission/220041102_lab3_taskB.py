from collections import deque
n, p = map(int, input().split())
adjencylist = [[] for i in range(n)]

for i in range(p):
    a1,a2 = map(int, input().split())
    adjencylist[a1-1].append(a2-1)
    adjencylist[a2-1].append(a1-1)

visisted_keeper = [0]*n 
size_keeper = []

for i in range(n):
    if not visisted_keeper[i]:
        q = deque([i])
        visisted_keeper[i]=1
        size = 1
        while q:
            curr =q.popleft()
            for j in adjencylist[curr]:
                if not visisted_keeper[j]:
                    q.append(j)
                    visisted_keeper[j]=1
                    size+=1
        size_keeper.append(size)

# sir sorry. To prepare for refer exam I couldn't study graphs problem.
# i learnt bfs in 2-1. I just implemented that here.