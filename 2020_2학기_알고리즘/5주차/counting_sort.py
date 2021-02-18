def counting_sorted(arr, K):
    c = [0] * K
    sorted_arr = [0] * len(arr)

    for i in arr:
        c[int(i)] += 1

    for i in range(1,K):
        c[i] += c[i-1]

    for i in range(len(arr)):
        sorted_arr[c[arr[i]]-1] = arr[i]
        c[arr[i]] -= 1
    return sorted_arr

input_list = list(map(int,input().split(' ')))
print(counting_sorted(input_list,100))
