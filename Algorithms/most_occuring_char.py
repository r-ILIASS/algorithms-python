sentence = "this is one of the most repeated interview questions"


def most_occuring_char(sentence):
    letters = {}
    for char in sentence:
        if char in letters:
            letters[char] += 1
        else:
            letters[char] = 1

    del letters[' ']

    # Convert the dict to a tuple so we can sort it by value
    sorted_tuple = sorted(letters.items(), key=lambda item: item[1])

    return sorted_tuple[-1]


print(most_occuring_char(sentence))
