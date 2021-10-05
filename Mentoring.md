# 09w05  
## MentoringLive

- 부르트포스란 ? -> 다 해보는 것.   
> 아무래도 다 해보다 하는 것이다 보니 O(N^3)에서 n^3 or n^2 >10억~ 이면 문제가 생길 수 있음  
> (문제에 주어진) N의 범위를 먼저 보고, N>10억 이면 n이나 n log n 으로 접근하는 것을 강하게 권장함.  
> for문의 사용 자제, 불필요한 함수의 자제, 효율적인 알고리즘의 사용 등으로 해결하는 것을 권장.  

### #2798
> import combination -> 생성 가능한 모든 경우의 수를 생성  
> import sys -> 큰 수에서 쓰면 효율적임  
> combination을 전반적으로 활용하는 모습  
> 부르트포스 형태. 결국 다 해봐야 알 수 있음.  

> if __name__ == "__main__" :   
>   > c에서의 main같은 느낌. class 사용시 자주 사용  
>   > 코테에서는 class 많이 사용 안하는 듯?  

### #7568
> people = [tuple(map(int, myInput().split))) for _ in range(N)] -> list comprehension 사용  
> else : pass -> ?    
> 다 .append(list(map(int, int().split())))를 쓰네..? map()은 어디에 쓰는거냐?  
> pythontutor.com -> 디버깅할때 진행사항 알 수 있어 좋을 듯  

### #1436
> 내가 작성한 코드의 경우 모든 경우에 대해 한것이고  
> 멘토가 구한 코드의 경우 '666'만 들어간 수만 list로 추출하여 구할 수 있도록 구현  
> 람다식을 써볼까..?  

### #13305
> 다음시간으로 순연 

### 기타
> 책 greedy 보고 오시길  
> 다음시간까지 주유소 문제까지 2문제 해올까요

# 10W01  
## BeforeMentoring  
### #11399...  
> custom = [] 없애고 custom = list(map(int, input().split()))하니까 되네..?  
>  custom = list(map(int, input().split())) << 이거 좀 안익숙함. 왜 이렇게 쓰는지 사실 잘 모르겠고 무슨 원리인지도 모르겟슴  
### #1931
> - 초기의 생각은, 처음 한 쌍을 받아서, 그걸 기준으로 입력을 순회하면서 비교하는건데...  
> - 이거를 앞 시간 sort, 뒷시간 sort해서 하는거같은데..  
> - 일단 map써서 이차원 배열을 append하는 방식에 익숙해져야할 것 같고  
> - 앞sort뒤sort할때 lambda를 많이 쓰네  
>    > sort(key)에 lambda식을 쓸 수 있는데, list.sort(key = lambda x : (x[0], x[1])) 이면 x[0]을 기준, x[1]을 기준으로 정렬한다.   
>    > 부호로 역순 정렬도 가능.  
>    > ......그럼 sort와 lambda정렬의 차이점은 뭘까..

> - 1차원 배열 입력 받기  
> https://dailylifeofdeveloper.tistory.com/119 참고
>    > 1. 띄어쓰기로 되어있는 경우 : arr = list(map(int, input(),split())  
>    > 즉, split()을 통해 띄어쓰기를 기준으로 하여 입력을 받고, 이를 int로 바뀌서(map()) list형태로 저장
>    > 2. Enter로 입력받는 경우 : 
>    >    > arr = []  
>    >    > for i in range (원소개수) :
>    >    >     arr.append(int(input())  
> - 2차원 배열 입력 받기 ; 위 링크의 132번 게시물 참고

> - python은 for문에 증가변수를 두개씩 넣을 수 있다...!(원래 그랬던가)  
>    > 예) for i, j in list : ...


## MentoringLive

## AfterMentoring