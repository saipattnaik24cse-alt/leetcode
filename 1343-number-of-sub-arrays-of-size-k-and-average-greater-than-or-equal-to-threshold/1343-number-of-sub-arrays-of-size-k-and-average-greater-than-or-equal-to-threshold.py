class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:

        count = 0

        
        windowsum = sum(arr[:k])

        if windowsum >= threshold * k:
            count += 1

       
        for i in range(k, len(arr)):

            
            windowsum += arr[i]
            windowsum -= arr[i - k]

            if windowsum >= threshold * k:
                count += 1

        return count