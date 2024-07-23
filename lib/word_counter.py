check_list = ["below", "down", "go", "going", "horn", "how", "howdy", "it", "i", "low", "own", "part", "partner", "sit"]

#check is the substring exists in the string
#Initiate a variable counting the occurence
#Return the counting in a dictionnary with the associated substring.

def checking_substring(str, array):
  counts = {}
  for substring in array:
    count = str.lower().count(substring)
    if count > 0:
      counts[substring] = count
  sorted_count = dict(sorted(counts.items()))
  return sorted_count
