def solution(phone_number):
    phone_number = str(phone_number) 
    return "*" * (len(phone_number) - 4) + phone_number[-4:]