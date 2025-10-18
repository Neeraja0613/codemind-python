# cook your dish here
complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
T = int(input())
for _ in range(T):
    N = int(input())
    S = input().strip()
    result = ""
    for base in S:
        result += complement[base]
    print(result)
