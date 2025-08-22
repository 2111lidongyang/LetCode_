class Solution:
    def combinationSum3(self, k: int, n: int):
        res = []
        temp = []
        sum_ = 0
        def backtracking(start_index, temp, sum_):
            if sum_ > n:
                return
            if len(temp) >= k:
                if sum_ == n:
                    res.append(temp[:])
                return
            # 1 2 3 4 5 6 7 8 9
            for i in range(start_index, 10):
                if i > n - sum_:
                    break
                temp.append(i)
                sum_ += i
                backtracking(i + 1, temp, sum_)  

                temp.pop()  
                sum_ -= i

        backtracking(1, [], sum_)
        return res
        