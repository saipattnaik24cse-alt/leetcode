from math import isqrt
from typing import List

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        left = 1
        right = min(ranks) * cars * cars

        while left < right:
            mid = (left + right) // 2
            total = sum(isqrt(mid // rank) for rank in ranks)

            if total >= cars:
                right = mid
            else:
                left = mid + 1

        return left
        