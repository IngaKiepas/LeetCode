''' 
Serialization is converting a data structure or object into a sequence of bits so that it can be stored in a file or memory
buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary search tree. There is no restriction on how your serialization/
deserialization algorithm should work. You need to ensure that a binary search tree can be serialized to a string, and this
string can be deserialized to the original tree structure.

The encoded string should be as compact as possible.
'''

import collections


class TreeNode(object):
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None
        
class Codec:
    def serialize(self, root):
        if not root:
            return "null"
        
        queue = collections.deque([root])
        result = []
        
        while queue:
            node = queue.popleft()
            if node:
                result.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append("null")
                
        return ",".join(result)
    
    def deserialize(self, data):
        if data == "null":
            return None
        
        values = data.split(",")
        root = TreeNode(int(values[0]))
        queue = collections.deque([root])
        i = 1
        
        while queue:
            node = queue.popleft()
            if values[i] != "null":
                node.left = TreeNode(int(values[i]))
                queue.append(node.left)
            i += 1
            
            if values[i] != "null":
                node.right = TreeNode(int(values[i]))
                queue.append(node.right)
            i += 1
        
        return root