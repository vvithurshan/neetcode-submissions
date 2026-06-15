class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 0:
            return [strs]
        if len(strs) == 1:
            return [strs]

        vocab = {}

        for s in strs:
            if "".join(sorted(s)) in vocab:
                vocab["".join(sorted(s))].append(s)
            else:
                vocab["".join(sorted(s))] = [s]
        
        ans = []
        for key, val in vocab.items():
            ans.append(val)
        return ans
        