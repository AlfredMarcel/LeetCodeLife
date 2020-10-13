# 给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
#
# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:

        temp1=head
        if(temp1==None):
            res=temp1
            return res

        elif(temp1.next==None):
            res=ListNode(temp1.val,temp1.next)
            return res

        else:
            temp2=temp1.next
            #两结点交换时，前一个结点next设为none
            temp1.next=None
            res_head=ListNode(temp2.val,temp1)
            res_temp=res_head.next

            while(temp2.next!=None):
                temp1=temp2.next
                if(temp1.next!=None):
                    temp2=temp1.next
                    # 两结点交换时，前一个结点next设为none
                    temp1.next=None
                    temp_node=ListNode(temp2.val,temp1)
                    res_temp.next=temp_node
                    res_temp=res_temp.next.next
                else:
                    res_temp.next=temp1
                    break

        return res_head

