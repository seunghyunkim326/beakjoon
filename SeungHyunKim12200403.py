# 대지 : 옥구슬을 모두 포함하는 최소 면적을 구하는 코드
# 옥구슬을 (x,y)의 형태로 주어지고 N개의 옥구슬이 주어짐, 가장 큰 x,y와 가장 작은 x,y값의 차이를 곱하여 계산
# x리스트와 y리스트를 만들고 차례대로 입력 받아서 정렬 후 처음과 끝의 차이를 구하면 간단할듯
N = int(input())
X, Y = [], []
for i in range(N):
    x,y = map(int,input().split())
    X.append(x)
    Y.append(y)

# X,Y 정렬 대신 max값과 min 값만 찾게 되더라도 차이만 구하면 가능
diff_x, diff_y = 0, 0
if N > 1:
    max_x, min_x = -10^5, 10^5
    for j in range(N):
        if X[j] > max_x:
            max_x = X[j]
        if X[j] < min_x:
            min_x = X[j]
    diff_x = max_x - min_x
    max_y, min_y = -10^5, 10^5
    for k in range(N):
        if Y[k] > max_y:
            max_y = Y[k]
        if Y[k] < min_y:
            min_y = Y[k]
    diff_y = max_y - min_y
    print(diff_x*diff_y)
else:
    print(0)
# 좌표가 음수도 포함함 => 