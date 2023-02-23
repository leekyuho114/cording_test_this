# DFS 메서드 정의
def dfs(graph, v, visited):
    visited[v]=True
    print(v, end=' ')
    for i in graph[v]:
        if visited[i] == False:
            dfs(graph, i, visited)

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

dfs(graph, 1, visited)
