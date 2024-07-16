# 세 막대 : a, b, c 세 막대를 가지고 있음 => 둘레가 최대가 되는 삼각형을 만드는 프로그램
# 삼각형 조건 : 가장 긴 변 < 나머지 변의 합
# 가장 큰 변을 찾고 나머지 변의 합을 이용해서 가장 긴 변을 조절하여 합을 출력하면 완성!
a, b, c = map(int,input().split())
arr = []
arr.append(a)
arr.append(b)
arr.append(c)
result = sorted(arr)
if result[2] >= result[0] + result[1]:
    print(2 * (result[0] + result[1]) - 1)
else:
    print(result[0] + result[1] + result[2])