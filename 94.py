from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def inorder_dfs(node):
            result_list = []
            if node is not None:
                result_list.extend(inorder_dfs(node.left))  # Traverse left subtree
                result_list.append(node.val)  # Append current node's value
                result_list.extend(inorder_dfs(node.right))  # Traverse right subtree
            return result_list
        
        result = inorder_dfs(root)
        return result

# construct the binary tree
# root = TreeNode(1)
# root.left = None
# root.right = TreeNode(2)
# root.right.left = TreeNode(3)

root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(6)
root.left.left = TreeNode(3)
root.left.right = TreeNode(1)
root.right.right = TreeNode(8)
root.right.left= TreeNode(7)
# Test the solution
s1 = Solution()
print(s1.inorderTraversal(root))