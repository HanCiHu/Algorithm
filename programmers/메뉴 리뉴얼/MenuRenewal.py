from itertools import combinations
from collections import Counter

def solution(orders, course):
    ans = []
    for C in course:
        temp = []
        for order in orders:
            comb = combinations(sorted(order), C)
            temp += comb
        counter = Counter(temp)
        if len(counter) != 0 and max(counter.values()) > 1:
            for i in counter:
                if counter[i] == max(counter.values()):
                    ans.append(''.join(i))
    return sorted(ans)