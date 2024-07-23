from lib.word_counter import checking_substring


def test_checking_substring():
  check_list = ["below", "down", "go", "going", "horn", "how", "howdy", "it", "i", "low", "own", "part", "partner", "sit"]

  assert checking_substring("how", check_list) == {"how": 1}
  assert checking_substring("HOW", check_list) == {"how": 1}
  assert checking_substring("Easy partner, there you go", check_list) == {"go": 1, "part": 1, "partner": 1}
