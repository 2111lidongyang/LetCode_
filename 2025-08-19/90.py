# encoding: utf-8
# @author: DayDreamer
# @file: 90.py
# @time: 2025/8/19 20:56
# @desc: 
"""
Your time is limited,So don't waste it living in someone else's life.
And most important,
Have the courage to follow your heart and intuition.
They somehow already know,
What you truly want to become,Everything else is secondary。
"""
# 本题的思路是：
# 1. 先去除重复元素
# 2. 然后递归求解子集
# 本题的类型是回溯，递归求解子集。
# TODO 需要先做第40题（去除重）
class Solution:
    def subsets(self, nums):
        res = []
        n = len(nums)

        def fun(i, temp):
            res.append(temp)
            for j in range(i, n):
                fun(j + 1, temp + [nums[j]])

        fun(0, [])
        return res

s = Solution()
print(s.subsets([1, 2, 3]))
