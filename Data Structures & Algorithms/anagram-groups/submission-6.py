class Solution:
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final = defaultdict(list)
        for s in strs:
            anagram = ''.join(sorted(s))
            final[anagram].append(s)
        return list(final.values())


