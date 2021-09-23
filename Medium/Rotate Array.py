class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
  
  
  """

        # Slice Solution
        length = len(nums)
        j = k % length
        print(j)

        temp = nums[:length-j]
        print(temp)

        print(nums[-j:])
        nums[:length-j] = nums[-j:]

        nums[-j:] = temp
