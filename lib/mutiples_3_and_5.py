def creating_list(length):
  return [num for num in range(length+1)]

def sorting_out_multiples_of_3_or_5(array):
  return [num for num in array if num % 3 == 0 or num % 5 == 0]
