def selection_sort(nums):
    for i in range(len(nums)):
        min_idx = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[min_idx]:
                min_idx = j
        nums[i], nums[min_idx] = nums[min_idx], nums[i]
n = int(input("Enter a total number: "))
nums = [0] * n
for i in range(n):
    val = int(input(f"Enter number {i + 1}: "))
    nums[i] = val
selection_sort(nums)
print(nums)
