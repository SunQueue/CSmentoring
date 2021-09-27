N = int(input()) # 초기 input
body = []

for i in range(0,N) : 
    body.append(input().split())
    body[i].append(1) #body[*][2] = rankFlag

    if(i>0) : 
        for j in range (0,i): # i = new; j = old
            if((body[i][0] > body[j][0]) and (body[i][1] > body[j][1])) : #if new is big, old.rank++
                body[j][2] += 1
            elif((body[i][0] < body[j][0]) and (body[i][1] < body[j][1])) : #if old is big, new.rank++
                body[i][2] += 1

for i in range (0,N) :
    print(body[i][2])