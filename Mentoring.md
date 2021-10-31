# 09w05  
## MentoringLive

- 부르트포스란 ? -> 다 해보는 것.   
> 아무래도 다 해보다 하는 것이다 보니 O(N^3)에서 n^3 or n^2 >10억~ 이면 문제가 생길 수 있음  
> (문제에 주어진) N의 범위를 먼저 보고, N>10억 이면 n이나 n log n 으로 접근하는 것을 강하게 권장함.  
> for문의 사용 자제, 불필요한 함수의 자제, 효율적인 알고리즘의 사용 등으로 해결하는 것을 권장.  

### #2798
3
> combination을 전반적으로 활용하는 모습  
> 부르트포스 형태. 결국 다 해봐야 알 수 있음.  

> if __name__ == '__main__' :   
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
- 초기의 생각은, 처음 한 쌍을 받아서, 그걸 기준으로 입력을 순회하면서 비교하는건데...  
- 이거를 앞 시간 sort, 뒷시간 sort해서 하는거같은데..  
- 일단 map써서 이차원 배열을 append하는 방식에 익숙해져야할 것 같고  
- 앞sort뒤sort할때 lambda를 많이 쓰네  
> sort(key)에 lambda식을 쓸 수 있는데, list.sort(key = lambda x : (x[0], x[1])) 이면 x[0]을 기준, x[1]을 기준으로 정렬한다.   
> 부호로 역순 정렬도 가능.  
> ......그럼 sort와 lambda정렬의 차이점은 뭘까..

 - 1차원 배열 입력 받기  
> https://dailylifeofdeveloper.tistory.com/119 참고
> 1. 띄어쓰기로 되어있는 경우 : arr = list(map(int, input(),split())  
> 즉, split()을 통해 띄어쓰기를 기준으로 하여 입력을 받고, 이를 int로 바뀌서(map()) list형태로 저장
> 2. Enter로 입력받는 경우 : 
>    > arr = []  
>    > for i in range (원소개수) :
>    >     arr.append(int(input())  
- 2차원 배열 입력 받기 ; 위 링크의 132번 게시물 참고

- python은 for문에 증가변수를 두개씩 넣을 수 있다...!(원래 그랬던가)  
> 예) for i, j in list : ...  

- 사실 왜 sort(key = lambda x : (x[1], x[0])) 해야하는지 아직도 모르겟슴...


## MentoringLive

### 13305
- 오름차순 -> 누적합 더하기 순으로 진행
- 그리디 ; 구현이랑 비슷한 느낌..? 사실 거의 잘 안됨. 다익스트라 할때는 그리디가 보이는데 이런 구현문제는 그리디보다는 푸는데 의의를 둘 것

- for-else구문  
> for 문중 break되어서 끝까지 돌지 못하고 탈출하면 else 구문이 실행되지 않는 구문  


### 1931
- 해제1
> 시작값과 끝값 따로 넣고, 끝값으로 정렬, 시작값으로 정렬 ->  
> ...인터넷의 해제와 비슷한듯    
> 왜 많이 걸릴까...? flow는 비슷한 것 같은데..    
- 1. 입력부분에서의 map()사용?  
- 2. list comprehension 사용  
- import sys > 큰 입력에서의 시간 효율성이 좋아짐  
> myinput = sys.stdin.readline  
> info = [list(map(int, myinput().split)) for _ in range(N)]  
> map()는 어떤 형태로 받을지, 어떤 식으로 받을 것인지가 인자로 들어감.   
> list를 빼면 map 객체로 받음. 그래서 list로 casting 해줌  
> list Comprehension사용을 권장.!!!!  
- 두유노 sort(key)?   
> 내림차순은 인자로 reverse=True 넣어줌.  
> 2차원 배열에서 정렬하고 싶을때 key와 lambda를 활용하여 특정 기준을 정해 정렬이 가능  
- 이중정렬의 경우 꼬인다...? ???????  
# 1,4 1,2 2,1 -> (앞정렬) 1,2 1,4 2,1 -> (뒷정렬) 2,1 1,4 1,2 ???? 왜 2,1 1,2 1,4가 아님?  


- 다음주는 하던대로 하고 18일주는 OS스터디 합시다  
- greedy,구현,정렬 해볼까요. 이왕이면 문법 많이 쓸 수 있는거루다가  

- 최지웅알고 플루이드, big0시공간 복잡도, 책의 알고리즘 참고자료 보고 계산해보는것 권장. 계산문제 설명문제 많음   


# 10w02  
## BeforeMentoring  
- list comprehension
### 1541  
### 1966  
### 3085  