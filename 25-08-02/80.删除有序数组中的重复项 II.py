"""
给你一个有序数组 nums ，请你 原地 删除重复出现的元素，使得出现次数超过两次的元素只出现两次 ，返回删除后数组的新长度。

不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。

"""

"""
输入：nums = [0,0,1,1,1,1,2,3,3]
输出：7, nums = [0,0,1,1,2,3,3]
解释：函数应返回新长度 length = 7, 并且原数组的前七个元素被修改为 0, 0, 1, 1, 2, 3, 3。不需要考虑数组中超出新长度后面的元素。
"""


from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # 最后返回数组的长度
        index_item = 0
        # 记录该元素出行的次数
        show_number = 0 
        # 上一次出行的数字
        last_item = nums[0]

        for i in nums:
            if i == last_item:
                if show_number == 0 or show_number == 1:  # 第一\二次出现
                    nums[index_item] = i
                    index_item += 1
                    show_number += 1
                else: # 三次以上的，啥也不用干
                    continue
            else:
                # 将该 i 插入 nums
                nums[index_item] = i
                index_item += 1
                last_item = i
                show_number = 1

        return index_item


        