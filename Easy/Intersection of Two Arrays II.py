class Solution:
    def intersect(self, nums1, nums2):
        arr = []
        for i in range(len(nums1)):
            if nums1[i] in nums2:
                nums2.remove(nums1[i])
                arr.append(nums1[i])

        return arr
