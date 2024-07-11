# 달팽이는 올라가고 싶다 : A, B, V 입력받음 V미터 까지 올라가는데 걸리는 일 수 구하기
# 낮에는 A미터 올라감, 밤에는 B미터 내려감
A, B, V = map(int,input().split())
count = 0
while V >= (A-B)*count:
    count += 1
    if V <= count*A - (count-1)*B:
        break
    else:
        pass
print(count)