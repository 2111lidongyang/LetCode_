class Solution:
    def combinationSum(self, candidates, target: int):
        res = []
        sum_ = 0
        temp = []
        start_index = 0
        target = target

        # 对list进行排序
        candidates.sort()


        def backtracking(sum_, temp, start_index, target):
            if sum_ > target:
                return '0'
            if sum_ == target:
                res.append(temp[:])  # 这里又忘记了
                return '1'

            # 2 3 6 7
            for i in range(start_index, len(candidates)):
                temp.append(candidates[i])
                sum_ += candidates[i]
                r = backtracking(sum_, temp, i, target)
                sum_ -= candidates[i]
                temp.pop()
                if r == '0':
                    break


        backtracking(sum_, temp, start_index, target)

        return res
        