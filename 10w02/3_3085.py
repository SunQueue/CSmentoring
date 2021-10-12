#allocate
size = int(input())
board = [input() for _ in range(size)]
print(board)
#searching


tmpboard = board
i=0; j=0; flag =0; result = 0;
while(i<size) :
    getchar = tmpboard[i][j]
    if getchar == tmpboard[i+1][j] : 
        flag +=1
    else : # not same
        if getchar == tmpboard[i+1][j+1] : 
            tmpboard[i][j], tmpboard[i+1][j+1] = tmpboard[i+1][j+1] , tmpboard[i][j] #swap
    i+=1
    if result < flag : result = flag
   
while(j<size) : #col
    getchar = tmpboard[i][j]
    if getchar == tmpboard[i][j+1] : 
        flag +=1
    else : # not same
        if getchar == tmpboard[i+1][j+1] : 
            tmpboard[i][j], tmpboard[i+1][j+1] = tmpboard[i+1][j+1] , tmpboard[i][j] #swap
    j+=1

    if result < flag : result = flag

print(result)
