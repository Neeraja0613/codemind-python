from collections import Counter
T = int(input())
for i in range(T):
    N = int(input())
    candies = list(map(int, input().split()))
    freq = Counter(candies)
    max_freq = max(freq.values())
    candidates = [color for color, count in freq.items() if count == max_freq]
    print(min(candidates))
