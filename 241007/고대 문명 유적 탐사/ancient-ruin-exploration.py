from collections import deque
import copy

K, M = map(int, input().split())
maps = []
for _ in range(5):
    maps.append(list(map(int, input().split())))
new_items = deque(list(map(int, input().split())))

def get(cur_map):
    visited = [[False]*5 for _ in range(5)]
    items = []

    def find(y,x,n):
        q = deque([[y, x]])
        visited[y][x] = True
        cur = []
        
        while q:
            cy, cx = q.popleft()
            cur.append([cy, cx])
            for ny, nx in [[cy-1, cx], [cy+1,cx], [cy,cx-1], [cy,cx+1]]:
                if ny>-1 and ny<5 and nx>-1 and nx<5:
                    if not visited[ny][nx] and cur_map[ny][nx]==n:
                        visited[ny][nx] = True
                        q.append([ny, nx])
        
        if len(cur)>2:
            items.extend(cur)
    
    for i in range(5):
        for j in range(5):
            if not visited[i][j]:
                find(i,j, cur_map[i][j])
    
    return items

def rotation(y, x, rot, change=False):
    maps_ = maps if change else copy.deepcopy(maps)
    map_3x3 = []
    for yy in range(y-1, y+2):
        map_3x3.append(maps_[yy][x-1:x+2].copy())
    if rot == 0:
        for yy in range(3):
            for xx in range(3):
                maps_[y-1+yy][x-1+xx] = map_3x3[2-xx][yy]

    elif rot==1:
        for yy in range(3):
            for xx in range(3):
                maps_[y-1+yy][x-1+xx] = map_3x3[2-yy][2-xx]
    
    elif rot==2:
        for yy in range(3):
            for xx in range(3):
                maps_[y-1+yy][x-1+xx] = map_3x3[xx][2-yy]
    
    return get(maps_)

def search():
    max_list = [0, 3, 5, 5, []]

    for y in range(1, 4):
        for x in range(1, 4):
            for rot in range(3):
                cur_item = rotation(y, x, rot, change=False)
                cur_list = [len(cur_item), rot, x, y, cur_item]
                max_list = sorted([max_list, cur_list], key=lambda x: [-x[0], x[1], x[2], x[3]])[0]
    if max_list[0]==0:
        return 0

    rotation(max_list[3], max_list[2], max_list[1], change=True)
    max_list[-1].sort(key=lambda x: [x[1], -x[0]])
    for [cy, cx] in max_list[-1]:
        maps[cy][cx] = new_items.popleft()
    
    ans = max_list[0]
    
    while True:
        cur_item = get(maps)
        if len(cur_item)==0:
            break
        ans += len(cur_item)
        cur_item.sort(key=lambda x: [x[1], -x[0]])
        for [cy, cx] in cur_item:
            maps[cy][cx] = new_items.popleft()

    
    return ans

answer_list = []
for k in range(K):
    answer = search()
    if answer==0:
        break
    
    answer_list.append(str(answer))

print(' '.join(answer_list))