# defining the function with two parameters
def find_lines_containing(filename, keyword):
    # creating the list that will contain the line numbers and line text that have the keyword inside them
    # also making the keyword case-insensitive
    matching_lines = []
    lower_keyword = keyword.lower()

    global line_number
    line_number = 1

    # opening the file and then checking if there is the keyword within each line and if there is appending the line text and line number to the list
    with open (filename, "r") as sample_file:
        for line in sample_file :
            if lower_keyword in line.lower():
                matching_lines.append((line_number, line.strip()))

            line_number += 1

    return matching_lines

# storing the result into result
result = find_lines_containing(r"C:\Users\natet\DATA221\Github\Assignment2\sample-file.txt", "data")

# print statements
print(f"There were {len(result)} keywords in the file")
print(f"The first 3 matching lines were {result[0]}, {result[1]}, {result[2]}")
