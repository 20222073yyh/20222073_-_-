def solution(letter):
    
   if 1<= len(letter) <= 1000:#letter의 길이제한
    morse = {'.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
             '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
             '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
             '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
             '-.--':'y','--..':'z'}
    
    answer = ''
    
    for code in letter.split(' '): #letter를 공백을 기준으로 나누어서 각각의 Morse 코드로 분리
        if code in morse: #mores 코드가 있는지 확인
            answer += morse[code] #코드가 있으면 대응 하는 알파벳생김
        else:
            answer += ' ' #없으면 빈칸

    return answer


morse_input = "-.-- --- ..- / -. . . -.. / .--. -.-- - .... --- -."#you need python
result = solution(morse_input)
print(result)
    
    
   