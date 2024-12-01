from functools import reduce
from operator import add

def idata(itext):
	return [[int(nr) for nr in line.strip().split()] for line in itext.strip().split("\n")]

def tworows(i_data):
	return (sorted([d[0] for d in i_data]), sorted([d[1] for d in i_data]))

def sum_of_dif(two_rows_of_data):
	return reduce(add, [abs(two_rows_of_data[0][elem]- two_rows_of_data[1][elem]) for elem in range(len(two_rows_of_data[0]))])

def similarity_score(two_rows_of_data):
	return reduce(add, [elem*two_rows_of_data[1].count(elem) for elem in two_rows_of_data[0]])


if __name__ == "__main__":
	with open("day1input", "r") as itextfile:
		input = tworows(idata(itextfile.read()))
	print("Total distance = {}".format(sum_of_dif(input)))
	print("Similarity score = {}".format(similarity_score(input)))
