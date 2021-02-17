import unittest
from Adding import task


class Test_Adding(unittest.TestCase):

    test1_in = """  5
                    10 42
                    56 123
                    45 556
                    1000 1000
                    82374 239487
                """

    test1_out = """ 52
                    179
                    601
                    2000
                    321861
                """

    def first_test(self):
        self.assertEqual(tas(10, 42), 52)


if __name__ == "__main__":
    unittest.main()