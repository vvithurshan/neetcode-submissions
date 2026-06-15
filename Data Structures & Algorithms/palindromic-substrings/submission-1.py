class Solution:
    def isPalindrome(self, subs):
        i = 0
        j = len(subs) - 1

        while i < j:
            if subs[i] != subs[j]:
                return False
            i += 1
            j -= 1
        return True
        
    def countSubstrings(self, s: str) -> int:

        cnt = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                if self.isPalindrome(s[i:j + 1]):
                    cnt += 1
        return cnt
