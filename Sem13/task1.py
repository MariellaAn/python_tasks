st = input()
nums = st.split()
for i in range(len(nums)):
    nums[i] = int(nums[i])
def is_positive(num: int) -> bool:
    if num >= 0:
        return True
    else:
        return False
def count_positive(numbers: list) -> int:
    count = 0
    for v in range(len(numbers)):
        if is_positive(numbers[v]):
            count += 1
    return count
def count_negative(numbers: list) -> int:
    count = 0
    for f in range(len(numbers)):
        if numbers[f] < 0:
            count += 1
    return count
print(f"Количество положительных чисел: {count_positive(nums)}")
print(f"Количество отрицательных чисел: {count_negative(nums)}")