# 세 막대 : a, b, c 세 막대를 가지고 있음 => 둘레가 최대가 되는 삼각형을 만드는 프로그램
# 삼각형 조건 : 가장 긴 변 < 나머지 변의 합
# 가장 큰 변을 찾고 나머지 변의 합을 이용해서 가장 긴 변을 조절하여 합을 출력하면 완성!
a, b, c = map(int,input().split())
arr = []
arr.append(a)
arr.append(b)
arr.append(c)

for i in range(3):
    for j in range(i+1,3):
        if arr[i] > arr[j]:
            temp = arr[j]
            arr[j] = arr[i]
            arr[i] = temp

# result = sorted(arr)
if arr[2] >= arr[0] + arr[1]:
    print(2 * (arr[0] + arr[1]) - 1)
else:
    print(arr[0] + arr[1] + arr[2])
# sorted 정렬을 통해서 쉽게 해결 가능한 문제
# sorted를 대신해서 사용할 코드를 만들어서 해결하는것 추천

# sorted 내장 함수를 사용하지 않고 이중 for문을 사용해서 각 인덱스 끼리 서로 순회하며 대소비교 가능하다.