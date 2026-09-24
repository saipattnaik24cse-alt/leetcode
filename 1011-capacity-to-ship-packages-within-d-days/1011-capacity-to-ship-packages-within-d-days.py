class Solution:
    def shipWithinDays(self, weights, days):
        left = max(weights)
        right = sum(weights)

        while left <= right:

            capacity = (left + right) // 2

            current_weight = 0
            required_days = 1

            for weight in weights:

                if current_weight + weight > capacity:
                    required_days += 1
                    current_weight = 0

                current_weight += weight

            if required_days <= days:
                right = capacity - 1
            else:
                left = capacity + 1

        return left