class Solution:
    def subsetsWithDup(self, nums):
        res = []
        n = len(nums)
        nums.sort() # 去重需要先对数组进行排序(对于可能存在重复的元素，那么就要去重)

        def backtracking(index_start, temp):
            res.append(temp[:])
            for i in range(index_start, n):
                if nums[i] == nums[i - 1] and i > index_start:
                    # nums[i] == nums[i - 1]的意思为：当前遍历到的元素不能与上一个被弹出去的元素相同
                    # i > index_start的意思为：且当前遍历到的元素不是当前层的第一个选择
                    continue
                temp.append(nums[i])
                backtracking(i + 1, temp)
                temp.pop()
        backtracking(0, [])
        return res