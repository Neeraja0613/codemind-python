def is_easy_to_pronounce(s):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    count = 0
    for ch in s:
        if ch not in vowels:
            count += 1
            if count >= 4:
                return "NO"
        else:
            count = 0
    return "YES"
T = int(input())
for _ in range(T):
    N = int(input())
    S = input().strip()
    print(is_easy_to_pronounce(S))
