def solution(t, p):
    count = 0
    a = len(t)
    b = len(p)
    for i in range (a-b+1):
        T = int(t[i:i+b]) 
        P = int(p)
        if T <= P:
            count += 1
    return count

