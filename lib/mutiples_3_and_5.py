def creating_list(length):
  return [num for num in range(length+1)]

def sorting_out_multiples_of_3_or_5(array):
  return [num for num in array if num % 3 == 0 or num % 5 == 0]

to_1000_list = creating_list(1000)
final_list = sorting_out_multiples_of_3_or_5(to_1000_list)
print(final_list)
