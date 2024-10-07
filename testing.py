
from tabulate import tabulate
import nltk
#nltk.download('punkt_tab')
import re


def search_words(s, arr):
    words = []
    for word in arr:
        if word in s:
            words.append(word)

    return words
       
def literals_result(s):
    literals = []
    for literal in s:
        if re.match(r"^[+-]?\d+$", literal):
            literals.append(literal)
    
    return literals

    





keywords = ["def", "return", "print"]
identifiers = ["add", "a", "b", "result"]
operators = ["=", "+"]
delimiters = ["(", ")", "{", "}", ",", ";", ":", "[", "]",]
literals = []

with open("file.txt", "r") as f:

    filetxt = ""

    for line in f:
        line = line.strip()
        if line and not line.startswith("#"):
            line = " ".join(line.split())
            filetxt += line + " " + "\n"
            

tokens = nltk.word_tokenize(filetxt)

print(filetxt)

keywords_result = search_words(tokens, keywords)
identifiers_result = search_words(tokens, identifiers)
operators_result = search_words(tokens, operators)
delimiters_result = search_words(tokens, delimiters)
literals_results = literals_result(tokens)


data = [
["Keywords", keywords_result],
["Identifiers", identifiers_result],
["Operators", operators_result],
["Delimiters", delimiters_result],
["Literals", literals_results]
]

table = tabulate(
    data,
    headers=["Category", "Tokens"],
    tablefmt="fancy_grid",

)
print(table)
print("\n")
print("Number of Tokens: ", len(tokens))