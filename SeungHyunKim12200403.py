# 그룹단어 체커 : N개의 단어 입력받음 -> 그룹단어 갯수 출력     단어는 한글자만 나올 수 있다.=> 무조건 그룹단어라 미리 계산 후 리스트에 안넣음
# aba => 그룹단어X happy, new, year => 그룹단어
# 문자열 안의 값을 계속 변경시키면 리스트 범위를 벗어나거나 불안정할 가능성 크다 => 새로운 리스트를 만들어서 같은거 나오면 무시, 다른거 나오면 업데이트 하는 형식(from GPT)
N = int(input())
storage = []
minus = 0
result = 0
for i in range(N):
    word = list(input())
    if len(word) == 1:
        result += 1
    else:
        new_word = []
        new_word.append(word[0])
        for j in range(1,len(word)):
            if word[j] != word[j-1]:
                new_word.append(word[j])
        storage.append(''.join(new_word))

for k in range(len(storage)):
    for checker in storage[k]:
        if storage[k].count(checker) >= 2:
            minus += 1
            break
    result += 1        
print(result-minus)
# 같은 문자가 연속으로 나오면 하나의 문자로 묶어버려 리스트에 넣고 다시 중복된 문자를 찾아서 중복된 문자가 없을 시 result+1