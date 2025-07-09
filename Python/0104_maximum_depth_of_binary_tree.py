# 104 Maximum Depth of Binary Tree
#
# 
# 
class Solution:
    # Time complexity: O(n) where n is the number of nodes
    # Space complexity: O(h) where h is the height of the tree
    def maxDepthRecursiveDFS(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
    

    # Time complexity: O(n)
    # Space complexity: O(n)
    def maxDepthBFS(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        level = 0
        q = deque([root])

        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            level += 1

        return level
    

    # Time complexity: O(n)
    # Space complexity: O(n)
    def maxDepthIterativeDFS(self, root: Optional[TreeNode]) -> int:
        if not root: 
            return 0
        
        stack = [[root, 1]]
        res = 0

        while stack:
            node, depth = stack.pop()
            if node:
                res = max(res, depth)
                stack.append([node.left, depth+1])
                stack.append([node.right, depth+1])

        return res