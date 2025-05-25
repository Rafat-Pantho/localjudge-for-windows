"""
Author : Sinthia Alam
Date : 23-05-2025
"""
def dfs(node, visited, graph, money, group):
    visited[node] = True
    group['sum'] += money[node]
    group['count'] += 1
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(neighbor, visited, graph, money, group)

T = int(input())  # case number

for case_num in range(1, T + 1):
    n, m = map(int, input().split())  # n = num of people, m = connected number
    money = list(map(int, input().split()))  # the amount of money each person has

    graph = [[] for _ in range(n)]  # create graph

    for i in range(m):
        u, v = map(int, input().split())
        graph[u - 1].append(v - 1)
        graph[v - 1].append(u - 1)

    visited = [False] * n
    possible = True

    total_money = sum(money)
    if total_money % n != 0:
        possible = False
    else:
        target = total_money // n
        for i in range(n):
            if not visited[i]:
                group = {'sum': 0, 'count': 0}
                dfs(i, visited, graph, money, group)
                if group['sum'] % group['count'] != 0 or group['sum'] // group['count'] != target:
                    possible = False
                    break

    result = "Yes" if possible else "No"
    print(f"Case {case_num}: {result}")