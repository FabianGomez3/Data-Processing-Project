
from tabulate import tabulate
import nltk
#nltk.download('punkt_tab')
import re
import keyword

#fuction that searches for specific words in an array and appends them
def search_words(s, arr):
    words = []
    for word in arr:
        if word in s:
            words.append(word)

    return words

#fuction that searches for number literals in an array and appends them
def literals_result(s):
    literals = []

    for literal in s:
        if re.match(r"^[+-]?\d+$", literal):
            literals.append(literal)
    return literals

#fuction that searches for words that aren't keywords (unfinished)
""" def searching_identifiers(s):
    ids = []
    for word in s:
        if not keyword.iskeyword(word):
            ids.append(word)
    return ids  """

#A list of arrays in each category
keywords = ["def", "return", "print", "for", "range","in", "and", "as", "assert", "break", "class", "continue", "del", "elif", "else", "except", "Await", "False", "True", "finally", "from", "global", "if", "import", "is", "with", "while", "try", "raise", "pass", "or", "not", "yield"]
operators = ["=", "+", "-", "%" , "*", "/" , "//", "**" , "<", ">"]
delimiters = ["(", ")", "{", "}", ",", ";", ":", "[", "]", "." , "_"]
identifiers = ["add", "a", "b", "result", "greet", "i", "count" ,"s", "string", "arr", "j", "word"]

#opening the file for reading
with open("file.txt", "r") as f:
    string = []
    filetxt = ""
    

#reads the file line by line and strips the spaces
    for line in f:
        line = line.strip()

#checks if line is empty and doesnt't start with # or else its skipped // splits string into list of words with a space between them and joined together
        if line and not line.startswith("#"):
            line = " ".join(line.split())
            new_txt = line.split("#")[0].strip()

#adds the text all together and gets searched for all double qouted strings
            if new_txt:
                filetxt += new_txt + "\n"
                matches = re.findall('"[^"]*"', new_txt)
                string += matches 

#tokenizes the file 
tokens = nltk.word_tokenize(filetxt)
print(filetxt)

#calling the fuctions
keywords_result = search_words(tokens, keywords)
identifiers_result = search_words(tokens, identifiers)
operators_result = search_words(tokens, operators)
delimiters_result = search_words(tokens, delimiters)
literals_results = literals_result(tokens)

#adding the double qouted strings to literals
literals_results += string

#sets the data for the table
data = [
["Keywords", keywords_result],
["Identifiers", identifiers_result],
["Operators", operators_result],
["Delimiters", delimiters_result],
["Literals", literals_results]
]

#makes the table for display
table = tabulate(
    data,
    headers=["Category", "Tokens"],
    tablefmt="fancy_grid",
)

#prints the table of tokens
print(table)
print("\n")
print("Number of Tokens: ", len(tokens))
