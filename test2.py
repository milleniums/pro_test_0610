import sys
from typing import List
class BikeManager:
    def __init__(self, pre_node: List[int], capacity: int):
        self.pre_node = pre_node
        self.max_cap = capacity
        self.capacity = [capacity // 2] * len(pre_node)
        self.capacity[0] = sys.maxsize
        print("init = ",self.capacity)

    def rent_bikes(self, node_id: int, num: int) -> int:
        if num <= self.capacity[node_id]:
            if node_id == 0:
                return self.capacity[node_id]
            self.capacity[node_id] -= num
            return self.capacity[node_id]
        else:
            res = num - self.capacity[node_id]
            self.capacity[node_id] = 0
            self.rent_bikes(self.pre_node[node_id], res)
        return self.capacity[node_id]

    def return_bikes(self, node_id: int, num: int) -> int:
        cur = num + self.capacity[node_id]
        if cur > self.max_cap:
            self.capacity[node_id] = self.max_cap
            res = cur - self.max_cap
            self.rent_bikes(self.pre_node[node_id], res)
        else:
            return cur

    def reset(self) -> int:
        for i in range(len(self.pre_node)):
            if self.capacity[i] == 0 or self.capacity[i] == self.max_cap:
                self.capacity = self.max_cap // 2

    def get_top5_nodes(self) -> List[int]:
        ans = []
        dic = {}
        for i in range(len(self.pre_node)):
            dic[i] = self.capacity[i]
        sorted_dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)
        for i in range(len(sorted_dic)):
            ans.append(sorted_dic[i][0])
        return ans[1:6] if len(ans) >= 5 else ans

sol = BikeManager([-1,0,1,1,5,0,1,0],41)
print(sol.rent_bikes(2,31))
print(sol.capacity)
print(sol.rent_bikes(3, 45))
print(sol.capacity)
print(sol.get_top5_nodes())
print(sol.return_bikes(5,29))
print(sol.capacity)
