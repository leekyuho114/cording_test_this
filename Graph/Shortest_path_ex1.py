# 메세지 받은 도시 개수(INF가 아닌 노드(vertex)의 개수?) , 총걸리는 시간(힙 최댓값)
import sys
import heapq
INF=int(1e9)

def dijkstra(start):
    q=[]
    heapq.heappush(q,(0,start))
    distance[start]=0
    while q:
        dist,now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for i in graph[now]:
            cost= distance[now]+i[1]
            if cost < distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))

input = sys.stdin.readline
n,m,c=map(int,input().split())
graph=[[] for _ in range(n+1)]
for i in range(m):
    x,y,z = map(int,input().split())
    graph[x].append((y,z))


distance=[INF for _ in range(n+1)]

dijkstra(c)
res=0
time=0
for i in range(n):
    if(distance[i] != INF):
        res+=1
for i in range(n):
    if(distance[i] != INF and distance[i]>time):
        time=distance[i]

print(res,time)
