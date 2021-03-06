"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        res = []
        if root is None:
            return res
        res.append(root.val)
        for node in root.children:
            arr = self.preorder(node)
            for val in arr:
                res.append(val)
        return res
        
