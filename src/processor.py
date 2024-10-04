import argparse
import os

def count_words(text):
    """
    Count the total number of words in the given text.

    Parameters:
    text (str): The input text to count words from.

    Returns:
    int: The total number of words in the text.
    """
    return len(text.split())

def count_chars(text):
    """
    Count the total number of characters in the given text.

    Parameters:
    text (str): The input text to count characters from.

    Returns:
    int: The total number of characters in the text.
    """
    return len(text)

def count_lines(text):
    """
    Count the number of lines in the given text.

    Parameters:
    text (str): The input text to count lines from.

    Returns:
    int: The total number of lines in the text.
    """
    return len(text.splitlines())

def find_word(text, word):
    """
    Search for a specific word in the text and return its frequency.

    Parameters:
    text (str): The input text to search in.
    word (str): The word to search for.

    Returns:
    int: The frequency of the word in the text.
    """

   

    return text.lower().split().count(word.lower())

def replace_word(text, old_word, new_word):
    """
    Replace a word in the text with another word.

    Parameters:
    text (str): The input text to perform replacement on.
    old_word (str): The word to be replaced.
    new_word (str): The word to replace with.

    Returns:
    str: The modified text with the word replaced.
    """
    return ' '.join([new_word if word.lower() == old_word.lower() else word for word in text.split()])

def process_file(args):
    """
    Process the input file based on the provided command-line arguments.

    Parameters:
    args (argparse.Namespace): The parsed command-line arguments.

    Raises:
    FileNotFoundError: If the specified input file is not found.
    ValueError: If a word to be replaced doesn't exist in the file.
    """
    try:
        with open(args.file, 'r') as file:
            text = file.read()

        if args.word_count:
            print(f"Word Count: {count_words(text)}")

        if args.char_count:
            print(f"Character Count: {count_chars(text)}")

        if args.find:
            occurrences = find_word(text, args.find)
            if(len(args.find) == 1):
                print(f'The word "{args.find}" occurs {occurrences} time.')
            print(f'The word "{args.find}" occurs {occurrences} times.')

        if args.replace:
            old_word, new_word = args.replace
            if find_word(text, old_word) == 0:
                raise ValueError(f'The word "{old_word}" does not exist in the file.')
            modified_text = replace_word(text, old_word, new_word)
            output_file = f"updated_{os.path.basename(args.file)}"
            with open(output_file, 'w') as file:
                file.write(modified_text)
            print(f'"{old_word}" was replaced with "{new_word}" and saved to {output_file}')

    except FileNotFoundError:
        print(f"Error: The file '{args.file}' was not found.")
    except ValueError as e:
        print(f"Error: {str(e)}")

def main():
    """
    Main function to set up argument parsing and call the process_file function.
    """
    parser = argparse.ArgumentParser(description="Process a text file with various operations.")
    parser.add_argument('-f', '--file', required=True, help="Path to the input text file")
    parser.add_argument('-wc', '--word-count', action='store_true', help="Display the total word count")
    parser.add_argument('-cc', '--char-count', action='store_true', help="Display the total character count")
    parser.add_argument('-find', help="A specific word to search in the text file")
    parser.add_argument('-r', '--replace', nargs=2, metavar=('OLD_WORD', 'NEW_WORD'),
                        help="Replace a word in the text file with another word")

    args = parser.parse_args()
    process_file(args)

if __name__ == "__main__":
    main()