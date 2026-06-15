class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        for id, i in enumerate(zip(*strs)):
            if len(set(i)) > 1:
                return strs[0][:id]

        return min(strs, key=len)