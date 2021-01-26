def search(a_list, key):
    cr_op = 0
    start = 0
    end = len(a_list) - 1

    while start <= end:
        cr_op += 1
        mid = (start + end) // 2

        if key == a_list[mid]:
            return cr_op

        else:

            if key < a_list[mid]:
                end = mid - 1

            else:
                start = mid + 1

    return cr_op

# Binary