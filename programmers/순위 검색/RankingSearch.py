def solution(info, query):
    answer = []
    db = {}
    
    for lang in ['cpp', 'java', 'python', '-']:
        for position in ['backend', 'frontend', '-']:
            for year in ['junior', 'senior', '-']:
                for food in ['chicken', 'pizza', '-']:
                    db.setdefault((lang, position, year, food), [])

    for i in info:
        i = i.split(' ')
        
        for lang in [i[0], '-']:
            for position in [i[1], '-']:
                for year in [i[2], '-']:
                    for food in [i[3], '-']:
                        db[lang, position, year, food].append(int(i[4]))
    
    for key in db:
        db[key].sort()
    
    for q in query:
        q = q.split(' ')
        
        data = db[(q[0], q[2], q[4], q[6])]
        target = int(q[7])
        
        left = 0
        right = len(data)
        
        while left < right:
            mid = (left + right) // 2
            
            if data[mid] >= target:
                right = mid
            else:
                left = mid + 1
        
        answer.append(len(data) - left)
    return answer