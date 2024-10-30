def main():
    file_path = "books/frankenstein.txt"
    text = get_text(file_path)
    num_words = word_count(text)
    chars_dict = character_count(text)
    chars_sorted_list = sort_character_count(chars_dict)

    print(f"--- Begin report of {file_path} ---")
    print(f"{num_words} words found in the document\n")

    # Iterate and print the results
    for char, count in chars_sorted_list:
        print(f"The character '{char}' was found {count} times.")  
    
    print("--- End Report ---")

def get_text(path):
    with open(path) as f:
        file_contents = f.read()
    return(file_contents)

def word_count(text):
    words = text.split()
    return(len(words))

def character_count(text):
    characters = {}

    for char in text.lower():
        if char in characters:
            characters[char] += 1
        if char not in characters and char.isalpha():
            characters[char] = characters.get(char, 0) + 1
    
    return(characters)

def sort_character_count(character_count_dict):

    # Convert the character count issue to a list of tuples
    char_list = list(character_count_dict.items())

    # Sort the list by count in descending order
    char_list.sort(key=lambda x: x[1], reverse=True)

    return(char_list)

main()