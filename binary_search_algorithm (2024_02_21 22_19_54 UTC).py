def binary_search(list, element):
    start = 0
    middle = 0
    end = len(list)
    steps = 0

    while start <= end:
        print("Step", steps, ":", str(list[start:end + 1]))

        steps += 1
        middle = (start + end) // 2

        if element == list[middle]:
            return middle
        elif element < list[middle]:
            end = middle - 1
        else:
            start = middle + 1

    return -1


mylist = [1, 2, 3, 4, 5, 6, 7, 8]
target = 4

binary_search(mylist, target)
