def solution(x,n):
    result=[]
    for i in range(1, n+1):
        result.append(x*i)
    return result

result = solution(2,5)
print(result)
result2 = solution(4,3)
print(result2)
result3 = solution(-4,2)
print(result3)