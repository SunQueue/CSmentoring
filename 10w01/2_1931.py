index = int(input())
timelist = []
for _ in range(index):
    tmp = list(map(int, input().split()))
    timelist.append(tmp)
timelist.sort()

# 결국 읽는게 이중for문이랑 다를게 뭐지..?

result = 0
for i in range(0,len(timelist)) :
    tmpcount = 1
    endTime = int(timelist[i][1])
    for j in  range(0,len(timelist)):
        if endTime > timelist[j][1] : continue;
        if endTime >= timelist[j][0] :
            tmpcount +=1
            endTime = timelist[j][1]
    if(result < tmpcount) : result = tmpcount
print(result)
