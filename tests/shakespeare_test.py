from lib.shakespeare import checking_words_in_shakespeare

def test_checking_words_in_shakespeare():
  list = ["a", "b", "c", "d", "e", "f" ,"g" ,"h", "i", "j" ,"k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
  assert checking_words_in_shakespeare("Piggy", list) == {"g": 2, "i": 1, "p": 1, "y": 1}
