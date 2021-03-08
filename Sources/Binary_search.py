class ClassicalSearch:

    def __init__(self, el, mas, n):
        self.el = el
        self.mas = mas
        self.N = n

    def classical_search(self):
        left = 0
        right = self.N - 1
        while True:
            middle = (left + right) // 2
            if self.mas[middle] > self.el:
                right = middle
            elif self.mas[middle] < self.el:
                left = middle
            elif self.mas[middle] == self.el:
                return middle
            if right - left <= 1:
                if self.mas[left] == self.el:
                    return left
                elif self.mas[right] == self.el:
                    return right
                else:
                    return -1


class ResultSearch:

    def __init__(self, N, K, mas):
        self.N = N
        self.K = K
        self.mas = mas

    def __check(self, lenght):
        count = 1
        current_len = self.mas[0] + lenght
        for i in range(1, self.N):
            if self.mas[i] > current_len:
                count += 1
                current_len = self.mas[i] + lenght
        return count <= self.K

    def result_search(self):
        left = 0
        right = self.mas[self.N - 1] - self.mas[0]
        answer = 0
        if len(self.mas) == 1:
            return answer
        while True:
            middle = (left + right) // 2
            if self.__check(middle):
                right = middle
                answer = right
            else:
                left = middle
            if right - left <= 1:
                return answer
