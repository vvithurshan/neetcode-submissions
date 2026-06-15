class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        count = {}

        for ch in s:
            count[ch] = count.get(ch, 0) + 1

        for ch in t:
            if ch not in count:
                return False

            count[ch] = count.get(ch, 0) - 1
            if count[ch] == 0:
                count.pop(ch, None)
        
        if not count:
            return True
        return False