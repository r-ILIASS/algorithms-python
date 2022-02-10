def binary_search(list, target):
    # Keep track of list positions
    first = 0
    last = len(list) - 1

    # Keep looping as long as first <= last
    while first <= last:
        # Calculate the midpoint of the list
        midpoint = (first + last) // 2

        # if the value at this position = target return the position value
        if list[midpoint] == target:
            return midpoint
        # If the value at this position < target set first to this postion + 1
        elif list[midpoint] < target:
            first = midpoint + 1
        # else set last to this postion - 1
        else:
            last = midpoint - 1

    return None


def verify(index):
    if index is not None:
        print("Target found in index: ", index)
    else:
        print("Target not found")


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

verify(binary_search(numbers, 8))
