from collections import deque
L, Q = map(int, input().split())
cho_list = {}
cus_list = {} 

def eat_chobab(name, loop):
    x, n = cus_list[name]
    if x in cho_list[name]:
        if loop==0:
            n -= cho_list[name][x]
        else:
            key_list = list(cho_list[name].keys())


def make_chobab(x, name):
    if name in cho_list:
        cho_list[name][x] += 1
    else:
        cho_list[name] = {x:1}
    
    if name in cus_list:
        if cus_list[name][0] in cho_list[name]:
            eat_chobab(name, cus_list[name])
        if not eat_chobab(x, x):
            cus_list.remove(x)


def entry(x, name, n):
    cus_list[name] = [x,n]
    

def take_picture():
    total_chobabs = 0
    for cho in cho_list.values():
        total_chobabs += sum(cho.values())
    print(len(cus_list.keys()), total_chobabs)

def circle(t, new_t):
    global cus_list, cho_list
    cir, rest = divmod(new_t - t, L)
    total_t = L+rest if cir>0 else rest
    for name, [x, n] in cus_list.items():
        
    
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