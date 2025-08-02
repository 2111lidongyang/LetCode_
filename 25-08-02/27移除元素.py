"""
给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素。元素的顺序可能发生改变。然后返回 nums 中与 val 不同的元素的数量。

假设 nums 中不等于 val 的元素数量为 k，要通过此题，您需要执行以下操作：

更改 nums 数组，使 nums 的前 k 个元素包含不等于 val 的元素。nums 的其余元素和 nums 的大小并不重要。
返回 k。
"""

"""
示例：
输入：nums = [0,1,2,2,3,0,4,2], val = 2
输出：5, nums = [0,1,4,0,3,_,_,_]
解释：你的函数应该返回 k = 5，并且 nums 中的前五个元素为 0,0,1,3,4。
"""
from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # 初始化新数组的索引位置
        index_nums = 0
        # 遍历原数组中的每个元素
        for i in nums:
            # 如果当前元素不等于要移除的值
            if i != val:
                # 将该元素放到新数组的位置上
                nums[index_nums] = i
                # 新数组索引后移一位
                index_nums += 1
        # 返回新数组的长度
        return index_nums

        