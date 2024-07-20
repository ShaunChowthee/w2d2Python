from lib.mutiples_3_and_5 import creating_list, sorting_out_multiples_of_3_or_5

def test_creating_list():
	assert creating_list(1000) == list(range(1001))
	assert creating_list(250) == list(range(251))

def test_sorting_out_mutiples_of_3_or_5():
	assert sorting_out_multiples_of_3_or_5([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [0, 3, 5, 6, 9, 10]
	assert sorting_out_multiples_of_3_or_5([0, 2, 4, 7, 8]) == [0]
	assert sorting_out_multiples_of_3_or_5([1, 2, 3, 5, 15, 30, 31]) == [3, 5, 15, 30]
	assert sorting_out_multiples_of_3_or_5(list(range(11))) == [0, 3, 5, 6, 9, 10]
