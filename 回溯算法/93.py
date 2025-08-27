# class Solution:
#     def restoreIpAddresses(self, s: str) -> List[str]:
#         res = []
#         start_index = 0
#         number = 0
#         def is_ok(s):
#             if s[0] == "0" and len(s) > 1:
#                 return False
#             else:
#                 if 0 <= int(s) <= 255:
#                     return True
#                 return False
#         # 2.5525511135
#         def backtracking(start_index, s, number):
#             if number == 3:
#                 if len(s) <= 3:
#                     res.append(s[:])
#                 return
#             for i in range(start_index, len(s)):
#                 if is_ok(s[start_index: i + 1]):
#                     number += 1
#                     s = str(s[: i + 1] + '.' + s[i + 1:])
#                     backtracking(i + 2, s, number)
#                     s = str(s[:i + 1] + s[i + 2:])
#                     number -= 1
#                 else:
#                     break

#         backtracking(start_index, s, number)

#         return res
        

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        
        def is_valid(segment):
            # 检查段是否有效：0-255，无前导零
            if not segment or len(segment) > 3:
                return False
            if len(segment) > 1 and segment[0] == '0':
                return False
            return 0 <= int(segment) <= 255
        
        def backtrack(start_index, path, dots):
            # 如果已经有3个点，检查最后一段
            if dots == 3:
                last_segment = s[start_index:]
                if is_valid(last_segment):
                    res.append('.'.join(path + [last_segment]))
                return
            
            # 尝试1-3位数字作为当前段 255.255.111.35
            for i in range(start_index, min(start_index + 3, len(s))):
                segment = s[start_index:i + 1]
                if is_valid(segment):
                    path.append(segment)
                    backtrack(i + 1, path, dots + 1)
                    path.pop()  # 回溯
                else:
                    break
        
        backtrack(0, [], 0)
        return res