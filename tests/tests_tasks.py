import logging

CLASSICAL_BINARY_SEARCH_IN = ["..\\tests\\tests-bin-search" + f"\\{i}.in" for i in range(1, 6)]
CLASSICAL_BINARY_SEARCH_OUT = ["..\\tests\\tests-bin-search" + f"\\{i}.out" for i in range(1, 6)]

ADDING_IN = ["..\\tests\\tests-adding" + f"\\{i}.in" for i in range(1, 3)]
ADDING_OUT = ["..\\tests\\tests-adding" + f"\\{i}.out" for i in range(1, 3)]

from Sources.Binary_search import classical_search
from Sources.Adding import adding

logging.basicConfig(level=logging.INFO)


def Classical_binary_saerch_test():
    log = logging.getLogger("ClassicalBinarySearch")
    for file_id in range(len(CLASSICAL_BINARY_SEARCH_IN)):
        log.info(f"Test {file_id + 1}...")
        fin = open(CLASSICAL_BINARY_SEARCH_IN[file_id], "r")
        fout = open(CLASSICAL_BINARY_SEARCH_OUT[file_id], "r")
        n = int(fin.readline())
        mas = fin.readline().split()
        mas = [int(i) for i in mas]
        k = int(fin.readline())
        flag = True
        for i in range(k):
            el = int(fin.readline())
            right_answer = int(fout.readline())
            get_result = classical_search(el, mas, n)
            if (get_result != right_answer):
                log.info(f"Test {file_id + 1} failed on the position {i} ({el}): expected {right_answer}, were got {get_result}")
                flag = False
            if not flag:
                break
        if flag:
            log.info(f"Test {file_id + 1} passed!")
        fin.close()
        fout.close()


def Adding_test():
    log = logging.getLogger("Adding")
    for file_id in range(len(ADDING_IN)):
        log.info(f"Test {file_id + 1}...")
        fin = open(ADDING_IN[file_id], "r")
        fout = open(ADDING_OUT[file_id], "r")
        a = int(fin.readline())
        flag = True
        for i in range(a):
            x, y = fin.readline().split(' ')
            if len(x) > 9 or len(y) > 9:
                a, b = list(x), list(y)
                a.reverse()
                b.reverse()
                if b[0] == '\n':
                    b.pop(0)
            else:
                a, b = int(x), int(y)

            get_result = adding(a, b)
            right_answer = type(get_result)(fout.readline())
            if type(right_answer) == str:
                if right_answer[-1] == "\n":
                    try:
                        right_answer = right_answer[:-1]
                    except:
                        pass

            if (get_result != right_answer):
                log.info(
                    f"Test {file_id + 1} failed on the position {i} ({a, b}): expected {right_answer}, were got {get_result}")
                flag = False
            if not flag:
                break

        if flag:
            log.info(f"Test {file_id + 1} passed!")

        fin.close()
        fout.close()


if __name__ == "__main__":
    #Classical_binary_saerch_test()
    Adding_test()



