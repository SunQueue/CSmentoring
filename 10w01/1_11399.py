# 대충 입력받은 배열이 오름차순으로 되어있을때, 
# n+1번째 시간 += 0~n번째 시간의 합

if __name__ == "__main__":
    # get input index
    index = int(input())
    # get input array
    customer = []
    customer = input().split()
    # arr.sort()
    customer.sort()
    # for i in range (0,inputIndex)
    #    accTime += arr[i]
    accTime =0
    for i in range(0,index) :
        accTime += int(customer[i]) * (index-i)
    print(accTime)