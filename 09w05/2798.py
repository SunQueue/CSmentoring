# N = input() # Number of Card
# M = input() # Upperbound of sum of cards
N, M = input().split()
## print(N); print(M);
# 두번째 수 배열들을 입력받고
cards = [int(x) for x in input().split()]
## print(cards)
# 3중for문 (0~n-2; 1~n-1 ; 2~n)

N = int(N)
M = int(M)
cmp = 0

for i in range(0,N-2) :
    for j in range(1,N-1) :
        for k in range (2,N) : 
            if((cards[i]+cards[j]+cards[k] < cmp) or (cards[i]+cards[j]+cards[k] > M)) : break
            else : 
                cmp = cards[i]+cards[j]+cards[k]
print(cmp)
