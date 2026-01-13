def solution(n, s, a, b, fares):
    INF = float('inf')
    dist = [[INF] * (n + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        dist[i][i] = 0
        
    for u, v, w in fares:
        dist[u][v] = w
        dist[v][u] = w
        
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    min_cost = dist[s][a] + dist[s][b]
    
    for k in range(1, n + 1):
        current_cost = dist[s][k] + dist[k][a] + dist[k][b]
        min_cost = min(min_cost, current_cost)
        
    return min_cost