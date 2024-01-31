from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        queue = [root]
        result = []
        while queue:
            length, count = len(queue), 0
            level_values = []
            while count < length:
                node = queue.pop(0)
                level_values.append(node.val)
                count += 1
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level_values)
        return result


if __name__ == "__main__":
    inputs = [
        TreeNode(val=3, left=TreeNode(val=9), right=TreeNode(val=20, left=TreeNode(val=15), right=TreeNode(val=7))),
        TreeNode(val=1),
        None,
    ]
    s = Solution()
    for root in inputs:
        print(s.levelOrder(root))