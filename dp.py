def knapsack_dp(C, n, v, w):
    dp = [[0 for _ in range(C + 1)] for _ in range(n + 1)]

    # Build DP table
    for i in range(1, n + 1):
        for j in range(C + 1):
            # dipilih
            if w[i - 1] <= j:
                dp[i][j] = max(
                    v[i - 1] + dp[i - 1][j - w[i - 1]],
                    dp[i - 1][j]
                )
            # tidak dipilih
            else:
                dp[i][j] = dp[i - 1][j]

    best_value = dp[n][C]

    # Tidak ada item yang dipilih
    if best_value == 0:
        return -1, -1

    # Backtracking untuk mencari total weight
    total_weight = 0
    j = C

    for i in range(n, 0, -1):
        if dp[i][j] != dp[i - 1][j]:
            total_weight += w[i - 1]
            j -= w[i - 1]

    return best_value, total_weight