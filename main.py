def main():
    book_path = "books/frankenstein.txt"
    text = get_strings(book_path)
    word_count = get_book_wordcount(text)
    num_char = get_num_char(text)
    list = conv_dict(num_char)
    list.sort(reverse=True, key=ret_num)

    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document")
    print("")
    for x in list:
        letter = x["char"]
        values = x["value"]
        print(f"The '{letter}' character was found {values} times")
    print(f"--- End report ---")
    

# Returns file as a string
def get_strings(book_path):
    with open(book_path) as f:
        return f.read()

# Returns number of words in the file
def get_book_wordcount(text):
    words = text.split()
    count = 0
    for word in words:
        count += 1
    return count
    
# Returns the number of each individual character in a document
def get_num_char(text):
    char_count = {}
    words = text.split()
    for word in words:
        lower_case = word.lower()
        for char in lower_case:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    return char_count

# Convert dictionary into a list of dictionaries, excludes not alphabet characters
def conv_dict(num_char):
    char_list = []
    char = "char"
    value = "value"
    for x in num_char:
        if x.isalpha():
            char_list.append({char: x, value: num_char[x]})
    return char_list
    
# Set key to be sorted
def ret_num(dict):
    return dict["value"]
        
    

main()