class Solution:
    def alphanum(self, c):
        
        if (ord('a') <= ord(c) <= ord('z')) or \
            (ord('A') <= ord(c) <= ord('Z')) or \
            (ord('0') <= ord(c) <= ord('9')):
            return True

        return False 

    def lower(self, c):

        if ord('a') <= ord(c) <= ord('z'): return c

        return chr(ord(c) + 32)

    def isPalindrome(self, s: str) -> bool:
        
        i, j = 0, len(s) - 1

        while i < j:
            
            while i < j and  not self.alphanum(s[i]): i += 1

            while i < j and not self.alphanum(s[j]): j -= 1

            if i < j and (self.lower(s[i]) != self.lower(s[j])):
                return False

            i += 1
            j -= 1

        return True


