#create the function which will convert the word into the encoded one
  #ord(letter)+3
  # z -> a

def get_word():
  while True:
    word = input("Veuillez rentrer votre message, sans espaces, sans caractères spéciaux, sans chiffres \n ----> ")
    if word.isalpha():
      return word
    else:
      print("Erreur, le message ne doit contenir que des caractères alphabétiques")

def get_number():
  while True:
    try:
      number = int(input("Entrez la clé de décalage: "))
      return number
    except ValueError:
      print("Erreur, vous devez rentrer un nombre")


def caesar_cipher(word, key):
    result = []
    for letter in word:
        if letter.islower():
            # Calculate shifted position and wrap around if necessary
            shifted = (ord(letter) - ord('a') + key) % 26 + ord('a')
            result.append(chr(shifted))
        elif letter.isupper():
            # Calculate shifted position and wrap around if necessary
            shifted = (ord(letter) - ord('A') + key) % 26 + ord('A')
            result.append(chr(shifted))
    return "".join(result)


def main():
  message = get_word()
  number = get_number()
  encoded_message = caesar_cipher(message, number)
  print(f"From {message}, here is the encoded version --> {encoded_message}")

main()
