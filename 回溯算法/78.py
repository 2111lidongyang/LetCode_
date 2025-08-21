# encoding: utf-8
# @author: DayDreamer
# @file: 78.py.py
# @time: 2025/8/19 20:11
# @desc:
"""
Your time is limited,So don't waste it living in someone else's life.
And most important,
Have the courage to follow your heart and intuition.
They somehow already know,
What you truly want to become,Everything else is secondary。
"""

## 本题的类型是回溯，递归求解子集。
class Solution:
    def subsets(self, nums):
        res = [] 
        n = len(nums)
        def backtracking(index_start, temp):
            res.append(temp[:]) 
            for i in range(index_start, n):
                temp.append(nums[i])
                backtracking(i + 1, temp)
                temp.pop()
        backtracking(0, [])
        return res


