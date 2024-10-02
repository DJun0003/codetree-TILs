from collections import deque

R, C, K = map(int, input().split())
maps = [[-1] * C for _ in range(R+3)]

def reset_maps():
    global maps
    maps = [[-1] * C for _ in range(R+3)]

def move_(cur):
    r, c, k = cur

    # move down
    if maps[r+2][c] == -1 and maps[r+1][c-1] == -1 and maps[r+1][c+1] == -1:
        maps[r-1][c] = maps[r][c-1] = maps[r][c+1] = -1
        maps[r+1][c] = 1
        maps[r][c] = maps[r+2][c] = maps[r+1][c-1] = maps[r+1][c+1] = 0
        return True, [r+1, c, k]
        
    # move left-down
    elif c>1 and maps[r][c-2] == -1 and maps[r-1][c-1]==-1 and maps[r+1][c-1]==-1 and maps[r+1][c-2]==-1 and maps[r+2][c-1]==-1:
        maps[r][c] = maps[r-1][c] = maps[r][c+1] = -1
        maps[r+1][c-1] = 1
        maps[r+1][c-2] = maps[r+2][c-1] = 0
        k = k-1 if k-1>0 else 3
        return True, [r+1, c-1, k]
    
    # move right-down
    elif c<C-2 and maps[r][c+2] == -1 and maps[r-1][c+1]==-1 and maps[r+1][c+1]==-1 and maps[r+1][c+2]==-1 and maps[r+2][c+1]==-1:
        maps[r][c] = maps[r-1][c] = maps[r][c-1] = -1
        maps[r+1][c+1] = 1
        maps[r+1][c+2] = maps[r+2][c+1] = 0
        return True, [r+1, c+1, (k+1)%4]
    
    return False, [r, c, k]

def move_angel(cur):
    r, c, _ = cur
    q = deque([[r,c]])
    visited = [[False] * C for _ in range(R+3)]
    visited[r][c] = True
    max_r = r
    while q:
        cr, cc = q.popleft()
    
        for mr, mc in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
            nr, nc = cr+mr, cc+mc
            if nr > R+2 or nr < 3 or nc < 0 or nc > C-1:
                continue
            
            if maps[cr][cc] == 0 and maps[nr][nc] == 1 and visited[nr][nc]==False:
                visited[nr][nc]=True
                q.append([nr, nc])
            elif maps[cr][cc]==2 and maps[nr][nc]==0 and visited[nr][nc]==False:
                visited[nr][nc]=True
                q.append([nr, nc])
            elif maps[cr][cc]==1:
                if max_r < nr:
                    max_r = nr
                if maps[nr][nc]==0 and visited[nr][nc]==False:
                    visited[nr][nc]=True
                elif maps[nr][nc]==2 and visited[nr][nc]==False:
                    visited[nr][nc]=True
                    q.append([nr,nc])
    
    return max_r                 



def move(cur):
    new_cur = cur.copy()
    while True:
        is_move, new_cur = move_(new_cur)
        if is_move == False or new_cur[0] == R+1:
            break
    
    r, c, k = new_cur
    if r < 4:
        reset_maps()
        ans = 0
    
    else:
        if k==0:
            maps[r-1][c] = 2
        elif k==1:
            maps[r][c+1] = 2
        elif k==2:
            maps[r+1][c] = 2
        elif k==3:
            maps[r][c-1] = 2
        
        ans = move_angel(new_cur)-2
    return ans


answer = 0
for i in range(K):
    c, e = map(int, input().split())
    answer += move([0, c-1, e])

print(answer)