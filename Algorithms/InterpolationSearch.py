def search(a_list, key):
    cr_op = 0
    end = len(a_list) - 1
    start = 0

    while key >= a_list[start] and key <= a_list[end] and start <= end:
        cr_op += 1
        position = start + (key - a_list[start]) * (end - start) // (a_list[end] - a_list[start])
        if start == end:
            if a_list[start] == key:
                return cr_op
            return cr_op

        if a_list[position] == key:
            return cr_op

        if a_list[position] > key:
            end = position - 1

        else:
            start = position + 1

    return cr_op

# Interpolation