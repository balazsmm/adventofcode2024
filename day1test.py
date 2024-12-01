import unittest
from day1 import idata, sum_of_dif, tworows, similarity_score


testdata = """3   4
4   3
2   5
1   3
3   9
3   3"""


class MyTestCase(unittest.TestCase):
	def test_diff_sum(self):
		self.assertEqual(sum_of_dif(tworows(idata(testdata))), 11)
		self.assertEqual(similarity_score(tworows(idata(testdata))), 31)


if __name__ == '__main__':
	unittest.main()
