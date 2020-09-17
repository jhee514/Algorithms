def solution(numbers):
    l = len(numbers)
    for i in range(l-1):
        cur = str(numbers[i])
        mx_idx = i
        mx_str = cur
        
        for j in range(i+1, l):
            next = str(numbers[j])
            if int(next+cur) >= int(cur+next):
                tmp_mx = j
                if int(mx_str+next) < int(next+mx_str):
                    mx_idx = j
                    mx_str = next
        numbers[i], numbers[mx_idx] = numbers[mx_idx], numbers[i]
    answer = ''
    for n in numbers:
        answer += str(n)
    answer = str(int(answer))
    return answer
    
    
nums = [3, 30, 34, 5, 9]
print(solution(nums))
