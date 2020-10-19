class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        node_queue=[]
        node_queue.append(root)
        count=0
        index=1

        while(node_queue[0]!=None):
            count+=1
            temp_node=node_queue[0]
            #第1，3，7，15，31，63......的next为none
            if(count==index):
                temp_node.next=None
                index=index*2+1
            else:
                temp_node.next=node_queue[1]
            node_queue.append(temp_node.left)
            node_queue.append(temp_node.right)
            node_queue=node_queue[1:]

        return root


