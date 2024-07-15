# 색종이 : 가로, 세로 100인 정사각형 흰색 도화지에 가로, 세로 10인 정사각형 검은 색종이 붙임
# 색종이 수 입력 => 색종이 위치 입력 => 검은 부분의 넓이 출력
# x, y 좌표를 이용하여 색종이가 위치한 부분은 1로 바꿔줌(중복이여도 그대로 1)

N = int(input())
black = [[0 for _ in range(100)] for _ in range(2)]
# x(1~100), y(1~100) x,y 좌표 만들기

for _ in range(N):
    x, y = map(int,input().split())
    for i in range(10):
        black[0][x-1+i] += 1
        black[1][y-1+i] += 1
        # 검은 부분의 좌표를 1로 표시(완료)
print(black)