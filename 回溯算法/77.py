# 77. 组合
# 教程链接： 【带你学透回溯算法-组合问题（对应力扣题目：77.组合）| 回溯法精讲！】 https://www.bilibili.com/video/BV1ti4y1L7cv/?share_source=copy_web&vd_source=6efdc1334fc2826b67f7d5693aac2513

class Solution:
    def combine(self, n: int, k: int):
        # 1 2 3 4 
        res = []
        temp = []
        def backtracking(n, k, start_index, temp):
            if len(temp) >= k:
                res.append(temp[:])  # 注意这里的temp[:],我一开始写的是temp,结果出错了
                # 这里的temp[:]是深拷贝,如果直接写temp,那么res中的元素会随着temp的变化而变化
                return
            for i in range(start_index, n + 1):
                temp.append(i)
                backtracking(n, k, i + 1, temp)
                temp.pop()

        backtracking(n, k, 1, temp)

        return res
        
# 优化，减枝操作，减少不必要的遍历
# 例如 n = 4, k = 3
# 当遍历到 2 时，还需要 3 - 1 = 2 个元素，但是 4 后面只有 1 个元素了，所以 2 后面的元素就没有必要遍历了

class Solution1:
    def combine(self, n: int, k: int):
        # 1 2 3 4 
        res = []
        temp = []
        def backtracking(n, k, start_index, temp):
            if len(temp) >= k:
                res.append(temp[:])
                return
            for i in range(start_index, n - (k - len(temp)) + 2):  # 减枝操作， 为什么是 n - (k - len(temp)) + 2 ？
                # 例如 n = 4, k = 3
                # 当遍历到 2 时，还需要 3 - 1 = 2 个元素，但是 4 后面只有 1 个元素了，所以 2 后面的元素就没有必要遍历了
                # 所以这里的范围是 start_index, n - (k - len(temp)) + 2
                # 这里的 n - (k - len(temp)) + 2 是因为要包含最后一个元素，所以要 + 1， 又因为是从 start_index 开始遍历的，所以要再 + 1
                temp.append(i)
                backtracking(n, k, i + 1, temp)
                temp.pop()

        backtracking(n, k, 1, temp)

        return res