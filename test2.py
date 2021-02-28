from itertools import combinations


def solution(num_buns, num_required):
    buns = [[] for i in range(num_buns)]
    if num_required == 0:
        return buns
    start = 0
    for c in combinations(buns, num_buns - num_required + 1):
        for item in c:
            item.append(start)
        print(c, start)
        start += 1
    return buns


print(solution(5, 2))
