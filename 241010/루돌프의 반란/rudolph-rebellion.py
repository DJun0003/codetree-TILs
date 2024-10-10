N, M, P, C, D = map(int, input().split())
maps = [[-1]*N for _ in range(N)]
santas = [[] for _ in range(P)]
scores = [0] * P
rr, rc = map(lambda x: x-1, map(int, input().split()))
maps[rr][rc] = P
for i in range(P):
    sp, sr, sc = map(lambda x: x-1, map(int, input().split()))
    santas[sp] = [sr, sc, False, -2]
    maps[sr][sc] = i

def inf(idx, move):
    if idx==-1:
        return
    santas[idx][0]+=move[0]
    santas[idx][1]+=move[1]
    if santas[idx][0]<0 or santas[idx][0]>=N or santas[idx][1]<0 or santas[idx][1]>=N:
        santas[idx][2] = True
    else:
        n_idx = maps[santas[idx][0]][santas[idx][1]]
        maps[santas[idx][0]][santas[idx][1]] = idx
        inf(n_idx, move)
             

def col(m, idx, move, is_ru):
    w = C if is_ru else D
    scores[idx] += w
    santas[idx][-1] = m
    santas[idx][0]+=move[0]*w
    santas[idx][1]+=move[1]*w
    if santas[idx][0]<0 or santas[idx][0]>=N or santas[idx][1]<0 or santas[idx][1]>=N:
        santas[idx][2] = True
    else:
        n_idx = maps[santas[idx][0]][santas[idx][1]]
        maps[santas[idx][0]][santas[idx][1]] = idx
        inf(n_idx, move)

def move_ru(m):
    global rr, rc
    near = [-1, 1e9, N, N]
    for i, (sr, sc, is_out, d_m) in enumerate(santas):
        if not is_out:
            l = (rr-sr)**2+(rc-sc)**2
            near = sorted([near, [i, l, sr, sc]], key=lambda x: [x[1], -x[2], -x[3]])[0]

    maps[rr][rc] = -1
    move = [0, 0]
    if (rr-near[-2])<0:
        rr += 1
        move[0]=1
    elif (rr-near[-2])>0:
        rr -= 1
        move[0]=-1
    if (rc-near[-1])<0:
        rc += 1
        move[1]=1
    elif (rc-near[-1])>0:
        rc -= 1
        move[1]=-1
    
    san_idx = maps[rr][rc]
    maps[rr][rc] = P
    if san_idx!=-1:
        col(m, san_idx, move, is_ru=True)

def move_santa(m):
    global santas

    def m_san(idx, move):
        cur = santas[idx][0:2]
        santas[idx][0] += move[0]
        santas[idx][1] += move[1]
        maps[cur[0]][cur[1]] = -1
        n_idx = maps[santas[idx][0]][santas[idx][1]]
        if n_idx==P:
            col(m, idx, [-move[0], -move[1]], is_ru=False)
        else:
            maps[santas[idx][0]][santas[idx][1]] = idx

    for i, (sr, sc, is_out, d_m) in enumerate(santas):
        if not is_out and m-d_m>1:
            r, c = rr-sr, rc-sc
            if r>0: moving = [1]
            elif r<0: moving = [-1]
            else: moving = [0]
            if c>0: moving.append(1)
            elif c<0: moving.append(-1)
            else: moving.append(0)

            can_move_r = maps[sr+moving[0]][sc]==-1 or maps[sr+moving[0]][sc]==P
            can_move_c = maps[sr][sc+moving[1]]==-1 or maps[sr][sc+moving[1]]==P
            
            if abs(r)>abs(c):
                if can_move_r:
                    m_san(i, [moving[0], 0])
                elif can_move_c:
                    m_san(i, [0, moving[1]])
            elif abs(r)<abs(c):
                if can_move_c:
                    m_san(i, [0, moving[1]])
                elif can_move_r:
                    m_san(i, [moving[0], 0])
            else:
                if r<0 and can_move_r:
                    m_san(i, [moving[0], 0])
                elif c>0 and can_move_c:
                    m_san(i, [0, moving[1]])
                elif r>0 and can_move_r:
                    m_san(i, [moving[0], 0])
                elif c<0 and can_move_c:
                    m_san(i, [0, moving[1]])
                    

for curm in range(M):
    move_ru(curm)
    move_santa(curm)

    for curi in range(P):
        if not santas[curi][2]:
            scores[curi] += 1

    # print(curm, '--------')
    # print([rr, rc])
    # print(santas)
    # print(scores)

    if sum(s[2] for s in santas)==P:
        break

print(' '.join(list(map(str, scores))))