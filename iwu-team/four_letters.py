def four_letters(sentence):
    """
    info
    """
    # to_parse = str(sentence)
    list_of_words = str(sentence).split(' ')
    print(list_of_words)

    count = 0

    for word in list_of_words:
        print(len(word))
        if len(word) == 4:
            print(word)
            count = count + 1

    print(count)
    return count

four_letters('This sentence is fine')