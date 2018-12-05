import unittest
import collections


class TestCollections(unittest.TestCase):

    def test_prime_path_1(self):
        """
        path: 1 2 4 6 7 13 8 (9 12)*3 9 13 14

        """

        myDict = {"t": 3, "e": 0, "s": -1}
        myList = ""
        testData = collections.Counter()
        testData.update(nonempty=1)
        testData.update(myList, t=3, e=0, s=-1)
        self.assertEqual(testData['t'], 3)
        self.assertEqual(testData['e'], 0)
        self.assertEqual(testData['s'], -1)
        self.assertEqual(testData['nonempty'], 1)

    def test_prime_path_2(self):
        """
        path: 1 2 4 6 7 (11 7)*4 13 8 (9 12)*3 9 13 14

        """

        myDict = {"t": 3, "e": 0, "s": -1}
        myList = "test"
        testData = collections.Counter()
        testData.update(nonempty=1)
        testData.update(myList, t=3, e=0, s=-1)
        self.assertEqual(testData['t'], 5)
        self.assertEqual(testData['e'], 1)
        self.assertEqual(testData['s'], 0)
        self.assertEqual(testData['nonempty'], 1)

    def test_prime_path_3(self):
        """
        path: 1 2 4 6 8 10 13 14

        """

        myDict = {"t": 3, "e": 0, "s": -1}
        myList = "test"
        testData = collections.Counter()
        # testData.update(nonempty=1)
        testData.update(myDict)
        self.assertEqual(testData['t'], 3)
        self.assertEqual(testData['e'], 0)
        self.assertEqual(testData['s'], -1)
        self.assertEqual(testData['nonempty'], 0)

    def test_prime_path_4(self):
        """
        path: 1 2 4 6 8 9 13 14

        """

        myDict = {}
        myList = "test"
        testData = collections.Counter()
        testData.update(nonempty=1)
        testData.update(myDict)
        self.assertEqual(testData['t'], 0)
        self.assertEqual(testData['e'], 0)
        self.assertEqual(testData['s'], 0)
        self.assertEqual(testData['nonempty'], 1)

    def test_prime_path_5(self):
        """
        path: 1 2 4 6 7 13 8 10 13 14


        """

        myDict = {"t": 3, "e": 0, "s": -1}
        myList = ""
        testData = collections.Counter()
        #testData.update(nonempty=1)
        testData.update(myList, t=3, e=0, s=-1)
        self.assertEqual(testData['t'], 3)
        self.assertEqual(testData['e'], 0)
        self.assertEqual(testData['s'], -1)
        self.assertEqual(testData['nonempty'], 0)

    def test_prime_path_6(self):
        """
        path: 1 2 4 13 8 9 (12 9) *3 13 14

        """

        myDict = {"t": 3, "e": 0, "s": -1}
        myList = ""
        testData = collections.Counter()
        testData.update(nonempty=1)
        testData.update(t=3, e=0, s=-1)
        self.assertEqual(testData['t'], 3)
        self.assertEqual(testData['e'], 0)
        self.assertEqual(testData['s'], -1)
        self.assertEqual(testData['nonempty'], 1)

    def test_prime_path_7(self):
        """
        path: 1 2 4 6 8 9 (12 9) *3 13 8 9 (12 9) *3 13 14

        """

        myDict = {"t": 3, "e": 0, "s": -1}
        myList = ""
        testData = collections.Counter()
        testData.update(nonempty=1)
        testData.update(myDict, t=3, e=0, s=-1)
        self.assertEqual(testData['t'], 6)
        self.assertEqual(testData['e'], 0)
        self.assertEqual(testData['s'], -2)
        self.assertEqual(testData['nonempty'], 1)

    def test_prime_path_8(self):
        """
        path: 1 2 4 6 7 13 14

        """

        myDict = {}
        myList = ""
        testData = collections.Counter()
        testData.update(nonempty=1)
        testData.update(myList)
        self.assertEqual(testData['t'], 0)
        self.assertEqual(testData['e'], 0)
        self.assertEqual(testData['s'], 0)
        self.assertEqual(testData['nonempty'], 1)

    def test_prime_path_9(self):
        """
        path: 1 2 4 13 8 10 13 14

        """

        myDict = {"t": 3, "e": 0, "s": -1}
        myList = ""
        testData = collections.Counter()
        #testData.update(nonempty=1)
        testData.update(t=3, e=0, s=-1)
        self.assertEqual(testData['t'], 3)
        self.assertEqual(testData['e'], 0)
        self.assertEqual(testData['s'], -1)
        self.assertEqual(testData['nonempty'], 0)

    def test_prime_path_10(self):
        """
        path: 1 2 4 6 8 10 13 8 9 (12 9) *3 13 14

        """

        myDict = {"t": 3, "e": 0, "s": -1}
        myList = ""
        testData = collections.Counter()
        #testData.update(nonempty=1)
        testData.update(myDict, t=3, e=0, s=-1)
        self.assertEqual(testData['t'], 6)
        self.assertEqual(testData['e'], 0)
        self.assertEqual(testData['s'], -2)
        self.assertEqual(testData['nonempty'], 0)

    def test_prime_path_11(self):
        """
        path: 1 2 4 13 14

        """

        myDict = {"t": 3, "e": 0, "s": -1}
        myList = ""
        testData = collections.Counter()
        #testData.update(nonempty=1)
        testData.update(None)
        self.assertEqual(testData['t'], 0)
        self.assertEqual(testData['e'], 0)
        self.assertEqual(testData['s'], 0)
        self.assertEqual(testData['nonempty'], 0)

    def test_prime_path_12(self):
        """
        path: 1 2 4 6 7 (11 7)*4 13 14

        """

        myDict = {"t": 3, "e": 0, "s": -1}
        myList = "test"
        testData = collections.Counter()
        testData.update(nonempty=1)
        testData.update(myList)
        self.assertEqual(testData['t'], 2)
        self.assertEqual(testData['e'], 1)
        self.assertEqual(testData['s'], 1)
        self.assertEqual(testData['nonempty'], 1)

    def test_prime_path_13(self):
        """
        path: 1 2 4 6 8 10 13 8 10 13 14

        """

        myDict = {}
        myList = ""
        testData = collections.Counter()
        #testData.update(nonempty=1)
        testData.update(myDict, t=3, e=0, s=-1)
        self.assertEqual(testData['t'], 3)
        self.assertEqual(testData['e'], 0)
        self.assertEqual(testData['s'], -1)
        self.assertEqual(testData['nonempty'], 0)

    def test_prime_path_14(self):
        """
        path: 1 2 4 6 8 9 13 8 9 (12 9) *3 13 14

        """

        myDict = {}
        myList = ""
        testData = collections.Counter()
        testData.update(nonempty=1)
        testData.update(myDict, t=3, e=0, s=-1)
        self.assertEqual(testData['t'], 3)
        self.assertEqual(testData['e'], 0)
        self.assertEqual(testData['s'], -1)
        self.assertEqual(testData['nonempty'], 1)

    def test_prime_path_15(self):
        """
        path: 1 2 5

        """
        myDict = {}
        myList = ""
        testData = collections.Counter()
        with self.assertRaises(TypeError):
            testData.update(myDict, myList)

    def test_prime_path_16(self):
        """
        path: 1 3

        """
        with self.assertRaises(TypeError):
            collections.Counter.update()

    def test_blackBox_init(self):
        """
        Testing empty input values
        Testing very long input strings and high values

        """

        self.assertEqual(collections.Counter(), collections.Counter(''))
        self.assertEqual(collections.Counter(), collections.Counter(None))
        self.assertEqual(collections.Counter({'a': 99999999999, 'b': 1}).most_common(2), [('a', 99999999999), ('b', 1)])
        self.assertEqual(collections.Counter({'a': 99999999999, 'b': 1}), collections.Counter(a = 99999999999, b = 1))
        self.assertEqual(collections.Counter({'a': 99999999999, 'b': 99999999999}), collections.Counter(a = 99999999999, b = 99999999999))
        "The test below is not nice, it takes 6 seconds on my computer."
        "Shows you can create a string with very long length though"
        #self.assertEqual(collections.Counter({'a': 9999999, 'b': 1}), collections.Counter("a" * 9999999 + "b"))

    "This function only returns 0 so I will not test it..."
    #def test_blackbox_missing(self):
    #   self.assertEqual()

    "To be implemented"
    def test_blackbox_update(self):
        self.assertEqual(1,1)

    "To be implemented"
    def test_blackbox_most_common(self):
        self.assertEqual(1,1)
if __name__ == '__main__':
    unittest.main()
