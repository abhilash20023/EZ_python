import sys
print('-----Travelling Salesman Problem-----')
def Cost(curr,visited,G,DP):
    n=len(G)
    if len(visited)==n:
        return G[curr][0]
    visit = tuple(visited)
    if (curr,visit) in DP:
        return DP[(curr.visit)]
    min_cost=sys.maxsize
    for i in range(n):
        if i not in visited:
            new_visit=visited+[i]
            new_cost=G[curr][i]+Cost(i,new_visit,G,DP)
            min_cost=min(min_cost,new_cost)
    DP[(curr,visit)]=min_cost
    return min_cost
G=[[0,4,7,5,5],
   [4,0,2,3,8],
   [7,2,0,3,4],
   [5,3,3,0,6],
   [5,8,4,6,0]]
DP={}
print('Minimum cost = ',Cost(0,[0],G,DP))
for i in DP:
    print(i)
