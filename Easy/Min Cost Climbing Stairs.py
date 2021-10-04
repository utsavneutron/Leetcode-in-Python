def minCostClimbingStaris(self,cost):
    if not cost:
        return 0
    
    dp = [0] * len(cost)

    dp[0] = cost[0]

    if len(cost) >=2:
        dp[i] = cost[i] + min(dp[i-1],dp[i-2])
    return min(dp[-1],dp[-2])