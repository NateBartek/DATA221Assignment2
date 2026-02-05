# opening the file that I will be working with and saving each line to a list
with open (file=r'C:\Users\natet\DATA221\Github\Assignment2\sample-file.txt', mode="r") as sample_file:
    sample_file_content = sample_file.readlines()

# creating my list for the clean lines
clean_lines = []
punctuation = ".,-"

# a nested loop that goes through each element in the list and cleans them and then appends them to the clean lines list
for line in sample_file_content:
    lowercase_line = line.lower()

    cleaned_line = lowercase_line
    for p in punctuation:
        cleaned_line = cleaned_line.replace(p, "")

    cleaned_line = cleaned_line.replace(" ", "").strip()

    clean_lines.append(cleaned_line)

# removes the lines that are just empty spaces
while "" in clean_lines:
    clean_lines.remove("")

clean_lines_dict = {}

key = 1

# saves the clean lines to a dict with an increasing key so that we know what line they're on
for line in clean_lines:
    clean_lines_dict[key] = line
    key += 1

# compares each line to one another and then prints the line number
for i in clean_lines_dict:
    for j in clean_lines_dict:
        if i < j:
            if clean_lines_dict[i] == clean_lines_dict[j]:
                print(f"Lines {i} and {j} form one near-duplicate set")
