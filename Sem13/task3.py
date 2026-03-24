def consecutive_operation(st: str) -> list:
    if len(st) != 10:
        return "Invalid input"
    lst = st.split(", ")
    result = []
    for i in range (len(lst)):
        lst[i] = int(lst[i])
    for i in range(1, len(lst)):
        if lst[i] - lst[i - 1] != 1:
            return "Not consecutive"
    number = (lst[0] * lst[1] * lst[2] * lst[3] + 1)
    result.append(number)
    result.append(number ** 0.5)
    return result

print(consecutive_operation(input()))