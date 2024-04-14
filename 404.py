# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root) -> int:
        def sum_left_leaves(node):
            if node is None:
                return 0
            # Check if the left child is a leaf node
            if node.left and node.left.left is None and node.left.right is None:
                return node.left.val + sum_left_leaves(node.right)  # Add the value of left leaf and recursively search in the right subtree
            else:
                return sum_left_leaves(node.left) + sum_left_leaves(node.right)  # Recursively search in both subtrees
        result = sum_left_leaves(root)
        print("sum : ", result)
        return result

# Construct the binary tree
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

# Test the solution
s1 = Solution()
print(s1.sumOfLeftLeaves(root))