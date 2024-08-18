from random import randint

def creating_list(length):
  return [num for num in range(length+1)]

def sorting_out_multiples_of_3_or_5(array):
  print(f"Sorting numbers up to {max(array)}")
  return [num for num in array if num % 3 == 0 or num % 5 == 0]

if __name__ == "__main__":
  res = sorting_out_multiples_of_3_or_5(creating_list(randint(50, 500)))
  print(res)
