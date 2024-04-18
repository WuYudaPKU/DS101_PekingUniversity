import itertools
def permutation(n):
    # n_pairs
    permutation_set = set(itertools.permutations(['('] * n + [')'] * n))
    sorted_lst = sorted(list(permutation_set))
    for i in sorted_lst:
        if is_valid("".join(i)):
            print("".join(i))

def is_valid(s:str):
    stack=[]
    for i in s:
        if i=='(':
            stack.append('(')
        elif i==')':
            if stack:
                stack.pop()
            else:
                return False
    return True

permutation(int(input()))
