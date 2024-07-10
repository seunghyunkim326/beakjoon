# 벌집 : 육각형으로 이루어짐, 중앙을 1번부터 시작해서 바깥을 한 바퀴 돌아가면서 1씩 증가
# N번 방까지 지나가야하는 최소 방의 갯수 출력
N = int(input())
if N-1 == 0:
    print("1")
else:
    k = 0
    share = 1
    while share <= N-1:
        share = share + 6*k
        k += 1
    print(k)
# X = 1+sigma(6n) 과 같이 표현 가능하고 n을 구하면 지나가야 하는 최소 방의 갯수를 알 수 있다.
# 이렇게 조건을 알 때, while을 통하여 편리하게 해결 가능하다.