def solution(new_id):
    new_id = new_id.lower()
    new_id = ''.join(list(filter(lambda x: x in [chr(ord('a') + i) for i in range(26)] + ['-','_','.'] + [str(i) for i in range(10)], new_id)))
    new_id = new_id.replace('..', '.')
    temp = ''
    flag = True
    for n in new_id:
        if n == '.' and flag:
            temp += n
            flag = False
        elif n != '.':
            temp += n
            flag = True
    new_id = temp
    if new_id[0] == '.':
        if len(new_id) == 1: new_id = ''
        else: new_id = new_id[1:]
    if len(new_id) > 0 and new_id[-1] == '.': new_id = new_id[:-1]
    if len(new_id) == 0: new_id = 'a'
    if len(new_id) >= 16: new_id = new_id[:15]
    if new_id[-1] == '.': new_id = new_id[:-1]
    if len(new_id) <= 2: new_id += new_id[-1]
    if len(new_id) <= 2: new_id += new_id[-1]
    return new_id