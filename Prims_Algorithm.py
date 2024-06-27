print('---Prims Algorithm---')
Graph=[[0,7,-1,-1,-1,-1,-1,2,-1,-1],
       [7,0,4,1,-1,5,-1,-1,-1,-1],
       [-1,4,0,-1,-1,-1,-1,8,-1,-1],
       [-1,1,-1,0,6,8,3,3,-1,-1],
       [-1,-1,-1,6,0,-1,-1,6,8,-1],
       [-1,5,-1,8,-1,0,-1,-1,-1,-1],
       [-1,-1,-1,3,-1,-1,0,-1,9,2],
       [2,-1,8,3,6,-1,-1,0,-1,-1],
       [-1,-1,-1,-1,8,-1,9,-1,0,-1],
       [-1,-1,-1,-1,-1,-1,2,-1,-1,0]]
v=[False]*len(Graph)
min=float('Inf')
MST=[]
x=y=-1
for i in range(len(Graph)):
    for j in range(len(Graph[i])):
        if Graph[i][j]==0 or Graph[i][j]==-1:
            continue
        elif Graph[i][j]<min:
            min=Graph[i][j]
            x=i
            y=j
v[x]=True
v[y]=True    
MST.append([x+1,y+1,min])  
while False in v:
    min=float('Inf')
    for i in range(len(v)):
        if v[i]==True:
            for j in range(len(Graph[i])):
                if Graph[i][j]==0 or Graph[i][j]==-1 or v[j]==True:
                    continue
                elif Graph[i][j]<min:
                    min=Graph[i][j]
                    x=i
                    y=j
    v[y]=True  
    MST.append([x+1,y+1,min]) 
print('Minimum Spanning Tree')
for i in range(0,len(MST)):
    print(MST[i])