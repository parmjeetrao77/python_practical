from collections import Counter
import string

def clean_text(text):
    return "".join(
        char.lower()
        for char in text
        if char.isalnum()
    )


def are_anagrams(first, second):
    return Counter(clean_text(first)) == Counter(clean_text(second))


word1 = input("Enter first word or phrase: ")
word2 = input("Enter second word or phrase: ")

if are_anagrams(word1, word2):
    print("The inputs are anagrams.")
else:
    print("The inputs are not anagrams.")

text = input("\nEnter text to search: ")
pattern = input("Enter pattern to find: ")

if pattern.lower() in text.lower():
    print("Pattern found.")
else:
    print("Pattern not found.")