index = int(input())
timelist = []
for _ in range(index):
    tmp = list(map(int, input().split()))
    timelist.append(tmp)

timelist.sort(key = lambda x : (x[1],x[0]))

earliest = 0
selected = 0

for begin, end in timelist :
    if begin >= earliest :
        selected +=1
        earliest = end

print(selected)
