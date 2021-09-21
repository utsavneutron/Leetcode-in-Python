class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # if(len(numbers) == 2):
        #     return [1,2]

        # for i in range(0,len(numbers)):
        #     a = i+1
        #     while(a<len(numbers)):
        #         if(numbers[i] + numbers[a] == target):
        #             return [i+1,a+1]
        #         a += 1

        left, right = 0, len(numbers) - 1

        while(left < right):
            if(numbers[left] + numbers[right] == target):
                return [left+1, right+1]
            elif(numbers[left] + numbers[right] < target):
                left += 1
            else:
                right -= 1
