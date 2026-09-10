# Program 2: Automated Word Frequency & Pattern Analyzer

import string
from collections import Counter


def analyze_text(text):
    # Convert text to lowercase
    text = text.lower()

    # Remove punctuation
    text = text.translate(str.maketrans("", "", string.punctuation))

    # Split into words
    words = text.split()

    # Count word frequency
    frequency = Counter(words)

    # Find palindromes
    palindromes = []

    for word in set(words):
        if len(word) > 1 and word == word[::-1]:
            palindromes.append(word)

    return words, frequency, palindromes


def main():
    print("===== Word Frequency & Pattern Analyzer =====")

    print("Enter text (type END on a new line to finish):")

    lines = []

    while True:
        line = input()

        if line.upper() == "END":
            break

        lines.append(line)

    text = " ".join(lines)

    words, frequency, palindromes = analyze_text(text)

    print("\n===== Analysis Report =====")
    print("Total words:", len(words))
    print("Unique words:", len(frequency))

    print("\nWord Frequencies:")

    for word, count in frequency.most_common():
        print(word, ":", count)

    print("\nPalindromes found:")

    if palindromes:
        print(", ".join(sorted(palindromes)))
    else:
        print("No palindromes found.")


if __name__ == "__main__":
    main()
