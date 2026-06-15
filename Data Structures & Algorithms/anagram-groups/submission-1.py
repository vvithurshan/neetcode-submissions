class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        def help(s, t):

            if len(s) != len(t):
                return False

            d = {}

            for i in range(len(s)):
                d[s[i]] = d.get(s[i], 0) + 1
                d[t[i]] = d.get(t[i], 0) - 1

            return all([v == 0 for v in d.values()])


        isTaken = [0] * len(strs)
        ans = []

        for i in range(len(strs)):
            if isTaken[i]:
                continue
            sub = [strs[i]]
            isTaken[i] = True

            for j in range(i + 1, len(strs)):
                if (not isTaken[j]) and help(strs[i], strs[j]):
                    isTaken[j] = True
                    sub.append(strs[j])

            ans.append(sub)

        return ans


