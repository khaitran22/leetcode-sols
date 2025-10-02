# %%
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# class Solution:


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def valid(node, minimum, maximum):
            if not node:
                return True

            if not (node.val > minimum and node.val < maximum):
                return False

            return valid(node.left, minimum, node.val) and valid(node.right, node.val, maximum)

        return valid(root, float("-inf"), float("inf"))


# %%
# node_27 = TreeNode(27, None, None)
# node_56 = TreeNode(56, None, None)
# node_19 = TreeNode(19, None, node_27)
# node_47 = TreeNode(47, None, node_56)
# node_26 = TreeNode(26, node_19, None)
# root = TreeNode(32, node_26, node_47)
# isValidBST(root)


# %%
