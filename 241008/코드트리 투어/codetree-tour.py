from collections import deque
import heapq

Q = int(input())
build = list(map(int, input().split()))
N, M = build[1], build[2]
maps = [[0]*N for _ in range(N)]
connects = [[] for _ in range(N)]
for i in range(1, M+1):
    if maps[build[3*i]][build[3*i+1]]==0:
        maps[build[3*i]][build[3*i+1]] = build[3*i+2]
        maps[build[3*i+1]][build[3*i]] = build[3*i+2]
        connects[build[3*i]].append(build[3*i+1])
        connects[build[3*i+1]].append(build[3*i])
    else:
        maps[build[3*i]][build[3*i+1]] = min(maps[build[3*i]][build[3*i+1]], build[3*i+2])
        maps[build[3*i+1]][build[3*i]] = min(maps[build[3*i]][build[3*i+1]], build[3*i+2])

start = 0
product = []

def travel(st, des):
    visited = [False] * N
    visited[st] = True
    

    def dfs(cur, cost, ans):
        if cur==des:
            return min(ans, cost)
        
        for d in connects[cur]:
            if not visited[d]:
                visited[d] = True
                ans = dfs(d, cost+maps[cur][d], ans) 
                visited[d] = False
        
        return ans
    
    total_cost = dfs(st, 0, 1e9)
    
    return total_cost

def create(ids, rev, des):
    heapq.heappush(product, [travel(start, des)-rev, ids, rev, des])
     
def sell():
    if not product or product[0][0]>0:
        print(-1)
    else:
        print(heapq.heappop(product)[1])

def del_product(ids):
    for i in range(len(product)):
        if ids==product[i][1]:
            del product[i]
            heapq.heapify(product)
            break
        

def change_start(s):
    global start, product
    start = s
    new_product = []
    for pro in product:
        heapq.heappush(new_product, [travel(start, pro[-1])-pro[-2], pro[1], pro[2], pro[3]])
    product = new_product

for _ in range(Q-1):
    req = list(map(int, input().split()))

    if req[0]==200:
        create(req[1], req[2], req[3])
    elif req[0]==300:
        del_product(req[1])
    elif req[0]==400:
        sell()
    elif req[0]==500:
        change_start(req[1])