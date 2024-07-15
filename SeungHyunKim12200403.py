# 색종이 : 가로, 세로 100인 정사각형 흰색 도화지에 가로, 세로 10인 정사각형 검은 색종이 붙임
# 색종이 수 입력 => 색종이 위치 입력 => 검은 부분의 넓이 출력
# x,y 좌표를 사용하지만 x좌표, y좌표 따로 볼 경우에 겹치지 않아도 2 이상이 되는 문제가 발생한다.
# 2차원 배열을 이용하여 x좌표, y좌표 두개 전부 고려한다.
# 100*100이라면 한 점이 넓이 1로 생각 가능 => 색종이의 코드에 따라 

result = 0
N = int(input())
black = [[0 for _ in range(100)] for _ in range(100)]

for i in range(N):
    x, y = map(int,input().split())
    for j in range(10):
        for k in range(10):
            if black[x+j-1][y+k-1] == 0:
                black[x+j-1][y+k-1] = 1

for X in range(100):
    for Y in range(100):
        if black[X][Y] == 1:
            result += 1

print(result)

#           
# 색종이가 있는 좌표에 1표시, 이미 1로 되어있으면 pass
# for _ in range()