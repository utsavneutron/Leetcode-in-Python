class Solution:
    @cache
    def tribonacci(self, n):
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        
        elif n == 3:
            return 2

        else:
            return self.tribonacci(n-3) + self.tribonacci(n-2) + self.tribonacci(n-1)







































