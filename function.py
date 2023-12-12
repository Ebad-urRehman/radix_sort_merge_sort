# max_len is the maximum length of a string or number in list
def radix_sort(my_list, max_len):
    n = 1
    current_len = 0
    while current_len != max_len:
        current_len += 1
        junk_list = []
        bucket_list = [None] * 10
        for i, elements in enumerate(my_list):
            ele_to_sort = int((my_list[i]/n) % 10)
            print(ele_to_sort)
            if bucket_list[ele_to_sort] is None:
                bucket_list[ele_to_sort] = [my_list[i]]
            else:
                bucket_list[ele_to_sort].append(my_list[i])
            print(f"unit place : {(my_list[i]/n) % 10}")
            print(my_list[i])
        for i, sub_list in enumerate(bucket_list):
            if sub_list is not None:
                print(sub_list)
                junk_list += sub_list
        my_list = junk_list
        n *= 10
        print(my_list)








if __name__ == "__main__":
    list_my = [23, 1, 45, 234, 5, 7, 89]
    radix_sort(list_my, max_len=3)