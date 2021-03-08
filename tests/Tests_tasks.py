import logging

CLASSICAL_BINARY_SEARCH_IN = ["..\\tests\\tests-bin-search" + f"\\{i}.in" for i in range(1, 6)]
CLASSICAL_BINARY_SEARCH_OUT = ["..\\tests\\tests-bin-search" + f"\\{i}.out" for i in range(1, 6)]

ADDING_IN = ["..\\tests\\tests-adding" + f"\\{i}.in" for i in range(1, 3)]
ADDING_OUT = ["..\\tests\\tests-adding" + f"\\{i}.out" for i in range(1, 3)]

BINARY_SEARCH_ON_THE_RESULT_IN = ["..\\tests\\binary-search-on-the-result-tests" + f"\\{i}.in" for i in range(1, 6)]
BINARY_SEARCH_ON_THE_RESULT_OUT = ["..\\tests\\binary-search-on-the-result-tests" + f"\\{i}.out" for i in range(1, 6)]


from Sources.Binary_search import ClassicalSearch
from Sources.Adding import Adding
from Sources.Binary_search import ResultSearch
from Sources.Trees import DefaultTree

logging.basicConfig(level=logging.INFO)


def classical_binary_search_test():
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
            cs = ClassicalSearch(el, mas, n)
            get_result = cs.classical_search()
            if (get_result != right_answer):
                log.info(f"Test {file_id + 1} failed on the position {i} ({el}): expected {right_answer}, were got {get_result}")
                flag = False
            if not flag:
                break
        if flag:
            log.info(f"Test {file_id + 1} passed!")
        fin.close()
        fout.close()


def adding_test():
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

            Add = Adding(a, b)
            get_result = Add.adding()
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


def binary_search_on_the_result_test():
    log = logging.getLogger("BinarySearchOnTheResult")
    for file_id in range(len(BINARY_SEARCH_ON_THE_RESULT_IN)):
        log.info(f"Test {file_id + 1}...")
        fin = open(BINARY_SEARCH_ON_THE_RESULT_IN[file_id], "r")
        fout = open(BINARY_SEARCH_ON_THE_RESULT_OUT[file_id], "r")
        n = int(fin.readline())
        k = int(fin.readline())
        mas = []
        for i in range(n):
            mas.append(int(fin.readline()))
        search = ResultSearch(n, k, mas)
        get_result = search.result_search()
        right_answer = int(fout.readline())

        if (get_result != right_answer):
            log.info(
                f"Test {file_id + 1} failed: expected {right_answer}, were got {get_result}")
        else:
            log.info(f"Test {file_id + 1} passed!")

        fin.close()
        fout.close()


def default_tree_test():
    DefaultTree.try_some_functions()


if __name__ == "__main__":
    """
    classical_binary_search_test()
    adding_test()
    binary_search_on_the_result_test()
    """
    default_tree_test()
