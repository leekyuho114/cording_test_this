# DFS 메서드 정의
from collections  import deque
def bfs(graph, start, visited):
    queue =deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=" ")
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True;

graph = [ #index 0은 사용하지 않는 쪽으로 하는것이 좋음 
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]
visited=[False]*9
bfs(graph, 1, visited)
