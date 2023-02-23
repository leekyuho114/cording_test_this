stack=[]
stack.append(5) #add
stack.append(2)
stack.append(7)
stack.append(4)
stack.pop() #delete
stack.append(3)

print(stack[::-1]) #스택의 최상단 원소부터 출력
print(stack) #스택의 최하단 원소부터 출력
