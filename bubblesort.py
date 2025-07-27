def sort(nums):
    n=len(nums)
    for i in range(n):
        for j in range(0, n-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j + 1]=nums[j+1],nums[j]
nums=[1,3,5,4,2]
print("Original array:", nums)
sort(nums)
print(nums)
