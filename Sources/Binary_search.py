def classical_search(el, mas, N):
    left = 0
    right = N - 1
    while True:
        middle = (left + right) // 2
        if mas[middle] > el:
            right = middle
        elif mas[middle] < el:
            left = middle
        elif mas[middle] == el:
            return middle
        if right - left <= 1:
            if mas[left] == el:
                return left
            elif mas[right] == el:
                return right
            else:
                return -1