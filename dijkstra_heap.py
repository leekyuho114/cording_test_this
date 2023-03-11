import heapq
import sys
input = sys.stdin.readline
INF = int(1e9) # 무한을 의미하는 값으로 10억 설정
#테이블 = distance 리스트
#노드개수, 간선 개수 입력
n,m = map(int, input().split())
#시작 노드 번호 입력받기
start=int(input())
#각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 ex) [[2,3],[6,7]] 1번노드 2,3번 노드와 연결
graph=[[] for _ in range(n+1)]
#visited 리스트 필요없음, 힙에서 꺼냈을때 저장된 길이보다 길면 그냥 넘어감
#visited=[False]*(n+1)
#최단거리 테이블
distance = [INF]*(n+1)

#모든 간선 정보 입력

for _ in range(m):
    a,b,c=map(int,input().split())
    #a번 노드에서 b번노드로 가는 비용이 c라는 의미(방향성 있는 그래프이기때문)
    graph[a].append((b,c))

#방문하지 않는 노드 중에서, 가장 최단거리가 짧은 노드의 번호를 반환
# def get_smallest_node(): 대신 heapq 사용

def dijkstra(start):
    q=[]
    heapq.heappush(q,(0,start))
    distance[start]=0
    while q: #큐가 비어있지않다면
        #가장 최단거리가 가장 짧은 노드 정보꺼내기
        dist,now = heapq.heappop(q)
        #노드가 이미 처리된적 있는 노드라면 무시 visited[i]=True의 역할함
        if distance[now]<dist:
            continue
        for i in graph[now]:
            #현재 노드까지의 거리(dist)에 다음 노드까지의 거리(i[1]) 더함
            cost = dist + i[1]
            #현재 노드 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))

dijkstra(start)
for i in range(1,n+1):
    if distance[i]==INF:
        print("INFINITY")
    else:
        print(distance[i])