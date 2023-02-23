from collections import deque 
#리스트를 이용한 구현은 시간 복잡도가 비효율적
#deque 라이브러리 사용
# 5 - 2- 7 - 4 popleft 2-7-4 (3) 2-7-4-3
queue = deque()

queue.append(5)
queue.append(2)
queue.append(7)
queue.append(4)
queue.popleft() #popleft를 사용하는 것이 관행임
queue.append(3)
print(queue)
queue.reverse()
print(queue)
