import argparse


def main():
    # Arg parser to take file path from user as arg
    parser = argparse.ArgumentParser(
        description="Processes a file_contents file (ie. .md, .txt, .html)"
    )
    parser.add_argument("input_file_path", help="Path to the file_contents file")
    args = parser.parse_args()

    # Extract file path and read file_contents
    file_contents = read_file_contents(args.input_file_path)

    # Perform analysis
    total_word_count = count_words(file_contents)
    character_frequency_dict = count_characters(file_contents)
    sorted_character_frequencies = sort_count_characters(character_frequency_dict)

    # Print the report
    print_report(args.input_file_path, total_word_count, sorted_character_frequencies)


def print_report(input_file_path, total_word_count, sorted_character_frequencies):
    # Prints a report of word and character count data
    print(f"--- Begin report of {input_file_path} ---")
    print(f"{total_word_count} words found in the document\n")

    # Iterate and print the results
    for char, count in sorted_character_frequencies:
        print(f"The character '{char}' was found {count} times.")
    print("--- End Report ---")


def read_file_contents(path):
    # Gets the file_contents from the file path
    with open(path) as f:
        file_contents = f.read()
    return file_contents


def count_words(file_contents):
    # Counts the words in the file_contents
    words = file_contents.split()
    return len(words)


def count_characters(file_contents):
    # Counts the characters in the file_contents, adds the count to a dict
    characters = {}

    for char in file_contents.lower():
        if char.isalpha():  # Check if the character is alphabetic
            characters[char] = characters.get(char, 0) + 1  # Increment the count

    return characters


def sort_count_characters(count_characters_dict):
    # Convert the character count issue to a list of tuples
    char_list = list(count_characters_dict.items())

    # Sort the list by count in descending order
    char_list.sort(key=lambda x: x[1], reverse=True)

    return char_list


if __name__ == "__main__":
    main()