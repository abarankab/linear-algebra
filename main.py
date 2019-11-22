'''
Calculates the parity of a permutation
'''
def sign(permutation):
    n_inversions = 0
    for i in range(len(permutation)):
        for j in range(i + 1, len(permutation)):
            if permutation[i] > permutation[j]:
                n_inversions += 1
    return (-1) ** n_inversions

'''
Calculates al permutations where x is in a power of 5 and
appends them to a global array [permutations]
'''
def gen_permutation(n, m, p = [], x_cnt = 0):
    if len(p) == n and x_cnt == 5:
        permutations.append(p)
    elif len(p) != n:
        for i in range(n):
            if i + 1 not in p:
                gen_permutation(n, m, p + [i + 1], x_cnt + (m[len(p)][i] == 'x'))

if __name__ == '__main__':
    print("Matrix size:")
    n = int(input())
    m = []
    coef = 0
    print("Matrix elements:")
    for i in range(n):
        m.append(list(input().split()))

    global permutations
    permutations = []
    gen_permutation(n, m)

    # iterates through permutataions and updates the answer
    for p in permutations:
        cur = 1
        for i, j in enumerate(p):
            if m[i][j - 1] != 'x':
                cur *= int(m[i][j - 1])
        coef += cur * sign(p)
                

    print(coef)
