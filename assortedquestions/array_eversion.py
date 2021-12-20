num_tests = int(input())
n_values = []
arrays_n = []
for i in range(num_tests):
    temp_n = int(input())
    n_values.append(temp_n)
    temp_array_n = list(map(int, input().strip().split(" ")))
    arrays_n.append(temp_array_n)


def find_num_eversions(array_n, k):
    last_val = array_n[-1]
    if last_val == max(array_n):
        return k
    else:
        new_array = []
        for item in array_n:
            if item > last_val:
                new_array.append(item)
        return find_num_eversions(new_array, k+1)


for arr_n in arrays_n:
    print(find_num_eversions(arr_n, 0))
