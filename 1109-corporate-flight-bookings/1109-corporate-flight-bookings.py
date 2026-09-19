class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        diff = [0] * (n + 2)

        for start, end, passengers in bookings:
            diff[start] += passengers
            diff[end + 1] -= passengers

        ans = []
        current = 0

        for i in range(1, n + 1):
            current += diff[i]
            ans.append(current)

        return ans