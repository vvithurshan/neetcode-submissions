class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        sorteds1 = "".join(sorted(s1))
        for i in range(len(s2)-len(s1)+1):
            if sorteds1 == "".join(sorted(s2[i:i+len(s1)])):
                return True

        return False