# 请判断一个链表是否为回文链表。

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        node_list=[]
        if head!=None:
            temp=head
            node_list.append(temp)
            while(temp.next!=None):
                temp=temp.next
                node_list.append(temp)

        length=len(node_list)
        flag=True
        if(length<2):
            return flag
        else:
            for i in range(length//2):
                if node_list[i].val!=node_list[length-1-i].val:
                    flag=False
                    break
            return flag

