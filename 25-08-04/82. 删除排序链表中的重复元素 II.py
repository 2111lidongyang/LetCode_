# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 创建虚拟头节点
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy  # pre指向当前已处理部分的最后一个节点
        
        while head:
            # 如果当前节点有重复
            if head.next and head.val == head.next.val:
                # 记录重复的值
                val = head.val
                # 跳过所有重复的节点
                while head and head.val == val:
                    head = head.next
                # 将pre连接到第一个不重复的节点
                pre.next = head
            else:
                # 没有重复，正常移动指针
                pre = head
                head = head.next
        
        return dummy.next


        
        

        