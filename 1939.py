class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)


T = int(input())

for i in range(T):
    n,v = input().strip().split(" ")
    
    root = TreeNode(v)

    for k in range(n-2):

        
    for j in range(n-1):
        x1, x2 = input().strip().split(" ")

        if(x1==v):
            root.add_child(TreeNode(x2))

        elif(x2==v):
            root.add_child(TreeNode(x1))

        else:
            r
            
        
   






















