def solution(numbers):
    first = [numbers[0]]
    second = [numbers[1]]
    for i in range(2, len(numbers)):
        x = numbers[i]
        count_first = sum(1 for a in first if a > x)
        count_second = sum(1 for b in second if b > x)
        if count_first > count_second:
            first.append(x)
            continue
        elif count_second > count_first:
            second.append(x)
            continue
        if len(first) < len(second):
            first.append(x)
            continue
        elif len(second) < len(first):
            second.append(x)
            continue
        first.append(x)
    return first + second
