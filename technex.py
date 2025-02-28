def time_to_get_ticket(N):
    if N == 1 or N == 3:
        return 1  
    elif N == 2:
        return 2
    seconds = 0
    while N > 3:
        N -= 2 
        seconds += 1
    return seconds + 1  
    
t=int(input())
for i in range(t):
    N = int(input())
    print(time_to_get_ticket(N))
