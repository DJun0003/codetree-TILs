from collections import deque
L, Q = map(int, input().split())
cho_list = {}
cus_list = {} 

def make_chobab(x, name):
    if name in cus_list and cus_list[name][0]==x:
        cus_list[name][1] -= 1
        if cus_list[name][1] == 0:
            cus_list.pop(name)
        return
    
    if name in cho_list:
        if x in cho_list[name]:
            cho_list[name][x] += 1
        else:
            cho_list[name][x] = 1
    else:
        cho_list[name] = {x:1}

def entry(x, name, n):
    if x in cho_list[name]:
        n -= cho_list[name][x]
        if n<0:
            cho_list[name][x] = -n
            return
        else:
            cho_list[name].pop(x)
            if n==0:
                return
    cus_list[name] = [x,n]
    
    

def take_picture():
    total_chobabs = 0
    for cho in cho_list.values():
        total_chobabs += sum(cho.values())
    print(len(cus_list.keys()), total_chobabs)

def circle(t, new_t):
    cir, rest = divmod(new_t - t, L)
    total_t = L+rest if cir>0 else rest
    rm_customers = []

    for name, [x, n] in cus_list.items():
        if name in cho_list:
            cho_x_list = list(cho_list[name].keys())
            l = len(cho_x_list)
            cho_x_list.sort(key=lambda k: x-k+l if x<k else x-k)
            
            for cho_x in cho_x_list:
                gap = x-cho_x+l if x<cho_x else x-cho_x
                if gap>total_t:
                    break
                n -= cho_list[name][cho_x]
                if n < 0:
                    cho_list[name][cho_x] = -n
                    rm_customers.append(name)
                    break
                elif n==0:
                    cho_list[name].pop(cho_x)
                    rm_customers.append(name)
                    break
                else:
                    cho_list[name].pop(cho_x)
                    cus_list[name][1] = n
    
    for name in cho_list.keys():
        new_cho_name = {}
        for cho_x, cho_v in cho_list[name].items():
            new_cho_name[(cho_x+rest)%L] = cho_v
        cho_list[name] = new_cho_name
    
    for name in rm_customers:
        cus_list.pop(name)
    
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
    # print(cho_list)