import json
import difflib
from langdetect import detect

from get_input_args import get_input_args


def find_similar_words(input_word, dictionary, cutoff, n):
    """
    Find and return similar words from the dictionary based on the input word.
    
    :param input_word: The word input by the user.
    :param dictionary: The dictionary to search for similar words.
    :param cutoff: The minimum similarity ratio (0 to 1) to consider a word as similar.
    :return: A list of tuples containing similar words and their meanings.
    """
    similar_keys = difflib.get_close_matches(input_word, dictionary.keys(), n=n, cutoff=cutoff)
    return [(key, dictionary[key]) for key in similar_keys]

def main():
    
    # Load the json files
    with open("math_ar_to_en_dict.json", 'r', encoding='utf-8') as file:
        ar_to_en_dict = json.load(file)
        
    with open("math_en_to_ar_dict.json", 'r', encoding='utf-8') as file:
        en_to_ar_dict = json.load(file)
    
    input_args = get_input_args()
    cutoff = input_args.cutoff
    n = input_args.number
    
    while True:
        user_input = input("Enter a mathematical term in Arabic or English (or type 'exit' to quit):\n").strip()
        if user_input.lower() == 'exit':
            print("Exiting the dictionary. Goodbye!")
            break
        elif not user_input:
            print("Please enter a valid input.")
            continue
        
        # check the language of user input
        lang = detect(user_input)
        if lang == 'ar':
            results = find_similar_words(user_input, ar_to_en_dict, cutoff=cutoff, n=n)
        else:
            results = find_similar_words(user_input, en_to_ar_dict, cutoff=cutoff, n=n)
        
        if results:
            print("\nFound matches:")
            for key, value in results:
                print(f"{key}: {value}")
        else:
            print("No similar words found.")
        
        print("\n")

if __name__ == "__main__":
    main()


    