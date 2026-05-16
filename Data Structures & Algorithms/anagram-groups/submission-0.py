class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)

        for s in strs:
            key = self.get_key(s)
            anagram_map[key].append(s)

        return list(anagram_map.values())

    def get_key(self, input: str) -> tuple:
        key = [0] * 26
        for i in input:
            key[ord(i) - ord('a')] += 1
        
        return tuple(key)