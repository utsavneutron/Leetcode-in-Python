class Solution:
    def sortedSquares(self, nums):
        a = []
        x = 0
        l = len(nums)

        for i in nums:
            a.append(i*i)

        a.sort()

        return a
