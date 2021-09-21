class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        i = len(nums)
        a = 0
        while(a<i):
            if(nums[a] == 0):
                nums.append(nums.pop(a))
                i -= 1
            else:
                a += 1
        
        
#           i = 0
#         n = len(nums)
#         while i < n:
#             if nums[i] == 0:
#                 nums.pop(i)
#                 n -= 1
#                 nums.insert(len(nums),0)
#             else:
#                 i += 1
        