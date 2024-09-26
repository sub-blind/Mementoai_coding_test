def solution(phone_number):
    result = ''
    for i in range(0, len(phone_number)-4):
        result += '*'
    return result+phone_number[-4:]
    
result = solution("01033334444")
print(result)
result2 = solution("027778888")
print(result2)