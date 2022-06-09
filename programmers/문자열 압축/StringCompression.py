def solution(s):
    answer = float('inf')
    for i in range(1, len(s) + 1, 1):
        zip = s[0:i]
        cnt = 0
        repeat = 1
        for j in range(i, len(s) + 1, i):
            if s[j:j+i] == zip:
                repeat += 1
                continue
            if s[j:j+i] != zip:
                if repeat > 1:
                    zip = s[j:j+i]
                    if repeat // 10 == 0:
                        cnt += i + 1
                    else:
                        cnt += i + len(str(repeat // 10)) + 1
                    repeat = 1
                else:
                    cnt += i
                    zip = s[j:j+i]
        
        if len(s) % i != 0:
            cnt += len(s) % i
        answer = min(answer, cnt)
                
        
    return answer