class Solution:
    def isPalindrome(self, word):
        i, j = 0, len(word) - 1
        while i <= j:
            if word[i] != word[j]:
                return False
            i += 1
            j -= 1
        return True
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        longest = 0
        palindrome = []
        
        for i in range(len(s) - 1):
            for j in range(i+longest, len(s)):
                subword = s[i: j+1]
                if self.isPalindrome(subword):
                    palindrome.append(subword)
                    longest = len(subword)
        if not palindrome:
            return ''
        palindrome = sorted(palindrome, key = len)
        return palindrome[-1]
        