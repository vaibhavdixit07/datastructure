def isArraySorted(array):
    if len(array) == 1:
        return True
    else:
        return array[0] < array[1] and isArraySorted(array[1:])


if __name__ == '__main__':
    print(isArraySorted(list(range(1, 995))))
