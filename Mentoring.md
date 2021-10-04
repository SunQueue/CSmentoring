# test

# test3

# 09w05_MentoringLive

- 부르트포스란 ? -> 다 해보는 것.   
> 아무래도 다 해보다 하는 것이다 보니 O(N^3)에서 n^3 or n^2 >10억~ 이면 문제가 생길 수 있음  
> (문제에 주어진) N의 범위를 먼저 보고, N>10억 이면 n이나 n log n 으로 접근하는 것을 강하게 권장함.  
> for문의 사용 자제, 불필요한 함수의 자제, 효율적인 알고리즘의 사용 등으로 해결하는 것을 권장.  

## #2798
> import combination -> 생성 가능한 모든 경우의 수를 생성  
> import sys -> 큰 수에서 쓰면 효율적임  
> combination을 전반적으로 활용하는 모습  
> 부르트포스 형태. 결국 다 해봐야 알 수 있음.  

> if __name__ == "__main__" :   
>   > c에서의 main같은 느낌. class 사용시 자주 사용  
>   > 코테에서는 class 많이 사용 안하는 듯?  

## #7568
> people = [tuple(map(int, myInput().split))) for _ in range(N)] -> list comprehension 사용  
> else : pass -> ?    
> 다 .append(list(map(int, int().split())))를 쓰네..? map()은 어디에 쓰는거냐?  
> pythontutor.com -> 디버깅할때 진행사항 알 수 있어 좋을 듯  

## #1436
> 내가 작성한 코드의 경우 모든 경우에 대해 한것이고  
> 멘토가 구한 코드의 경우 '666'만 들어간 수만 list로 추출하여 구할 수 있도록 구현  
> 람다식을 써볼까..?  

## #13305
> 다음시간으로 순연 

## 기타
> 책 greedy 보고 오시길
> 다음시간까지 주유소 문제까지 2문제 해올까요
