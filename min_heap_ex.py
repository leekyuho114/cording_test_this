import heapq
#heapq 라이브러리는 최소힙(min heap)임
# heap에 넣었다 빼면서 오름차순으로 정렬하는 heap sort
#오름차순으로 힙 정렬(heap sort)
def heapsort(iterable):
    h=[]
    result=[]
    # h가 힙, 모든 원소 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h,value)
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result

result = heapsort([1,3,5,7,9,2,4,6,8,0])
print(result)