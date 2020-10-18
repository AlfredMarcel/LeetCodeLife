# 给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        nodelist=[]
        tempnode=head
        nodelist.append(tempnode)
        while(tempnode.next!=None):
            tempnode=tempnode.next
            nodelist.append(tempnode)
        length=len(nodelist)
        if(length==1):
            return None
        elif n==1:
            nodelist[-2].next=None
        elif n==length:
            head=nodelist[1]
        else:
            nodelist[length-n-1].next=nodelist[length-n+1]

        return head