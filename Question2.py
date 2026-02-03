# opening and reading the file as sample_file
# Then it reads the file and stores it in a variable to then be later split up into tokens

with open (file=r'C:\Users\natet\DATA221\Github\Assignment2\sample-file.txt', mode="r") as sample_file:
    sample_file_content = sample_file.read()
    tokens = sample_file_content.split()

# intizaling the dictionary that I will store the cleaned up words in
list_of_clean_words = []

# goes through each word in tokens and turns them lowercase as well as strips them of punctuation
# then it keeps and appends only tokens that contain at least two alphabetic characters
for word in tokens:
    clean_word = word.lower().strip(".,!?")

    if sum(char.isalpha() for char in clean_word) >= 2:
        list_of_clean_words.append(clean_word)

# intializing the dictionary for the bigrams to be stored into
final_dictionary_bigram = {}

# goes through the list of cleaned words and constructs the bigrams with a space in between the words
# counts them as well using a conditional statement
for i in range (len(list_of_clean_words)-1):
    bigram = (list_of_clean_words[i] + " " + list_of_clean_words[i+1])

    if bigram in final_dictionary_bigram:
        final_dictionary_bigram[bigram] +=1
    else:
        final_dictionary_bigram[bigram] = 1

# sorts the bigrams
sorted_bigrams = sorted(final_dictionary_bigram.items(), key=lambda x: x[1], reverse=True)

# prints the top 5 most frequent bigrams
for word, count in sorted_bigrams[:5]:
    print(f"{word} -> {count}", end=" ")

