def whatever_it_is(arr: list) -> list:
    alphabet = " abcdefghijklmnopqrstuvwxyz"
    result = []
    for string in arr:
        count_sum = 0
        for i in range(len(string)):
            num = alphabet.index(string[i])
            count_sum += num
        count = count_sum * (arr.index(string)+1)
        result.append(count)
    return result

print(whatever_it_is(["abcd", "efgh", "ijkl", "mnop", "pqrs", "tuv", "wxyz"]))



