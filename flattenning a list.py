L=[1,2, ['a','b','c', ['A','B','C'], 'd','e'], 3,4,5, ['d','e', ['D','E', ['F']]]]


def flatten(S):
    if S == []:
        return S
    if isinstance(S[0], list):
        return flatten(S[0]) + flatten(S[1:])
    return S[:1] + flatten(S[1:])


print(flatten(L))
