import bisect

def dict_find(n_dict, t):
	if t in n_dict.values():
		return 1
	else :
		return 0

def bin_ser(input_list, t):
	input_list.sort()
	if bisect.bisect(input_list, t) >= 0:
		print("ret: ",bisect.bisect(input_list, t))
		return 1
	else:
		return 0

target = int(input())
input_key_string = input().strip().split()
input_val_value = list(map(int, input_key_string))
input_dict = dict(zip(input_key_string, input_val_value))
print(dict_find(input_dict,target))
print(bin_ser(list(input_val_value), target))