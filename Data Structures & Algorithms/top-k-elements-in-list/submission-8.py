class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = {}
        for i in nums: 
            if i not in result:
                result[i] = 0
            result[i] += 1
        e = sorted(result.values(),reverse=True)
        r = []
        for i in range(k): 
            for k1, v in result.items():
                if v == e[i]:
                    r.append(k1)
                    del result[k1]
                    break
        return r[:k]