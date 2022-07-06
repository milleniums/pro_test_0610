from typing import List
class Solution:
    def get_successful_num(self, interval: int, orders: List[List[int]]) -> int:
        pos = [[0] * 100] * 100
        cnt = 0
        flag = []
        for order in orders:
            day = order[0]
            p = order[1:]
            if day // interval not in flag:
                pos = [[0] * 100] * 100
            for i in range(0, len(p), 2):
                if pos[p[i]][p[i+1]] == 0:
                    print(p)
                    pos[p[i]][p[i + 1]] = 1
                    cnt += 1
                    flag.append(day // interval)
                    break
        return cnt

sol = Solution()
ret = sol.get_successful_num(4, [[0,17,8,11,15], [4,10,9],
                           [5,10,9,14,13],[5,14,13,10,9],[6,14,13],[7,14,13],[11,14,13]])
print(ret)