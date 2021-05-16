def print_upper_words(words, must_start_with):
    """print list of words in uppercase that start with a certain letter in supplied list"""
    for word in words:
        for letter in must_start_with:
            if word.lower().startswith(letter):
                print (word.upper())
                break