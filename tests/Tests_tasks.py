import logging
from Sources.Binary_search import ClassicalSearch
from Sources.Adding import Adding
from Sources.Binary_search import ResultSearch
from Sources.Trees import DefaultTree, Treap

CLASSICAL_BINARY_SEARCH_IN = [f"..\\tests\\tests-bin-search\\{i}.in" for i in range(1, 6)]
CLASSICAL_BINARY_SEARCH_OUT = [f"..\\tests\\tests-bin-search\\{i}.out" for i in range(1, 6)]

ADDING_IN = [f"..\\tests\\tests-adding\\{i}.in" for i in range(1, 3)]
ADDING_OUT = [f"..\\tests\\tests-adding\\{i}.out" for i in range(1, 3)]

BINARY_SEARCH_ON_THE_RESULT_IN = [f"..\\tests\\binary-search-on-the-result-tests\\{i}.in" for i in range(1, 6)]
BINARY_SEARCH_ON_THE_RESULT_OUT = [f"..\\tests\\binary-search-on-the-result-tests\\{i}.out" for i in range(1, 6)]

SEARCH_TREES_IN = [f"..\\tests\\search-trees-tests\\{i}.in" for i in range(1, 7)]
SEARCH_TREES_CONTAINS_OUT = [f"..\\tests\\search-trees-tests\\{i}.contains.out" for i in range(1, 7)]

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
    log = logging.getLogger("DefaultTree")
    for file_id in range(len(SEARCH_TREES_IN)):
        tree = DefaultTree()
        tree.get_tree()
        log.info(f"Contains test {file_id + 1}...")
        fin = open(SEARCH_TREES_IN[file_id], "r")
        fout = open(SEARCH_TREES_CONTAINS_OUT[file_id], "r")
        n = int(fin.readline())
        flag = True
        for i in range(n):
            value = int(fin.readline())
            answer = fout.readline().replace("\n", "")
            if tree.proof_node(value) != answer:
                flag = False
                log.info(f"Test {file_id + 1} failed: expected {answer}, on the value {value}, "
                         f"number of value: {i + 1}")
                break
        if flag:
            log.info(f"Test {file_id + 1} passed!")


def treap_test():
    treap = Treap(node_count=10)
    treap.get_treap()


if __name__ == "__main__":
    # classical_binary_search_test()
    # adding_test()
    # binary_search_on_the_result_test()
    default_tree_test()
    # treap_test()
