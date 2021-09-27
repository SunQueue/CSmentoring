n = int(input())
flag = 0
count = 1
while (1) :
    count += 1
    if("666" in str(count)) : 
        flag += 1
    if (flag == n) : break
print(count)