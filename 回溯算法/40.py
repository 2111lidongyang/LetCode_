class Solution:
    def combinationSum2(self, candidates, target: int):
        res = []
        temp = []
        start_index = 0
        sum_ = 0
        n = len(candidates)
        candidates.sort()
        is_used = [0 for i in range(n)]

        def backtracking(start_index, temp, sum_):
            if sum_ > target:
                return
            elif sum_ == target:
                res.append(temp[:])
            # 1 1 2 5 6 7 10
            for i in range(start_index, n):
                if sum_ + candidates[i] > target:
                    break
                if candidates[i] == candidates[i -1] and  is_used[i - 1] == 0 and i > 0:  # 这里是关键（我不太清楚）
                    continue
                temp.append(candidates[i])
                is_used[i] = 1
                sum_ += candidates[i]
                backtracking(i + 1, temp, sum_)
                is_used[i] = 0
                sum_ -= candidates[i]
                temp.pop()


        backtracking(start_index, temp, sum_)
        return res