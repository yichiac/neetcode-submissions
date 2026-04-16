"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copyTable = {None: None}

        cur = head
        while cur:
            copy = Node(cur.val)
            copyTable[cur] = copy
            cur = cur.next
        
        cur = head
        while cur:
            copy = copyTable[cur]
            copy.next = copyTable[cur.next]
            copy.random = copyTable[cur.random]
            cur = cur.next
        
        return copyTable[head]