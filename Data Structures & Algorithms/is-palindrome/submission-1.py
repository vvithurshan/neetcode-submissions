class Solution:
    def reverse(self, text):
        rev = ""
        n = len(text)
        for i in range(n - 1, -1, -1):
            rev += text[i]

        return rev

    def isPalindrome(self, s: str) -> bool:
        string = ""
        for ch in s:
            if ch.isalnum():
                string += ch.lower()

        return string == self.reverse(string)

