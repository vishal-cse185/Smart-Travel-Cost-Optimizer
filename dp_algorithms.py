def min_cost_with_stops(n, flights, src, dst, K):
    dp = [float('inf')] * n
    dp[src] = 0

    for _ in range(K + 1):
        temp = dp.copy()

        for u, v, cost in flights:
            if dp[u] != float('inf'):
                temp[v] = min(temp[v], dp[u] + cost)

        dp = temp

    return dp[dst] if dp[dst] != float('inf') else -1