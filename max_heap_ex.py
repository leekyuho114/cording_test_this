import heapq

# 내림차순 힙 정렬(heap sort)
# 그냥 최소힙 정렬과 똑같이 쓰돼 값에 -만 붙여서 힙에 push, 꺼내며 다시 -
def heapsort(iterable):
    h=[]
    result=[]
    # h가 힙, 모든 원소 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h,-value)
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(-heapq.heappop(h))
    return result

result = heapsort([1,3,5,7,9,2,4,6,8,0])
print(result)