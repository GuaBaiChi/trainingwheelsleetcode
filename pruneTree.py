# https://leetcode.com/problems/binary-tree-pruning/
# 814. Binary Tree Pruning

# to make driver code you need to use this
# https://favtutor.com/blogs/tree-traversal-python-with-recursion


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        if root == None:
            return None

        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)

        if root.val == 0 and root.left == None and root.right == None:
            return None

        return root


# driver code
# https://www.geeksforgeeks.org/trim-given-binary-tree-for-any-subtree-containing-only-0s/


def inorderTraversal(root):
    answer = []

    inorderTraversalUtil(root, answer)
    return answer


def inorderTraversalUtil(root, answer):
    if root is None:
        return

    inorderTraversalUtil(root.left, answer)
    answer.append(root.val)
    inorderTraversalUtil(root.right, answer)
    return


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode()
    root.right = TreeNode(0)
    # root.left.left = TreeNode()
    # root.left.right = TreeNode()
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(1)

    solution = Solution()
    ReceivedRoot = solution.pruneTree(root)
    # inorderPrint(ReceivedRoot)
    print(inorderTraversal(root))
    print()
