class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        freq_s = {}
        freq_t = {}
        for i, char in enumerate(s):
            if char in freq_s:
                freq_s[char] += 1
            else:
                freq_s[char] = 1
            
            if t[i] in freq_t:
                freq_t[t[i]] += 1
            else:
                freq_t[t[i]] = 1

        # validate the frequency of characters is same
        # for key, value in freq_s.items():
        #     if value not in freq_t or freq_t[key] != value:
        #         return False
        # return True
        for i, value in enumerate(s):
            if value not in freq_t:
                return False
            if freq_s[value] != freq_t[value]:
                return False
        return True

