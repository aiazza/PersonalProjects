def twoSum(nums,target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    response = []
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if i != j and nums[i] + nums[j] == target:
                print([i,j])

number = [3,2,4,5,1]
target = 6
print(twoSum(number,target))