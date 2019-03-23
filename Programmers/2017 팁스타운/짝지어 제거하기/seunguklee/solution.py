def solution(s):
    stk = [s[0]]
    
    for c in s[1:]:
        stk_last_value = stk[-1] if stk else None
        stk.pop() if stk_last_value == c else stk.append(c)
    
    return 0 if stk else 1

