def solution(a, b):
    w = ("THU", "FRI", "SAT", "SUN","MON","TUE","WED")
    month = (0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    
    return w[(sum(month[:a]) + b) % 7]

