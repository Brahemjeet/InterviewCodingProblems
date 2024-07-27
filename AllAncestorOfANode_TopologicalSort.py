from typing import List
from collections import deque

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        adjList = []
        ancestorList  = [ ]
        indegree = []
        for i in range(n):
            adjList.append([])
            ancestorList.append( [] )
            indegree.append(0)

        for edge in edges:
            adjList[ edge[0] ].append( edge[1] )
            indegree[edge[1]]+=1
        topologicalOrder = []
        
        #Topological Sort Function
        def topologicalSort():
            queue = deque()
            for i in range(n):
                if(indegree[i] == 0):
                    queue.append(i)
            
            while( len(queue) > 0):
                elem = queue.popleft()
                topologicalOrder.append(elem)
                for node in adjList[elem]:
                    indegree[node]-=1
                    if indegree[node] == 0:
                        queue.append(node)

        
        topologicalSort()
        
        for node in topologicalOrder:
            for adjNode in adjList[node]:
                ancestorList[adjNode].extend(ancestorList[node] )
                ancestorList[adjNode].append(node )

        return [ sorted(set(res))  for res  in ancestorList]

        


obj = Solution()

n = 8
edges = [[0,3],[0,4],[1,3],[2,4],[2,7],[3,5],[3,6],[3,7],[4,6]]

result = obj.getAncestors(n, edges)

for r in result:
    print(r)
print("="*20)

n=5
edges  = [[0,1],[0,2],[0,3],[0,4],[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]

result = obj.getAncestors(n, edges)

for r in result:
    print(r)

print("="*20)
n=10
edges = [[5,2],[8,7],[7,2],[8,3],[1,6],[9,0]]
result = obj.getAncestors(n, edges)

for r in result:
    print(r)