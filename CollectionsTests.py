import unittest
import collections


class CollectionsTests(unittest.TestCase):

    def order_and_len_test(self):
        for i in range(1000):
            testData[i] = i*i
            self.assertEqual(len(testData), i+1)
        for i in range(1000):
            (key, value) = testData.popitem(False)
            self.assertEqual((key, value), (i, i*i))

    def update_tests(self):
        testData.update(test=3, test2=0, test3=-1)
        testData.update(test=3)
        self.assertEqual(testData['test'], 6)
        self.assertEqual(testData['test2'], 0)
        self.assertEqual(testData['test3'], -1)


if __name__ == '__main__':
    unittest.main()