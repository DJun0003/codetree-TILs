from collections import deque
import heapq

Q = int(input())
build = list(map(int, input().split()))
N, M = build[1], build[2]
graph = [{} for _ in range(N)]

for i in range(1, M+1):
    u, v, w = build[3*i:3*i+3]
    if v in graph[u]:
        graph[u][v] = min(w, graph[u][v])
        graph[v][u] = min(w, graph[v][u])
    else:
        graph[u][v] = w
        graph[v][u] = w

start = 0
total_products = []
canceled_products = {}
total_costs = []

def travel():
    global total_costs, start
    total_costs = [1e9]*N
    q = [[start, 0]]
    total_costs[start] = 0

    while q:
        cur, cost = heapq.heappop(q)
        if total_costs[cur]<cost:
            continue
        for des, w in graph[cur].items():
            n_cost = cost+w 
            if n_cost<total_costs[des]:
                total_costs[des]=n_cost
                heapq.heappush(q, [des,n_cost])

def create(ids, rev, des):
    heapq.heappush(total_products, [total_costs[des]-rev, ids, rev, des])
    canceled_products[ids] = False
     
def sell():
    if not total_products or total_products[0][0]>0:
        print(-1)
    else:
        product = heapq.heappop(total_products)
        if canceled_products[product[1]]:
            sell()
        else:
            print(product[1])

def del_product(ids):
    canceled_products[ids] = True
        
def change_start(s):
    global start, total_products, total_costs
    start = s
    travel()
    new_products = []
    for pro in total_products:
        heapq.heappush(new_products, [total_costs[pro[3]]-pro[2], pro[1], pro[2], pro[3]])
    total_products = new_products

travel()
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