import unittest
import collections


class CollectionsTests(unittest.TestCase):

    def order_and_len_test(self):
        testData = collections.OrderedDict()
        for i in range(1000):
            testData[i] = i*i
            self.assertEqual(len(testData), i+1)
        for i in range(1000):
            (key, value) = testData.popitem(False)
            self.assertEqual((key, value), (i, i*i))


if __name__ == '__main__':
    unittest.main()