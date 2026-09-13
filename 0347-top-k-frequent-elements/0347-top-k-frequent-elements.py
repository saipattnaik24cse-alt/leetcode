class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hashmap = {}

        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1

        sorted_nums = sorted(hashmap, key=hashmap.get, reverse=True)

        return sorted_nums[:k]