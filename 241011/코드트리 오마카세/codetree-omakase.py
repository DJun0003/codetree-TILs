from collections import deque
L, Q = map(int, input().split())
cho_list = [{} for _ in range(L)]
table_list = [[] for _ in range(L)]
cus_list = [] 

def make_chobab(x, name):
    if name in cho_list[x]:
        cho_list[x][name] += 1
    else:
        cho_list[x][name] = 1
    
    if table_list[x]:
        if not eat_chobab(x, x):
            cus_list.remove(x)


def eat_chobab(cus_id, table_id):
    if table_list[cus_id][1] in cho_list[table_id]:
        table_list[cus_id][2] -= cho_list[table_id][table_list[cus_id][1]]
        if table_list[cus_id][2] < 0:
            cho_list[table_id][table_list[cus_id][1]] = -table_list[cus_id][2]
            table_list[cus_id] = []
            return False
        else:
            cho_list[table_id].pop(table_list[cus_id][1])
            if table_list[cus_id][2] == 0:
                table_list[cus_id] = []
                return False
            else:
                return True
    
    return True
            


def entry(x, name, n):
    table_list[x] = [x, name, n]
    cus_list.append(x)
    if not eat_chobab(x, x):
        cus_list.pop()
        table_list[x] = []

def take_picture():
    total_chobabs = 0
    for table in cho_list:
        total_chobabs += sum(table.values())
    print(len(cus_list), total_chobabs)

def circle(t, new_t):
    global cus_list, cho_list
    cir, rest = divmod(new_t - t, L)
    total_t = L+rest if cir>0 else rest
    for idx in range(1, total_t+1):
        new_cus_list = []
        for x in cus_list:
            if eat_chobab(x, (x-(idx%L))):
                new_cus_list.append(x)
        cus_list = new_cus_list
    cho_list = cho_list[-rest:] + cho_list[:-rest]

    return new_t


curt = 0
for q in range(Q):
    request = list(input().split())
    curt = circle(curt, int(request[1]))

    if request[0] == '100':
        make_chobab(int(request[2]), request[3])
        # print(curt, '100', cho_list)
    elif request[0] == '200':
        entry(int(request[2]), request[3], int(request[4]))
        # print(curt, '200', cus_list, table_list)
    elif request[0]=='300':
        take_picture()
    
    # print(curt, cus_list)
    # print(table_list)
    # print(cho_list)