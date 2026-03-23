def solve(word: str) -> str:
    result = ""
    count_up = 0
    count_low = 0
    for i in range(len(word)):
        if word[i].isupper():
            count_up += 1
        else:
            count_low += 1
    if count_up > count_low:
        for i in range(len(word)):
            if word[i].islower():
                result += word[i].upper()
            else:
                result += word[i]
    elif count_low > count_up:
        for i in range(len(word)):
            if word[i].isupper():
                result += word[i].lower()
            else:
                result += word[i]
    else:
        result = word.lower()
    return result
print(solve(input()))