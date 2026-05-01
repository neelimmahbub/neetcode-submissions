class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        final = {}
        topK = []
                
        for num in nums:
            str_label = str(num)
            final.setdefault(str_label, 0)
            final[str_label] = final[str_label] + 1

        final = dict(sorted(final.items(), key=lambda item: item[1]))
        
        for i in range(k):  
            topK.append(int(final.popitem()[0]))

        return topK