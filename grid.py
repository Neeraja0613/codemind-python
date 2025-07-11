def min_treasure_sum(grid):
    n = len(grid)
    dp = grid[0][:]  # Copy of first row

    for i in range(1, n):
        new_dp = [0] * n

        # Find the smallest and second smallest in previous row
        min1 = min2 = float('inf')
        idx1 = idx2 = -1
        for j in range(n):
            if dp[j] < min1:
                min2, idx2 = min1, idx1
                min1, idx1 = dp[j], j
            elif dp[j] < min2:
                min2, idx2 = dp[j], j

        for j in range(n):
            # Use second min if same column as previous min
            new_dp[j] = grid[i][j] + (min2 if j == idx1 else min1)

        dp = new_dp

    return min(dp)

# Input reading
n = int(input())
grid = []
for _ in range(n):
    row = list(map(int, input().split()))
    grid.append(row)

print(min_treasure_sum(grid))
