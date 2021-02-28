dp = dict()


def nCr(n, r):
    if r == 0 or n == r:
        return 1
    if r > n:
        return 0
    if n - 1 not in dp:
        dp[n - 1] = dict()

    dp[n - 1][r - 1] = nCr(n - 1, r - 1)
    dp[n - 1][r] = nCr(n - 1, r)

    return dp[n - 1][r - 1] + dp[n - 1][r]


def find_leading_one_index(arr):
    n = len(arr)
    i = -1
    while i > -n:
        if arr[i] == 1:
            return i
        i -= 1

    return 0


def next(old_arr):
    arr = old_arr[:]
    n = len(arr)

    leading_one_index = find_leading_one_index(arr)
    if leading_one_index == -1:
        leading_one_count = 0
        i = -1
        while i > -n and arr[i] == 1:
            arr[i] = 0
            leading_one_count += 1
            i -= 1
        leading_one_index = find_leading_one_index(arr)
        arr[leading_one_index] = 0
        arr[leading_one_index + 1] = 1
        for i in range(leading_one_count):
            arr[leading_one_index + 2 + i] = 1
    else:
        arr[leading_one_index] = 0
        arr[leading_one_index + 1] = 1

    return arr


def generate_combination(n, r):
    iterations = nCr(n, r)
    combinations = []
    combinations.append([1 if i < r else 0 for i in range(n)])

    for _ in range(iterations - 1):
        nc = next(combinations[-1])
        combinations.append(nc)

    return combinations


def transpos_combination(old_combination):
    return map(list, zip(*old_combination))


# def check_combination(combination, r):
#     bit = 0
#     target = 2 ** len(combination[0]) - 1
#     for bits in combination[0:r]:
#         for j in range(len(bits)):
#             if bits[j] == 1:
#                 bit |= 1 << j
#     return bit == target


def translate_combination(old_combination):
    combination = []
    for old_c in old_combination:
        new_p = []
        for number in range(len(old_c)):
            if old_c[number] == 1:
                new_p.append(number)

        combination.append(new_p)
    return combination


def solution(num_buns, num_required):
    if num_required == 0:
        return [[] for _ in range(num_buns)]

    if num_required == 1:
        return [[0] for _ in range(num_buns)]

    if num_required == num_buns:
        return [[i] for i in range(num_buns)]

    combination = generate_combination(num_buns, num_buns-num_required+1)
    combination = transpos_combination(combination)
    combination = translate_combination(combination)
    return combination


print(solution(5, 2))
print(solution(5, 3))
