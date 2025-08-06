"""
给定一个已排序的链表的头 head ， 删除所有重复的元素，使每个元素只出现一次 。返回 已排序的链表 。
"""

# 示例
"""
输入：head = [1,1,2]
输出：[1,2]

输入：head = [1,1,2,3,3]
输出：[1,2,3]
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 对于排序链表的去重，我们只需要跳过重复的节点，不需要记录当前链表的最后一个节点
        current = head
        
        while current and current.next:
            if current.val == current.next.val:
                # 跳过所有重复节点，只保留当前节点
                current.next = current.next.next
            else:
                # 只有当下一个节点值不同时才移动current
                current = current.next
                
        return head