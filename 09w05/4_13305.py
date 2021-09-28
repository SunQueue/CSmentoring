city = input()
dist = []
price = []
dist = input().split()
price = input().split()
#do :
total = int(dist[0])*int(price[0])
#cmp
for i in range (0,len(dist)-1) : 
    if(int(price[i]) > int(price[i+1])) : # 후행하는 price가 더 싼 경우 -> 후행하는 price선택
        total += int(dist[i+1]) * int(price[i+1])
    if(int(price[i]) <= int(price[i+1])) : # 기존의 price가 더 싼 경우 -> 기존 price 선택
        total += int(dist[i+1]) * int(price[i]) 
print(total)