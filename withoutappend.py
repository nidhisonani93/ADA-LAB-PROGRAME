def sort(nums):
    for i in range(len(nums) - 1, 0, -1):
        for j in range(i):
            if nums[j] > nums[j + 1]:

                temp = nums[j]
                nums[j] = nums[j + 1]
                nums[j + 1] = temp
n = int(input("Enter a total number: "))

nums = [0] * n
for i in range(n):
    val = int(input(f"Enter number {i + 1}: "))
    nums[i] = val
sort(nums)
print(nums)