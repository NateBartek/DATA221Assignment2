# opening and reading the file as sample_file
# Then it reads the file and stores it in a variable to then be later split up into tokens
with open (file=r'C:\Users\natet\DATA221\Github\Assignment2\sample-file.txt', mode="r") as sample_file:
    sample_file_content = sample_file.read()
    tokens = sample_file_content.split()

# intizaling the dictionary that I will store the cleaned up words in
final_dictionary = {}

# goes through each word in tokens and turns them lowercase as well as strips them of punctuation
# then it checks to see if it is 2 or more alphabetic characters before counting the frequency of it and adding it to the final dictionary
for word in tokens:
    clean_word = word.lower().strip(".,!?")

    if sum(char.isalpha() for char in clean_word) >= 2:
        if clean_word in final_dictionary:
            final_dictionary[clean_word] += 1
        else:
            final_dictionary[clean_word] = 1

# sorts the final dictionary by frequency of words and reverses it so that the most common are first in the list
sorted_words = sorted(final_dictionary.items(), key=lambda x: x[1], reverse=True)

# prints the word and the count on the same line for the first 10 words
for word, count in sorted_words[:10]:
    print(f"{word} -> {count}", end=" ")


