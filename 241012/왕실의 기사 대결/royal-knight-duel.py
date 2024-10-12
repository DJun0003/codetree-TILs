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

def check(sol, d):
    check_list = [False, []]
    if d[0] == 1 or d[0]==-1: # up
        new_r = soliders[sol][0]+d[0]
        if d[0]==1:
            new_r+= soliders[sol][2]-1
        if new_r==L or new_r==-1:
            return check_list
        for new_c in range(soliders[sol][1], soliders[sol][1]+soliders[sol][3]):
            if maps[new_r][new_c][1] == 2:
                return check_list
            elif maps[new_r][new_c][0] > -1:
                check_list[1].append(maps[new_r][new_c][0])
    
    elif d[1] == 1 or d[1]==-1:
        new_c = soliders[sol][1]+d[1]
        if d[1]==1:
            new_c+= soliders[sol][3]-1
        # print(soliders[sol][0], new_c)
        if new_c==L or new_c==-1:
            return check_list
        for new_r in range(soliders[sol][0], soliders[sol][0]+soliders[sol][2]):
            if maps[new_r][new_c][1] == 2:
                return check_list
            elif maps[new_r][new_c][0] > -1:
                check_list[1].append(maps[new_r][new_c][0])
    
    check_list[0]=True
    return check_list

def move(sol, d, delk):
    if d[0]==1 or d[0]==-1: # up
        bf_r = soliders[sol][0]
        new_r = bf_r+d[0]
        soliders[sol][0] = new_r
        if d[0]==1:
            new_r+= soliders[sol][2]-1
        
        for new_c in range(soliders[sol][1], soliders[sol][1]+soliders[sol][3]):
            maps[new_r][new_c][0] = sol
            if maps[new_r][new_c][1]==1:
                soliders[sol][-1]+=1
            maps[bf_r][new_c][0] = -1
            if maps[bf_r][new_c][1]==1:
                soliders[sol][-1]-=1
        
    elif d[1] == 1 or d[1]==-1: # up
        bf_c = soliders[sol][1]
        new_c = bf_c+d[1]
        soliders[sol][1] = new_c
        if d[1]==1:
            new_c+= soliders[sol][3]-1
        
        for new_r in range(soliders[sol][0], soliders[sol][0]+soliders[sol][2]):
            maps[new_r][new_c][0] = sol
            if maps[new_r][new_c][1]==1:
                soliders[sol][-1]+=1
            maps[new_r][bf_c][0] = -1
            if maps[new_r][bf_c][1]==1:
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
    
    q = deque([[sol]])
    move_q = deque([[sol]])
    while q:
        cur_sol_list = q.popleft()
        for cur_sol in cur_sol_list:
            can_move, n_sols = check(cur_sol, d)
            # print(sol, cur_sol, can_move, n_sols)
            if not can_move:
                return False
            if n_sols:
                q.append(n_sols)
                move_q.appendleft(n_sols)
    
    while move_q:
        cur_sol_list = move_q.popleft()
        if not cur_sol_list:
            continue
        for cur_sol in cur_sol_list:
            move(cur_sol, d, True if move_q else False)
    
    
for _ in range(Q):
    qi, qd = map(int, input().split())
    if qd==0:
        qdd=[-1,0]
    elif qd==1:
        qqd=[0,1]
    elif qd==2:
        qqd=[1,0]
    elif qd==3:
        qqd=[0,-1]
    move_solider(qi-1, qqd)
    # print(soliders)
    # print('--')
    # print(maps)
    # print('--')

answer = 0
for final_sol in soliders:
    if final_sol[-2]>0:
        answer+= final_sol[-3]-final_sol[-2]
print(answer)