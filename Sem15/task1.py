def is_zero(num: int) -> bool:
    if num == 0:
        return True
    return False

def count_zero(numbers: str) -> int:
    count = 0
    lst = numbers.split()
    for i in range(len(lst)):
        lst[i] = int(lst[i])
    for v in range(len(lst)):
        if is_zero(lst[v]):
            count += 1
    return count

def count_non_zero(numbers: str) -> int:
    count = 0
    lst = numbers.split()
    for i in range(len(lst)):
        lst[i] = int(lst[i])
    for i in range(len(lst)):
        if not is_zero(lst[i]):
            count += 1
    return count

st = input()
print(count_zero(st), count_non_zero(st))