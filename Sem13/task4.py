def hacks(hackers: list, security_level: int, increase: int) -> int:
    result = 0
    for i in range(len(hackers)):
        if hackers[i] > security_level:
            result += 1
        elif hackers[i] <= security_level:
            security_level += increase
    return result

print(hacks([3,6, 11, 14, 2, 7, 20], int(input()), int(input())))
