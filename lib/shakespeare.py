from pathlib import Path

def checking_words_in_shakespeare(corpus, array):
    counts = {}
    corpus_lower = corpus.lower()
    for word in array:
        count = corpus_lower.count(word.lower())  # Make the search case-insensitive
        if count > 0:
            counts[word] = count
    return counts

# Correctly set the file paths relative to the script's location
current_dir = Path(__file__).parent

# Reading Shakespeare text file
txt_shakespeare_file_path = current_dir / 'text_shakespeare.txt'
txt_shakespeare_file = txt_shakespeare_file_path.read_text(encoding='utf-8')

# Define the dictionary of words
dictionary = ["the", "of", "and", "to", "a", "in", "for", "is", "on", "that", "by", "this", "with", "i", "you", "it", "not", "or", "be", "are"]

# Check the words in the Shakespeare file
sp_file = checking_words_in_shakespeare(txt_shakespeare_file, dictionary)
print(sp_file)

# Reading bad words file
bad_words_file_path = current_dir / 'bad_words.txt'
bad_words_file = bad_words_file_path.read_text(encoding='utf-8').split()

# Check the bad words in the Shakespeare file
bw_file = checking_words_in_shakespeare(txt_shakespeare_file, bad_words_file)
print()
print(bw_file)
