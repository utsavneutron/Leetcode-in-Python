class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dic = {}
        for item in nums:
            dic[item] = dic.get(item, 0) + 1
        for key, val in dic.items():
            if val != 1:
                return True
