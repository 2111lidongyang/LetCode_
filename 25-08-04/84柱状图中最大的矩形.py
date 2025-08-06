"""
给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。

求在该柱状图中，能够勾勒出来的矩形的最大面积。
"""

# 示例
"""
输入：heights = [2,1,5,6,2,3]
输出：10
解释：最大的矩形为图中红色区域，面积为 10
"""

class Solution:
    def largestRectangleArea(self, heights) -> int: 
        # 以示例 1 为例：我们需要考虑的只有怎么多种情况
        """
        21 215 2156 21562 215623
        15 156 1562 15623
        56 562 5623
        62 623
        23
        """   
        # 不不不，你还需要考虑一个鹤立鸡群的情况

        # 也就是一个双层循环就可以解决的问题
        def get_res(t_list):
            # 这个函数主要是计算每种可能的面积
            if not t_list:  # 处理空列表
                return 0
            # 获取这个列表中的最小值
            # 返回最小值 * len(t_list)
            return min(t_list) * len(t_list)

        def nomal():
            max_area = 0
            for i in range(len(heights) - 1):
                if i == len(heights) - 1:
                    # 最后一个元素直接跳出循环
                    break
                temp_list = [heights[i]]
                for j in heights[i + 1:]:
                    temp_list.append(j)
                    area = get_res(temp_list)
                    if area > max_area:
                        max_area = area 
            max_val = max(set(heights))
            # 如果最后的结果为 0，那就取max(list)
            if max_area == 0:
                return max_val
            elif max_area < max_val:
                return max_val
            else:
                return max_area

        # 当然先考虑一些特殊情况
        # 在这之前直接返回列表元素为 1 个的情况
        if len(heights) == 1:
            return heights[0]
        elif len(heights) == 2:
            if heights[0] == heights[1]:
                return sum(heights)
            elif 0 not in heights:
                return nomal()
            else:
                return max(heights)
        else:
            return nomal()


                



         
