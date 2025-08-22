class Solution:
    def letterCombinations(self, digits: str):
        if not digits:
            return []
        # 定义一个字典来映射数字和字母间的关系
        number_dict = {
            '0':"",
            '1':"",
            '2':"abc",
            '3':"def",
            '4':"ghi",
            '5':"jkl",
            '6':"mno",
            '7':"pqrs",
            '8':"tuv",
            '9':"wxyz",
        }
        
        res = []
        temp = ''
        res_len = len(digits)
        def backtracking(index, temp, digits):
            # 取结果
            if index == res_len:
                res.append(temp[:])
                return
            # 23
            in_str = number_dict.get(digits[index])
            if in_str:
                for i in in_str:
                    backtracking(index + 1, temp + i, digits)
               
        backtracking(0, temp, digits)
        return res