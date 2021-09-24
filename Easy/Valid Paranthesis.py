class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        b_map = {
            '}': '{',
            ')': '(',
            ']': '['
        }

        for bracket in s:
            if bracket not in b_map:
                stack.append(bracket)
            elif stack and b_map[bracket] == stack[-1]:
                stack.pop(-1)
            else:
                return False

        return stack == []

#         while(len(s) > 0):

#             l = len(s)
#             s.replace('{}','').replace('()','').replace('[]','')


#             if(l == len(s)):
#                 print(l)
#                 return True

#         return False
