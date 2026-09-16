class Solution:
    def fourSumCount(self, A, B, C, D):
        hashmap = {}
        count = 0

        for a in A:
            for b in B:
                total = a + b
                hashmap[total] = hashmap.get(total, 0) + 1

        for c in C:
            for d in D:
                total = c + d
                need = -total

                if need in hashmap:
                    count += hashmap[need]

        return count