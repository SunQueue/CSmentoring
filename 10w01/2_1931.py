flag = 0
index = int(input())
timelist = []
for i in range(0, index):
    timelist.append(input().split())

for i in range (0, len(timelist)) :
    tmp = 0
    for j in range (i+1, len(timelist)) :
        if(timelist[i][1] < timelist[j][0]):
            tmp +=1
            i = j
            continue
    if(tmp > flag) : flag = tmp
print(flag)

