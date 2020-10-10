##n,m,q = list(map(int, input().split(",")))
##M = sorted(list(map(int, input().strip().split(" "))))
##
##answer=[]
##for i in range(q):
##    L=M[:]
##    a,b = sorted(list(map(int, input().split(","))))
##    L.extend([a,b])
##    L.sort()
##    min_index = L.index(a)
##    L.reverse()
##    max_index = len(L) -L.index(b)
##    print(max_index- min_index-2)
##
##
##
##
##

