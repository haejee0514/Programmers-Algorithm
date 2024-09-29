def solution(n, words):
    used_words = set()  # 사용한 단어를 기록하는 집합
    used_words.add(words[0])  # 첫 번째 단어는 이미 사용된 단어로 기록
    
    for i in range(1, len(words)):
        # 끝말잇기 규칙 위반 (마지막 글자와 첫 글자가 다를 때)
        if words[i-1][-1] != words[i][0]:
            return [(i % n) + 1, (i // n) + 1]
        
        # 중복 단어 체크 (이미 사용한 단어일 경우)
        if words[i] in used_words:
            return [(i % n) + 1, (i // n) + 1]
        
        # 새로운 단어를 집합에 추가
        used_words.add(words[i])
    
    return [0, 0]  # 탈락자가 없을 경우

            