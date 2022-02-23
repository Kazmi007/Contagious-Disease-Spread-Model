import math
import random
from evaluator import *


def new_move():
    global i_state
    m = i_state[0]
    n = i_state[1]
    d = i_state[2]
    k_ = i_state[3]
    lambda_ = i_state[4]
    mu = i_state[5]
    p = deepcopy(i_state[6])
    dir_l = ['f', 'fr', 'r', 'br', 'b', 'bl', 'l', 'fl']
    pp = deepcopy(p)
    for i in pp:
        dir_s = random.choices(dir_l,
                               weights=[mu / 2, mu / 8, (1 - mu - (mu ** 2)) / 2,
                                        (2 * (mu ** 2)) / 5, (mu ** 2) / 5, (2 * (mu ** 2)) / 5,
                                        (1 - mu - (mu ** 2)) / 2, mu / 8], k=1)
        offset = i[1]
        if dir_s == ['f']:
            pos = tuple(map(sum, zip(i[0], revolve((0, 1), offset))))
            if 0 <= pos[0] < n and 0 <= pos[1] < m:
                i[0] = pos
                i[1] = ((0 + offset) % 8)
        if dir_s == ['fl']:
            pos = tuple(map(sum, zip(i[0], revolve((1, 1), offset))))
            if 0 <= pos[0] < n and 0 <= pos[1] < m:
                i[0] = pos
                i[1] = ((7 + offset) % 8)
        if dir_s == ['fr']:
            pos = tuple(map(sum, zip(i[0], revolve((-1, 1), offset))))
            if 0 <= pos[0] < n and 0 <= pos[1] < m:
                i[0] = pos
                i[1] = ((1 + offset) % 8)
        if dir_s == ['l']:
            pos = tuple(map(sum, zip(i[0], revolve((1, 0), offset))))
            if 0 <= pos[0] < n and 0 <= pos[1] < m:
                i[0] = pos
                i[1] = ((6 + offset) % 8)
        if dir_s == ['r']:
            pos = tuple(map(sum, zip(i[0], revolve((-1, 0), offset))))
            if 0 <= pos[0] < n and 0 <= pos[1] < m:
                i[0] = pos
                i[1] = ((2 + offset) % 8)
        if dir_s == ['bl']:
            pos = tuple(map(sum, zip(i[0], revolve((1, -1), offset))))
            if 0 <= pos[0] < n and 0 <= pos[1] < m:
                i[0] = pos
                i[1] = ((5 + offset) % 8)
        if dir_s == ['br']:
            pos = tuple(map(sum, zip(i[0], revolve((-1, -1), offset))))
            if 0 <= pos[0] < n and 0 <= pos[1] < m:
                i[0] = pos
                i[1] = ((3 + offset) % 8)
        if dir_s == ['b']:
            pos = tuple(map(sum, zip(i[0], revolve((0, -1), offset))))
            if 0 <= pos[0] < n and 0 <= pos[1] < m:
                i[0] = pos
                i[1] = ((4 + offset) % 8)
    for i in range(len(p)):
        wait = False
        for j in range(len(pp)):
            if p[i][0] == pp[j][0]:
                wait = True
        if not wait:
            p[i] = pp[i]
    q = deepcopy(p)
    for i in range(len(p)):
        for j in range(i + 1, len(p)):
            distance = math.sqrt((p[j][0][0] - p[i][0][0]) ** 2 + (p[j][0][1] - p[i][0][1]) ** 2)
            if distance <= d:
                if p[i][2] == 'masked':
                    if p[j][2] == 'masked':
                        if not (p[i][3] == p[j][3]):
                            states = ['inf', 'n_inf']
                            state = random.choices(states, weights=[((min(1, (k_ / (distance ** 2)))) / lambda_ ** 2),
                                                                    (1 - ((min(1,
                                                                               (k_ / (
                                                                                       distance ** 2)))) / lambda_ ** 2))],
                                                   k=1)
                            if state == ['inf']:
                                q[i][3] = 'infected'
                                q[j][3] = 'infected'
                    else:
                        if not (p[i][3] == p[j][3]):
                            states = ['inf', 'n_inf']
                            state = random.choices(states, weights=[((min(1, (k_ / (distance ** 2)))) / lambda_),
                                                                    (1 - ((min(1,
                                                                               (k_ / (distance ** 2)))) / lambda_))],
                                                   k=1)
                            if state == ['inf']:
                                q[i][3] = 'infected'
                                q[j][3] = 'infected'
                elif p[j][2] == 'masked':
                    if not (p[i][3] == p[j][3]):
                        states = ['inf', 'n_inf']
                        state = random.choices(states, weights=[((min(1, (k_ / (distance ** 2)))) / lambda_),
                                                                (1 - ((min(1,
                                                                           (k_ / (distance ** 2)))) / lambda_))],
                                               k=1)
                        if state == ['inf']:
                            q[i][3] = 'infected'
                            q[j][3] = 'infected'
                else:
                    if not (p[i][3] == p[j][3]):
                        states = ['inf', 'n_inf']
                        state = random.choices(states, weights=[(min(1, (k_ / (distance ** 2)))),
                                                                (1 - (min(1, (k_ / (distance ** 2)))))],
                                               k=1)
                        if state == ['inf']:
                            q[i][3] = 'infected'
                            q[j][3] = 'infected'
    i_state[6] = deepcopy(q)
    return q


def revolve(vector, order):
    lst = [(0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1)]
    index = lst.index(vector) + order
    resultant = lst[index % 8]
    return resultant


def deepcopy(lst):
    result = []
    for e in lst:
        if isinstance(e, list):
            result.append(deepcopy(e))
        else:
            result.append(e)
    return result


i_state = get_data()
