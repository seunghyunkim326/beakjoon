# 삼각형과 세 변 : 삼각형 세 변의 길이에 따라 정의
# Equilateral : 세 변의 길이가 같은 경우, Isosceles : 두 변의 길이만 같은 경우, Scalene : 세 변의 길이가 모두 다른 경우
# 세 변의 길이가 삼각형 조건을 만족하지 않으면 Invalid 출력
# 0 0 0 이 입력될 때 까지 입력받음
while True:
    array = list(map(int,input().split()))
    new = sorted(array)
    if new[0] == new[1] == new[2] == 0:
        break
    else:
        if new[0] + new[1] <= new[2]:
            print("Invalid")
        else:
            if new[0] == new[1]:
                if new[0] == new[2]:
                    print("Equilateral")
                else:
                    print("Isosceles")
            elif new[1] == new[2]:
                if new[0] == new[1]:
                    print("Equilateral")
                else:
                    print("Isosceles")
            else:
                print("Scalene")