from lib.crypto import caesar_cipher

def test_caesar_cipher():
  message = "Mugiwara"
  number = 10

  assert caesar_cipher(message, number) == "Weqsgkbk"
