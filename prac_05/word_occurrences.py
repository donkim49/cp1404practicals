"""
Word Occurrences
Estimate: 20 minutes
Actual:   18 minutes


"""


def count_words(text):
    """Return a dictionary of word counts from the given text string."""
    word_to_count = {}
    for word in text.split():
        word_to_count[word] = word_to_count.get(word, 0) + 1
    return word_to_count


def main():
    text = input("Text: ")
    word_to_count = count_words(text)

    longest = max(len(word) for word in word_to_count)

    for word in sorted(word_to_count):
        print(f"  {word:{longest}} : {word_to_count[word]}")


main()