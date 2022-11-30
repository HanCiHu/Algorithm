from collections import Counter
def solution(k, tangerine):
    t = Counter(tangerine).most_common()
    answer = 0
    ret = 0
    for i in t:
        if answer < k:
            answer += i[1]
            ret += 1
    return ret