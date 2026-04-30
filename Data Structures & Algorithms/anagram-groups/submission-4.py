class Solution:
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final = []
        grouping = []
        i = 0 
        j = 0
        while i < len(strs): 
            i -= 1
            current_word = strs.pop(strs.index(strs[i + 1]))
            grouping.append(current_word)
            
            while j < len (strs):
                if len(current_word) == len(strs[j]) and sorted(current_word) == sorted(strs[j]):
                    j -= 1
                    anagram_word = strs.pop(strs.index(strs[j + 1]))
                    grouping.append(anagram_word)
                    j += 1
                else:
                    j += 1
            i += 1 
            j = 0
            final.append(grouping)
            grouping = []
        return final

