import logging
import math


logging.basicConfig(filename='aritmetika.log', level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s')

def sum(*args):
	total = 0
	for x in args:
		total += x
	logging.info(f"suma: {total}")

	return total


sum(2,5,6)

def square_root(x: float) -> float :
	answer = math.sqrt(x)
	logging.info(f"square root: {answer}")
	return answer


square_root(9)

def len_of_sentence(x):
	answer = len(x)
	logging.info(f"lenght of sentence: {answer}")
	return answer

len_of_sentence("Hey There")