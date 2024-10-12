from collections import deque
L, N, Q = map(int, input().split())
maps = []
for _ in range(L):
    maps.append([[-1, x] for x in map(int, input().split())])

soliders = []
for n in range(N):
    r, c, h, w, k = map(int, input().split())
    cur_k = 0
    for i in range(r-1, r-1+h):
        for j in range(c-1, c-1+w):
            maps[i][j][0] = n
            if maps[i][j][1]==1:
                cur_k+=1
    soliders.append([r-1, c-1, h, w, k, k, cur_k])

def check(sol, d, visited):
    check_list = [False, []]
    if d[0]!=0: # up
        new_r = soliders[sol][0]+d[0] if d[0]==-1 else soliders[sol][0]+soliders[sol][2] 
        if new_r>=L or new_r<0:
            return check_list, visited
        for new_c in range(soliders[sol][1], soliders[sol][1]+soliders[sol][3]):
            if maps[new_r][new_c][1] == 2:
                return check_list, visited
            elif maps[new_r][new_c][0] > -1 and not visited[maps[new_r][new_c][0]]:
                check_list[1].append(maps[new_r][new_c][0])
                visited[maps[new_r][new_c][0]] = True
    
    elif d[1]!=0:
        new_c = soliders[sol][1]+d[1] if d[1]==-1 else soliders[sol][1]+soliders[sol][3]
        if new_c>=L or new_c<0:
            return check_list, visited
        for new_r in range(soliders[sol][0], soliders[sol][0]+soliders[sol][2]):
            if maps[new_r][new_c][1] == 2:
                return check_list, visited
            elif maps[new_r][new_c][0] > -1 and not visited[maps[new_r][new_c][0]]:
                check_list[1].append(maps[new_r][new_c][0])
                visited[maps[new_r][new_c][0]] = True
    
    check_list[0]=True
    return check_list, visited

def move(sol, d, delk):
    if d[0]!=0: # up
        if d[0]==1:
            rm_r = soliders[sol][0]
            new_r = soliders[sol][0]+soliders[sol][2]
        elif d[0]==-1:
            rm_r = soliders[sol][0]+soliders[sol][2]-1
            new_r = soliders[sol][0]+d[0]
        soliders[sol][0] += d[0]
        
        for new_c in range(soliders[sol][1], soliders[sol][1]+soliders[sol][3]):
            maps[new_r][new_c][0] = sol
            if maps[new_r][new_c][1]==1:
                soliders[sol][-1]+=1
            maps[rm_r][new_c][0] = -1
            if maps[rm_r][new_c][1]==1:
                soliders[sol][-1]-=1
        
    elif d[1]!=0: # up
        if d[1]==1:
            rm_c = soliders[sol][1]
            new_c = soliders[sol][1]+soliders[sol][3]
        elif d[1]==-1:
            rm_c = soliders[sol][1]+soliders[sol][3]-1
            new_c = soliders[sol][1]+d[1]
        soliders[sol][1] = soliders[sol][1]+d[1]
        
        for new_r in range(soliders[sol][0], soliders[sol][0]+soliders[sol][2]):
            maps[new_r][new_c][0] = sol
            if maps[new_r][new_c][1]==1:
                soliders[sol][-1]+=1
            maps[new_r][rm_c][0] = -1
            if maps[new_r][rm_c][1]==1:
                soliders[sol][-1]-=1
    
    if delk:
        soliders[sol][-2] -= soliders[sol][-1]
        if soliders[sol][-2] < 1:
            for r in range(soliders[sol][0], soliders[sol][0]+soliders[sol][2]):
                for c in range(soliders[sol][1], soliders[sol][1]+soliders[sol][3]):
                    maps[r][c][0] = -1
    


def move_solider(sol, d):
    if soliders[sol][-2] < 1:
        return False
    visited = [False] * N
    visited[sol] = True
    q = deque([[sol]])
    move_q = [sol]
    while q:
        cur_sol_list = q.popleft()
        for cur_sol in cur_sol_list:
            [can_move, n_sols], visited = check(cur_sol, d, visited)
            if not can_move:
                return False
            if n_sols:
                q.append(n_sols)
                move_q+=n_sols
    
    if d[0]!=0:
        move_q.sort(key=lambda x: soliders[x][0]*d[0])
    elif d[1]!=0:
        move_q.sort(key=lambda x: soliders[x][1]*d[1])
    # print(move_q)
    while move_q:
        cur_sol = move_q.pop()
        move(cur_sol, d, True if move_q else False)
    
# for ll in range(L):
#     print(maps[ll])
# print(soliders)

for _ in range(Q):
    qi, qd = map(int, input().split())
    if qd==0:
        qqd = [-1,0]
    elif qd==1:
        qqd = [0,1]
    elif qd==2:
        qqd = [1,0]
    elif qd==3:
        qqd = [0,-1]
    # print(qi-1, qd, qqd)
    
    move_solider(qi-1, qqd)
    
    # for ll in range(L):
    #     print(maps[ll])
    # print(soliders)
    
    # print('--')
    # print(maps)
    # print('--')

answer = 0
for final_sol in soliders:
    if final_sol[-2]>0:
        answer+= final_sol[-3]-final_sol[-2]
print(answer)