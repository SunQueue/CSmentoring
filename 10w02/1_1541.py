# -부호를 만났을 때 (를 시작해서
# if 식이 끝나거나 새로운 -가 나왔을때 )닫음
# 위의 행위를 하나의 문장이 끝날때까지 진행

# stack..?
# 진짜 stack은 아니고. 일단 +변수 -변수를 만들어 놓은 뒤에 
# 일반 경우, 숫자를 +변수에 +=
# -를 만난 경우, -변수에 +=
#     -내에서 괄호가 존재한다고 가정하고
#    - 내에서 +가 나오면 -변수에 +=
#    - 내에서 -가 나오면 괄호를 닫고 다시 연다고 가정하고 -변수에 +=

val = 0

exp = list(input().split('-'))
print(exp)

for i in range(0, len(exp)):
    exp[i] = list(map(int, exp[i].split('+')))
    if i < 1 : 
        val += sum(exp[i])
    else :
        val -= sum(exp[i])
print(val)