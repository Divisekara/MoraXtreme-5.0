##n, s = list(map(int, input().strip().split(" ")))
##L = list(map(int,(input().strip().split(" "))))


def powerset(s):
    x = len(s)
    masks = [1 << i for i in range(x)]
    for i in range(1 << x):
        yield [ss for mask, ss in zip(masks, s) if i & mask]


 
for i in ))
