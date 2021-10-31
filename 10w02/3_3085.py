#allocate
size = int(input())
board = [input() for _ in range(size)]
print(board)
#searching


tmpboard = board
i=0; j=0; flag =0; result = 0;
getchar = tmpboard[i][j]

for i, j in (size-1):
    if getchar == tmpboard[i+1][j] : 
        i+=1
        getchar = tmpboard[i][j]
        continue
    if getchar == tmpboard[i][j+1] :
        j+= 1
        getchar = tmpboard[i][j]
        continue
    else


print(result)
