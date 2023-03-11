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
#visited 리스트
visited=[False]*(n+1)
#최단거리 테이블
distance = [INF]*(n+1)

#모든 간선 정보 입력

for _ in range(m):
    a,b,c=map(int,input().split())
    #a번 노드에서 b번노드로 가는 비용이 c라는 의미(방향성 있는 그래프이기때문)
    graph[a].append((b,c))

#방문하지 않는 노드 중에서, 가장 최단거리가 짧은 노드의 번호를 반환
def get_smallest_node():
    min_value=INF
    index=0 #가장 최단거리가 짧은 노드 (index)
    for i in range(1,n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index=i
    return index

def dijkstra(start):
    #시작 노드에 대해서 초기화
    distance[start]=0
    visited[start]=True
    #시작 노드에 인접한 노드들까지의 최단거리 먼저 갱신
    for j in graph[start]:
        distance[j[0]]=j[1] 

    #시작 노드 제외 전체 n-1개의 노드에 대해 반복
    for i in range(n-1):
        #전체 테이블 중 가장 짧은 거리가진 노드 꺼내와서 방문처리
        now=get_smallest_node()
        visited[now] = True
        #현재 노드와 연결된 다른 노드 확인, 테이블 갱신
        for j in graph[now]:
            cost = distance[now] + j[1]
            #더 짧을 경우에만 갱신
            if cost < distance[j[0]]:
                distance[j[0]] = cost

dijkstra(start)
for i in range(1,n+1):
    if distance[i]==INF:
        print("INFINITY")
    else:
        print(distance[i])
