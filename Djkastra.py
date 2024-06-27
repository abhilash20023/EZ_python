G=[
    [0,  7, False, False, False, False,False, 2, False, False],
    [7,  0,  4,  1, False,  5, False,False, False, False],
    [False, 4,  0, False, False, False, False, 8, False, False],
    [False, 1, False,  0,  6,  8,  3, 3, False, False],
    [False, False,False,  6,  0, False, False, 6,  8, False],
    [False, 5, False,  8, False,  0, False, False, False,False],
    [False,False, False,  3, False, False,  0, False,  9, 2],
    [2, False,  8,  3,  6, False, False,  0, False,False],
    [False,False, False, False,  8, False,  9, False,  0,False],
    [False,  False, False, False, False, False,  2, False, False, 0]
]
temp={}
for i in range(len(G)):
    temp[i]=float("inf")
dist=[float("inf")]*len(G)
temp[0]=0

while len(temp)>0:
    min_value=min(temp.values())
    min_key=min(temp,key=temp.get)
    temp.pop(min_key)
    dist[min_key]=min_value
    for j in range(len(G[min_key])):
        if G[min_key][j]!=False and G[min_key][j]!=0:
            new_dist=min_value+G[min_key][j]
            if j in temp.keys() and temp[j]>new_dist:
                temp[j]=new_dist
print(dist)