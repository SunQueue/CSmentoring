from queue import PriorityQueue
# 문서의 개수 
# 몇번째로 인쇄되었는지 궁금한 문서가 현재 Queue의 몇번째에 놓여있는가

# index로 1회, priority로 정렬을 한 후 M번 문저의 ..

# deque사용시 pop-append 사용할 것.(O(1))

doTestcase = int(input())
for i in range (0, doTestcase):
    getIndex, whQue = input().split()
    getIndex = int(getIndex)
    whQue = int(whQue)
    que = PriorityQueue(maxsize=getIndex)
    for i in range(0, getIndex):
        que.put((input().split(),i))#priority, inputIndex

    print(que)