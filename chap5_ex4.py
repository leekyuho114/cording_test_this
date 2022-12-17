#미로탈출 (bfs)
from collections import deque
def bfs(x,y):
    #먼저 queue에 0,0 append
    queue=deque()
    queue.append((x,y))
    while queue:
        #bfs queue에서 요소 하나 pop
        x,y=queue.popleft()
        #가능한 네가지 방향 중 1인경우 첫 방문이므로 queue에 추가하고 거리 추가
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=m:
                continue
            if graph[nx][ny]==1:
                queue.append((nx,ny))
                graph[nx][ny]=graph[x][y]+1
    return graph[n-1][m-1]    


n,m=map(int, input().split())
graph=[]
for i in range(n):
    graph.append(list(map(int,input())))

dx=[-1,1,0,0]
dy=[0,0,-1,1]

print(bfs(0,0))