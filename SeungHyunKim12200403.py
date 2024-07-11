# 분수찾기 : 지그재그로 순서 증가 => 순서 입력받고 순서에 맞는 분수 출력
# X = sigma n
# 대각선이 되는 지점을 기준으로 생각해봄 => (2,3) = 2개 / (4,5,6) = 3개 / (7,8,9,10) = 4개 / (11,12,13,14,15) = 5개 / ...
# 갯수만 정하면 while문을 사용하여 구할 수 있다고 생각함 => sigma n을 받는 변수를 이용해서 n값을 결정
X = int(input())
if X == 1:
    print('1/1')
else:
    n = 2
    share = 1 + n
    while X > share:
        n += 1
        share = share + n
    # 짝수 n => 1/n 부터 시작, 홀수 n => n/1 부터 시작
    number = share - X
    if n % 2 == 0:      #짝수
        print(n-(number),end = '')
        print("/",end = '')
        print(n-(n-(number+1)))
    elif n % 2 == 1:    #홀수
        print(n-(n-(number+1)),end = '')
        print("/",end = '')
        print(n-(number))