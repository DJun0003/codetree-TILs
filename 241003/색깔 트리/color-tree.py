from collections import deque

tree = {} # 0: pid, 1: color, 2: max_dep, 3: children
root = []

def check_max_dep(mid, cur_dep):
    global tree
    if tree[mid][2] < cur_dep:
        return False
    elif tree[mid][0] == -1:
        return True 
    return check_max_dep(tree[mid][0], cur_dep+1)
    

def add_node(mid, pid, color, max_dep):
    global tree
    if pid == -1:
        tree[mid] = [pid, color, max_dep, []]
        root.append(mid)
    elif check_max_dep(pid, 2):
        tree[mid] = [pid, color, max_dep, []]
        tree[pid][-1].append(mid)

def change_color(mid, color):
    global tree
    q = deque([mid])

    while q:
        cur_id = q.popleft()
        tree[cur_id][1] = color
        for child in tree[cur_id][3]:
            q.append(child)

def check_color(mid):
    print(tree[mid][1])


def check(cur_id, score):
    global tree
    cur_colors = set([tree[cur_id][1]])
    for child in tree[cur_id][3]:
        child_colors, score = check(child, score)
        cur_colors |= child_colors
    
    score += len(cur_colors)**2
    return cur_colors, score

def check_score():
    global root

    total_score = 0
    for r in root:
        _, tree_score = check(r, 0)
        total_score += tree_score
    
    print(total_score)


Q = int(input())
for _ in range(Q):
    k = list(map(int, input().split()))
    if k[0] == 100:
        add_node(k[1], k[2], k[3], k[4])
    elif k[0] == 200:
        change_color(k[1], k[2])
    elif k[0] == 300:
        check_color(k[1])
    elif k[0]==400:
        check_score()