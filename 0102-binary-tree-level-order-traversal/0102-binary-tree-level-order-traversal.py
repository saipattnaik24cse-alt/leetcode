
from collections import deque

class Solution:
    def levelOrder(self, root):
        if not root:
            return []

        q = deque([root])
        result = []

        while q:
            level = []

            for i in range(len(q)):
                node = q.popleft()
                level.append(node.val)

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

            result.append(level)

        return result
        