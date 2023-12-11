def solution(numbers):
    if 1 <= len(numbers) <= 100000:
        numbers_str = list(map(str, numbers))  # 주어진 numbers 리스트의 각 숫자를 문자열로 변환하여 numbers_str 리스트에 저장
        numbers_str.sort(key=lambda x: x*3, reverse=True)
        answer = ''.join(numbers_str)  # 정렬된 문자열을 모두 이어붙여서 하나의 문자열로 만든다
        return answer  # 가장 큰 수 반환
   


numbers_input = [8, 30, 17, 2, 23]
result = solution(numbers_input)
print(result)
