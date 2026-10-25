
class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack = []

        for asteroid in asteroids:
            alive = True

            while (alive and asteroid < 0
                   and stack and stack[-1] > 0):

                if stack[-1] < abs(asteroid):
                    stack.pop()

                elif stack[-1] == abs(asteroid):
                    stack.pop()
                    alive = False

                else:
                    alive = False

            if alive:
                stack.append(asteroid)

        return stack
