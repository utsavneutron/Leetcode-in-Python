class Solution:
    def maxSubArray(self, nums) -> int:

        newNum = maxTotal = nums[0]

        for i in range(1, len(nums)):
            newNum = max(nums[i], nums[i]+newNum)
            # print(newNum)
            maxTotal = max(newNum, maxTotal)
            print(maxTotal)
        return maxTotal
