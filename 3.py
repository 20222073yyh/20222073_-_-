def solution(age):
    

    answer = ''
    number = {0: 'a', 1: 'b', 2: 'c', 3:'d', 4: 'e', 5: 'f', 6:'g', 7:'h', 8:'i', 9:'j'} #숫자에 각각의 알파벳 저장
    age_str = str(age)
    for i in age_str: # 한글자씩 반복

        answer += number[int(i)] #각 자릿수에 해당하는 문자열을 number를 통해 알파벳으로 변환하여 answer에 저장

        

    return answer

    
age = "12" #ab가 출력된다
result = solution(age)
print(result)