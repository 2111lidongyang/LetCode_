class Solution:
    def partition(self, s: str):
        # 回文串（Palindrome）是指一个字符串，从左向右读和从右向左读是完全一样的。
        # 换句话说，字符串关于其中心对称。
        res = []
        temp = []
        start_index = 0
        n = len(s)

        def is_huiwen(s, start_index, i):
            # 判断是否为回文串
            rg = i - start_index
            if rg <= 0:
                return True
            for j in range(rg):
                if s[i] != s[start_index]:
                    return False
                start_index += 1
                i -= 1
            return True

        def backtracking(start_index):

            if start_index >= n:
                res.append(temp[:])
                return
            # aab
            for i in range(start_index, n):
                if is_huiwen(s, start_index, i):
                    if i == start_index:
                        temp.append(s[i])
                    else:
                        temp.append(s[start_index: i - start_index + 1])
                else:
                    continue
                backtracking(i + 1)
                temp.pop()
        backtracking(start_index)
        return res
        