# 색종이 : 가로, 세로 100인 정사각형 흰색 도화지에 가로, 세로 10인 정사각형 검은 색종이 붙임
# 색종이 수 입력 => 색종이 위치 입력 => 검은 부분의 넓이 출력
# x,y 좌표를 사용하지만 x좌표, y좌표 따로 볼 경우에 겹치지 않아도 2 이상이 되는 문제가 발생한다.
# 2차원 배열을 이용하여 x좌표, y좌표 두개 전부 고려한다.

N = int(input())
black = [[0 for _ in range(2)] for _ in range(N)]

for i in range(N):
    x, y = map(int,input().split())
    black[i][0] = x
    black[i][1] = y

print(black)

s = 0

for j in range(N):
    for k in range(j+1,N-j):
        x_num = 0
        y_num = 0
        if (black[j][0] < black[k][0] < black[j][0]+10) or (black[k][0] < black[j][0] < black[k][0]+10):
            if (black[j][1] <= black[k][1] < black[j][0]+10) or (black[k][1] < black[j][1] < black[k][1]+10):
                x_num = 10 - abs(black[k][0]-black[j][0])
                y_num = 10 - abs(black[k][1]-black[j][1])
                print(x_num)
        s = s + (x_num * y_num)
print(100*N-s)
# N번째 까지 서로 탐색하는 코드를 만들 때, range(j+1,N-j)를 하면 중복 탐색 없이 서로 한번 씩 탐색 가능하다.
# 시작 범위도 설정할 수 있음에 주의해라!