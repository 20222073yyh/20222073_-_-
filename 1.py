def solution(my_string, target):
  if 1<= len(my_string) <= 100 and my_string.lower(): #my_string 길이를 1에서 100 사이로 영소문자로
   if 1<= len(target) <= 100 and target.lower(): #target의 길이를 1에서 100 사이로 영소문자로
    if target in(my_string): #target이 my_string에 있는지
    
        return 1 #있다면 1
    
    else: 
        return 0 #없다면 0
       
        
         
my_string = "abc"
target = "a"
result = solution(my_string, target)
print(result)       
    
