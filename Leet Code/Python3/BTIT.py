class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root):
        # iterative approach for inorder traversal
        """ We maintain a stack, first we make a pointer to the root node and then traverse the left of the tree until we reach null.

        As we traverse we keep on pushing the nodes in the stack

        When we reach null, the left-most node of the tree, we start poping the nodes and adding them in the Traversal list.
        
        Also when a node is poped we do traverse the right sub-tree of the node poped.
        """
        traversal = []
        stack = []
        current = root
        while current is not None or len(stack) != 0:   # this loop goes on till current reaches null(leaf node) and stack becomes empty(Traversal of the tree gets completed)
            while current is not None:
                stack.append(current)
                current = current.left
            current = stack[-1]
            t = stack.pop()
            traversal.append(t.val)
            current = current.right
        return traversal

if __name__ == "__main__":
    # simple tree is created no inputs taken
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)

    sol = Solution()
    li = sol.inorderTraversal(root)
    print(li)

