# 100 Same Tree
# 
# Time complexity: O(n)
# Space complexity: O(h) where h is the height of the tree
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True

        if not p or not q or p.val != q.val:
            return False

        return (self.isSameTree(p.left, q.left) and
            self.isSameTree(p.right, q.right))