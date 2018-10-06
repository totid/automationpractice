import unittest
from tests.FunctionalTests import FunctionalTests


def suite():
    s = unittest.TestSuite()
    s.addTest(FunctionalTests('test_open_page'))
    return s


if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())
