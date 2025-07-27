def insertion_sort(nums):
    for i in range(1, len(nums)):
        temp = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > temp:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = temp

n = int(input("How many numbers do you want to enter? "))

nums = [0] * n
for i in range(n):
    nums[i] = int(input(f"Enter number {i + 1}: "))

insertion_sort(nums)
print("Sorted list:", nums)