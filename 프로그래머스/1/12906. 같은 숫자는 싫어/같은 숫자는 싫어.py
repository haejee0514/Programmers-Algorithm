def solution(arr):
    answer = []
    previous = None
    for num in arr:
        if num != previous:  
            answer.append(num)
        previous = num  
    return answer
