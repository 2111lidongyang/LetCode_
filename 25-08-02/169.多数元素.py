"""
给定一个大小为 n 的数组 nums ，返回其中的多数元素。多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。

你可以假设数组是非空的，并且给定的数组总是存在多数元素。
"""

from typing import List
# 我的代码
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # 记录每个元素出现的次数
        item_dict = {}
        max_item = None
        max_number = 0
        for i in nums:
            number = item_dict.get(i, 0) + 1
            if number > max_number and number > len(nums) / 2:
                max_number = number
                max_item = i
            item_dict[i] =  number
        return max_item  # type: ignore
            
        



# AI 给的代码
from collections import Counter
class Solution_:
    def majorityElement(self, nums: List[int]) -> int:
        # 原代码使用哈希表记录每个元素出现次数，在遍历过程中找出出现次数超过半数的元素
        # 以下提供几种不同的优化写法

        # 方法一：使用 collections.Counter 更简洁的统计元素出现次数
        counter = Counter(nums)
        return counter.most_common(1)[0][0]

        # 方法二：摩尔投票法，时间复杂度 O(n)，空间复杂度 O(1)
        # 此方法更为高效，特别适合处理大规模数据
        # candidate = None
        # count = 0
        # for num in nums:
        #     if count == 0:
        #         candidate = num
        #         count = 1
        #     elif num == candidate:
        #         count += 1
        #     else:
        #         count -= 1
        # return candidate
        