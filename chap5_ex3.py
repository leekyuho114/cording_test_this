#음료수 얼려먹기 문제(dfs)
def dfs(x,y):
    #주어진 범위를 넘어갔을 시의 예외처리
    if x<=-1 or y<=-1 or x>=n or y>=m:
        return False
    #일단 0이면 마지막 줄 결과는 return True 여야하는게 맞음
    if graph[x][y]==0:
        graph[x][y]=1
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False

n, m = map(int, input().split())

graph =[]
for i in range(n):
    graph.append(list(map(int, input())))

result=0
for i in range(n):
    for j in range(m):
        if(dfs(i,j)==True):
            result+=1

print(result)