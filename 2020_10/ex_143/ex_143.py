# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        node_list=[]
        if head!=None:
            temp1=head
            node_list.append(temp1)
            while(temp1.next!=None):
                temp1=temp1.next
                node_list.append(temp1)

            length=len(node_list)
            head=node_list[0]
            temp = head
            if((length+2)%2==0):
                temp.next=node_list[-1]
                temp=temp.next
                for i in range(length//2-1):
                    temp.next=node_list[1+i]
                    temp=temp.next
                    temp.next=node_list[length-2-i]
                    temp=temp.next
                    #最后一个结点的next设置成None，否则就成环了
                    temp.next=None
            else:
                for i in range(length//2):
                    temp.next=node_list[length-1-i]
                    temp=temp.next
                    temp.next=node_list[1+i]
                    temp=temp.next

                    temp.next = None

t5=ListNode(5)
t4=ListNode(4,t5)
t3=ListNode(3,t4)
t2=ListNode(2,t3)
t=ListNode(1,t2)

a=Solution()
a.reorderList(t)
