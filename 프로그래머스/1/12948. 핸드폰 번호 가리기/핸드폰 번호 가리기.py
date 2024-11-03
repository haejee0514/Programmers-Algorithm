def solution(phone_number):
    phone_number = str(phone_number)  # 숫자를 문자열로 변환
    return "*" * (len(phone_number) - 4) + phone_number[-4:]