"""
给你一个 非严格递增排列 的数组 nums ，请你 原地 删除重复出现的元素，使每个元素 只出现一次 ，返回删除后数组的新长度。元素的 相对顺序 应该保持 一致 。然后返回 nums 中唯一元素的个数。

考虑 nums 的唯一元素的数量为 k ，你需要做以下事情确保你的题解可以被通过：

更改数组 nums ，使 nums 的前 k 个元素包含唯一元素，并按照它们最初在 nums 中出现的顺序排列。nums 的其余元素与 nums 的大小不重要。
返回 k 。
"""

"""
输入：nums = [0,0,1,1,1,2,2,3,3,4]
输出：5, nums = [0,1,2,3,4]
解释：函数应该返回新的长度 5 ， 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4 。不需要考虑数组中超出新长度后面的元素。
"""
from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        所谓的`原地`就是对nums进行修改
        """

        # 取数组中的第一个元素作为上一次标记的值
        now_item = nums[0]
        # 取 index_item 初始为 1， index_item 代表的意思为：当遍历到的 i 与上一次标记的值不同时，i 应该插到nums的哪个位置上。
        index_item = 1  # 默认取 1，是因为nums的第一个元素永远不会被修改。
        # 对数组进行遍历
        for i in nums:
            # 如果 i = now_item
            if i == now_item:
                continue
            else:
                # 如果不等于 将 i 赋值给数组的 index 
                nums[index_item] = i
                # 更新 now_item 的值为 i
                now_item = i
                # 更新 index_item 索引
                index_item += 1
        return index_item
            