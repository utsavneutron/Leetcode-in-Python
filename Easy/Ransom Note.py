class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for i in ransomNote:
            if(magazine.count(i) < ransomNote.count(i)):
                return False

        return True

        # print(ransomNote[0])
