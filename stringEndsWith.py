def solution(text, ending):
    if text[-len(ending):] == ending: return True 
    return False 
    
print(solution("abc", "bc"))