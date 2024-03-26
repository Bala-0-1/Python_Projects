def find_subarrays(arr, length):
    subarrays = []
    for i in range(len(arr) - length + 1):
        subarray = arr[i:i+length]
        subarrays.append(subarray)
    return subarrays

# Example usage:

my_list = [1, 2, 3, 4, 5, 6, 7]
subarrays = find_subarrays(my_list, 3)
print(subarrays)
